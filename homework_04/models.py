"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    MetaData,
    create_engine,
)
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

import os


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@0.0.0.0:5522/postgres"
)

engine = create_engine(url=PG_CONN_URI, echo=False)
async_engine = create_async_engine(url=PG_CONN_URI, echo=False)

Session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

metadata = MetaData()


class Base:
    @declared_attr
    def __tablename__(cls):
        # return f"{cls.__name__.lower()}s"
        return f"{cls.__name__}"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, autoincrement=False)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(String(30), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True)

    posts = relationship("Post", back_populates="user", uselist=True)


class Post(Base):
    user_id = Column(Integer, ForeignKey("User.id"), unique=False, nullable=False)
    title = Column(String(90), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts", uselist=False)
