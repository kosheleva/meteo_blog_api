from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

from os import getenv
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = getenv('DB_URL')
HASH_METHOD = getenv('HASH_METHOD')

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_all(db, model, offset, limit):
    return db.query(model).offset(offset).limit(limit).all()


def get_by_id(db, model, id):
    return db.query(model).filter(model.id == id).first()


def get_by_ids(db, model, ids):
    return db.query(model).filter(model.id.in_(ids)).all()


def create(db, new_record):
    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


def update(db, existed_record, new_record):
    for key, value in new_record.__dict__.items():
        setattr(
            existed_record,
            key,
            value if key != 'password' else generate_password_hash(value, method=HASH_METHOD)
        )

    db.commit()
    db.refresh(existed_record)

    return existed_record


def delete(db, model, id):
    db.query(model).filter_by(id=id).delete()
    db.commit()

    return True