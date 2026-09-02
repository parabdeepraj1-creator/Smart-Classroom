from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import models
import schemas


# ============================================================
# CREATE DATABASE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="SmartSched API",
    description="Smart Classroom & Timetable Scheduler Backend",
    version="1.0.0",
)


# ============================================================
# ROOT
# ============================================================

@app.get("/", tags=["Health"])
def root():
    return {
        "message": "SmartSched API is running!"
    }


# ============================================================
# TEACHERS
# ============================================================

@app.get(
    "/teachers",
    response_model=list[schemas.TeacherResponse],
    tags=["Teachers"]
)
def get_teachers(
    db: Session = Depends(get_db)
):
    return db.query(models.Teacher).all()


@app.get(
    "/teachers/{teacher_id}",
    response_model=schemas.TeacherResponse,
    tags=["Teachers"]
)
def get_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    teacher = (
        db.query(models.Teacher)
        .filter(models.Teacher.id == teacher_id)
        .first()
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher


@app.post(
    "/teachers",
    response_model=schemas.TeacherResponse,
    status_code=201,
    tags=["Teachers"]
)
def create_teacher(
    teacher_data: schemas.TeacherCreate,
    db: Session = Depends(get_db)
):

    # Check duplicate teacher
    existing_teacher = (
        db.query(models.Teacher)
        .filter(models.Teacher.name == teacher_data.name)
        .first()
    )

    if existing_teacher:
        raise HTTPException(
            status_code=400,
            detail="Teacher already exists"
        )

    teacher = models.Teacher(
        name=teacher_data.name,
        subject=teacher_data.subject
    )

    db.add(teacher)
    db.commit()
    db.refresh(teacher)

    return teacher


@app.put(
    "/teachers/{teacher_id}",
    response_model=schemas.TeacherResponse,
    tags=["Teachers"]
)
def update_teacher(
    teacher_id: int,
    teacher_data: schemas.TeacherUpdate,
    db: Session = Depends(get_db)
):

    teacher = (
        db.query(models.Teacher)
        .filter(models.Teacher.id == teacher_id)
        .first()
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    if teacher_data.name is not None:

        duplicate = (
            db.query(models.Teacher)
            .filter(
                models.Teacher.name == teacher_data.name,
                models.Teacher.id != teacher_id
            )
            .first()
        )

        if duplicate:
            raise HTTPException(
                status_code=400,
                detail="Teacher with this name already exists"
            )

        teacher.name = teacher_data.name

    if teacher_data.subject is not None:
        teacher.subject = teacher_data.subject

    db.commit()
    db.refresh(teacher)

    return teacher


@app.delete(
    "/teachers/{teacher_id}",
    tags=["Teachers"]
)
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):

    teacher = (
        db.query(models.Teacher)
        .filter(models.Teacher.id == teacher_id)
        .first()
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    db.delete(teacher)
    db.commit()

    return {
        "message": "Teacher deleted successfully"
    }

# ============================================================
# SUBJECTS
# ============================================================

@app.get(
    "/subjects",
    response_model=list[schemas.SubjectResponse],
    tags=["Subjects"]
)
def get_subjects(
    db: Session = Depends(get_db)
):
    return db.query(models.Subject).all()


@app.get(
    "/subjects/{subject_id}",
    response_model=schemas.SubjectResponse,
    tags=["Subjects"]
)
def get_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):
    subject = (
        db.query(models.Subject)
        .filter(models.Subject.id == subject_id)
        .first()
    )

    if not subject:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    return subject


@app.post(
    "/subjects",
    response_model=schemas.SubjectResponse,
    status_code=201,
    tags=["Subjects"]
)
def create_subject(
    subject_data: schemas.SubjectCreate,
    db: Session = Depends(get_db)
):

    # Check teacher exists
    teacher = (
        db.query(models.Teacher)
        .filter(models.Teacher.id == subject_data.teacher_id)
        .first()
    )

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    # Check duplicate subject
    existing_subject = (
        db.query(models.Subject)
        .filter(models.Subject.name == subject_data.name)
        .first()
    )

    if existing_subject:
        raise HTTPException(
            status_code=400,
            detail="Subject already exists"
        )

    subject = models.Subject(
        name=subject_data.name,
        teacher_id=subject_data.teacher_id
    )

    db.add(subject)
    db.commit()
    db.refresh(subject)

    return subject


@app.put(
    "/subjects/{subject_id}",
    response_model=schemas.SubjectResponse,
    tags=["Subjects"]
)
def update_subject(
    subject_id: int,
    subject_data: schemas.SubjectUpdate,
    db: Session = Depends(get_db)
):

    subject = (
        db.query(models.Subject)
        .filter(models.Subject.id == subject_id)
        .first()
    )

    if not subject:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    # Update teacher if provided
    if subject_data.teacher_id is not None:

        teacher = (
            db.query(models.Teacher)
            .filter(
                models.Teacher.id == subject_data.teacher_id
            )
            .first()
        )

        if not teacher:
            raise HTTPException(
                status_code=404,
                detail="Teacher not found"
            )

        subject.teacher_id = subject_data.teacher_id

    # Update name if provided
    if subject_data.name is not None:

        duplicate = (
            db.query(models.Subject)
            .filter(
                models.Subject.name == subject_data.name,
                models.Subject.id != subject_id
            )
            .first()
        )

        if duplicate:
            raise HTTPException(
                status_code=400,
                detail="Subject with this name already exists"
            )

        subject.name = subject_data.name

    db.commit()
    db.refresh(subject)

    return subject


@app.delete(
    "/subjects/{subject_id}",
    tags=["Subjects"]
)
def delete_subject(
    subject_id: int,
    db: Session = Depends(get_db)
):

    subject = (
        db.query(models.Subject)
        .filter(models.Subject.id == subject_id)
        .first()
    )

    if not subject:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    db.delete(subject)
    db.commit()

    return {
        "message": "Subject deleted successfully"
    }


# ============================================================
# DIVISIONS
# ============================================================

@app.get("/divisions", tags=["Divisions"])
def get_divisions(
    db: Session = Depends(get_db)
):
    divisions = db.query(models.Division).all()
    return divisions


@app.get("/divisions/{division_id}", tags=["Divisions"])
def get_division(
    division_id: int,
    db: Session = Depends(get_db)
):
    division = (
        db.query(models.Division)
        .filter(models.Division.id == division_id)
        .first()
    )

    if not division:
        raise HTTPException(
            status_code=404,
            detail="Division not found"
        )

    return division


@app.post("/divisions", tags=["Divisions"])
def create_division(
    name: str,
    student_count: int,
    db: Session = Depends(get_db)
):
    division = models.Division(
        name=name,
        student_count=student_count
    )

    db.add(division)
    db.commit()
    db.refresh(division)

    return division


# ============================================================
# API INFORMATION
# ============================================================

@app.get("/api-info", tags=["Health"])
def api_info():
    return {
        "name": "SmartSched API",
        "version": "1.0.0",
        "swagger": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json"
    }