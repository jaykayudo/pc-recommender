from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from settings import app
import hashlib
from sqlalchemy.sql import func



db = SQLAlchemy(app)

class Admin(db.Model):
    __tablename__="admin"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def set_password(self, password):
        salt = "pcrecommender"
        gen_pass = password + salt
        hashed_pass = hashlib.md5(gen_pass.encode())
        self.password = hashed_pass.hexdigest()
    def check_password(self,password):
        salt = "dinero"
        gen_pass = password + salt;hashed_pass = hashlib.md5(gen_pass.encode())
        return self.password == hashed_pass.hexdigest()
    def save(self):
        db.session.add(self)
        db.session.commit()
        return db

class CaseStudy(db.Model):
    __tablename__ = "case_studies"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<CaseStudy "{self.title}">'
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

casestudy_questions = db.Table(
    'question_choices',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('choices_id', db.Integer, db.ForeignKey('choices.id'))
    )    

            
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    order = db.Column(db.Integer)
    answer = db.Column(db.Integer,db.ForeignKey('choices.id'))
    choices = db.relationship("Choices",secondary=question_choices,backref="questions")
    def __repr__(self):
        return f'<Question "{self.title}">'
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

question_choices = db.Table(
    'question_choices',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('choices_id', db.Integer, db.ForeignKey('choices.id'))
    )
    
class Choice(db.Model):
    __tablename__ = "choices"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    questions = db.relationship('Question', backref='questions')
    score = db.Column(d.Integer);
    def __repr__(self):
        return f'<Choice "{self.title}" Question "{self.questions}">'
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
        
class Laptop(db.Model):
    __tablename__ = "steps"

    id = db.Column(db.Integer, primary_key = True)
    solution_id = db.Column(db.Integer,db.ForeignKey('solutions.id'))
    step = db.Column(db.String)
    order = db.Column(db.Integer)
    def __repr__(self):
        return f"<Laptop {self.step} >"
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
def minor_save():
    db.session.commit()

with app.app_context():
	db.create_all()