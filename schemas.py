from pydantic import BaseModel, Field
from datetime import time


# ============================================================
# TEACHER
# ============================================================

class TeacherCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    subject: str = Field(..., min_length=2, max_length=100)


class TeacherUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    subject: str | None = Field(None, min_length=2, max_length=100)


class TeacherResponse(BaseModel):
    id: int
    name: str
    subject: str

    class Config:
        from_attributes = True


# ============================================================
# SUBJECT
# ============================================================

class SubjectCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    teacher_id: int = Field(..., gt=0)


class SubjectUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    teacher_id: int | None = Field(None, gt=0)


class SubjectResponse(BaseModel):
    id: int
    name: str
    teacher_id: int

    class Config:
        from_attributes = True


# ============================================================
# DIVISION
# ============================================================

class DivisionCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    student_count: int = Field(..., gt=0)


class DivisionUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=50)
    student_count: int | None = Field(None, gt=0)


class DivisionResponse(BaseModel):
    id: int
    name: str
    student_count: int

    class Config:
        from_attributes = True


# ============================================================
# CLASSROOM
# ============================================================

class ClassroomCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    capacity: int = Field(..., gt=0)
    type: str = Field(..., min_length=2, max_length=50)


class ClassroomUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    capacity: int | None = Field(None, gt=0)
    type: str | None = Field(None, min_length=2, max_length=50)


class ClassroomResponse(BaseModel):
    id: int
    name: str
    capacity: int
    type: str

    class Config:
        from_attributes = True


# ============================================================
# PERIOD
# ============================================================

class PeriodCreate(BaseModel):
    day: str = Field(..., min_length=1, max_length=20)
    start_time: time
    end_time: time


class PeriodUpdate(BaseModel):
    day: str | None = Field(None, min_length=1, max_length=20)
    start_time: time | None = None
    end_time: time | None = None


class PeriodResponse(BaseModel):
    id: int
    day: str
    start_time: time
    end_time: time

    class Config:
        from_attributes = True


# ============================================================
# TEACHER AVAILABILITY
# ============================================================

class TeacherAvailabilityCreate(BaseModel):
    teacher_id: int = Field(..., gt=0)
    day: str = Field(..., min_length=1, max_length=20)
    start_time: time
    end_time: time
    available: int = Field(default=1, ge=0, le=1)


class TeacherAvailabilityUpdate(BaseModel):
    teacher_id: int | None = Field(None, gt=0)
    day: str | None = Field(None, min_length=1, max_length=20)
    start_time: time | None = None
    end_time: time | None = None
    available: int | None = Field(None, ge=0, le=1)


class TeacherAvailabilityResponse(BaseModel):
    id: int
    teacher_id: int
    day: str
    start_time: time
    end_time: time
    available: int

    class Config:
        from_attributes = True


# ============================================================
# TIMETABLE
# ============================================================

class TimetableResponse(BaseModel):
    id: int
    day: str
    period_id: int
    subject_id: int
    teacher_id: int
    classroom_id: int
    division_id: int

    class Config:
        from_attributes = True