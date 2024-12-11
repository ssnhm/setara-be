from sqlalchemy import Column, DateTime, ForeignKey, func
import uuid
from sqlalchemy.dialects.postgresql import UUID 
from src.utils.db import db

class JobRecommendation(db.Model):
    __tablename__ = 'job_recommendations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    job_type_id = Column(UUID(as_uuid=True), ForeignKey('job_types.id'), nullable=False)
    
    created_at = Column(DateTime, default=func.now())


    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"