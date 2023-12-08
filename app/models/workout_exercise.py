import uuid

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class WorkoutExercise(Base):
    __tablename__ = 'workout_exercises'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workout_id = Column(UUID(as_uuid=True), ForeignKey('workouts.id'))
    exercise_id = Column(UUID(as_uuid=True), ForeignKey('exercises.id'))
    sets = Column(Integer)
    reps = Column(Integer)

    workout = relationship("Workout", back_populates="exercises")
    exercise = relationship("Exercise", back_populates="workouts")
