from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.orm import relationship

from database import Base


# =========================
# TEACHERS
# =========================

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    subject = Column(String(100), nullable=False)

    subjects = relationship("Subject", back_populates="teacher")
    availability = relationship("TeacherAvailability", back_populates="teacher")


# =========================
# SUBJECTS
# =========================

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)

    teacher = relationship("Teacher", back_populates="subjects")


# =========================
# DIVISIONS
# =========================

class Division(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    student_count = Column(Integer, nullable=False)


# =========================
# CLASSROOMS
# =========================

class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False)


# =========================
# PERIODS
# =========================

class Period(Base):
    __tablename__ = "periods"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String(20), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)


# =========================
# TEACHER AVAILABILITY
# =========================

class TeacherAvailability(Base):
    __tablename__ = "teacher_availability"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    day = Column(String(20), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    available = Column(Integer, default=1)

    teacher = relationship("Teacher", back_populates="availability")


# =========================
# TIMETABLE
# =========================

class Timetable(Base):
    __tablename__ = "timetable"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String(20), nullable=False)

    period_id = Column(Integer, ForeignKey("periods.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    division_id = Column(Integer, ForeignKey("divisions.id"), nullable=False)