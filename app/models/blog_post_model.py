from app import db
from sqlalchemy import Column, Integer, String, Text, Date


class BlogPostModel(db.Model):
    __tablename__ = "BlogPosts"

    id = Column(Integer, primary_key=True)
    post_name = Column(String(60), nullable=False)
    genre = Column(String(60), nullable=False)
    content = Column(Text, nullable=False)
    image_url = Column(String(150), nullable=False)
    creator_name = Column(String(80), nullable=False)
    creator_email = Column(String(80), nullable=False)
    creation_date = Column(Date, nullable=False)

    def __str__(self):
        return f"< Post, named: {self.name} - {self.id}>"

    def __repr__(self):
        return f"< Post, named: {self.name} - {self.id}>"