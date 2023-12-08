import uuid

from sqlalchemy import Column, String, DateTime, Date, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    date = Column(Date)
    notes = Column(Text)

    exercises = relationship("WorkoutExercise", back_populates="workout")
