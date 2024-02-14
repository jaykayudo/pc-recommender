from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from settings import app
import hashlib
from sqlalchemy.sql import func
import os

UPLOAD_FOLDER_PATH = os.path.join(os.path.dirname(__file__),"laptop_uploads")


db = SQLAlchemy(app)

def switch_image_path(old_path,id,name):
    if not os.path.exists(UPLOAD_FOLDER_PATH):
        os.mkdir(UPLOAD_FOLDER_PATH)
    extension = old_path.rsplit(".", maxsplit = 2)[1]
    new_path = os.path.join(UPLOAD_FOLDER_PATH,f"{id}_{name}.{extension}")
    os.replace(old_path,new_path)
    return new_path


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
        salt = "pcrecommender"
        gen_pass = password + salt
        hashed_pass = hashlib.md5(gen_pass.encode())
        return self.password == hashed_pass.hexdigest()
    def save(self):
        db.session.add(self)
        db.session.commit()
        return db

class CaseStudy(db.Model):
    __tablename__ = "casestudies"
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
    'casestudy_questions',
    db.Column('casestudy_id', db.Integer, db.ForeignKey('casestudies.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id'))
    )
    
question_choices = db.Table(
    'question_choices',
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('choices_id', db.Integer, db.ForeignKey('choices.id'))
    )
            
class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    order = db.Column(db.Integer)
    casestudies = db.relationship("CaseStudy",secondary=casestudy_questions,backref="questions")
    answer = db.Column(db.Integer,db.ForeignKey('choices.id'))
    choices = db.relationship("Choice",secondary=question_choices,backref="questions")
    def __repr__(self):
        return f'<Question "{self.title}">'
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


    
class Choice(db.Model):
    __tablename__ = "choices"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    question_id = db.Column(db.Integer,db.ForeignKey('questions.id'))
    score = db.Column(db.Integer);
    def __repr__(self):
        return f'<Choice "{self.title}" Question "{self.question}">'
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
        
class Laptop(db.Model):
    __tablename__ = "steps"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    ram = db.Column(db.String)
    storage = db.Column(db.String)
    processor = db.Column(db.String)
    resolution = db.Column(db.String)
    graphics = db.Column(db.String)
    image = db.Column(db.String)
    def __repr__(self):
        return f"<Laptop {self.name} >"
    def save(self):
        new_path = switch_image_path(self.image,self.id,self.name)
        self.image = new_path
        db.session.add(self)
        db.session.commit()
        return self

class Preference(db.Model):
    __tablename__ = "preferences"
    id = db.Column(db.Integer, primary_key = True)
    custom1 = db.Column(db.Integer, default = 0)
    custom2 = db.Column(db.Integer, default = 0)
    custom3 = db.Column(db.Integer, default = 0)
    weight = db.Column(db.Integer)
    mobility = db.Column(db.Integer)
    storage = db.Column(db.Integer)
    important_feature = db.Column(db.Integer)   
    def __repr__(self):
        return f"<Preference {self.custom1}-{self.custom2}-{self.custom3}-{self.weight}-{self.mobility}-{self.storage}-{self.important_feature} >"
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    
def minor_save():
    db.session.commit()

with app.app_context():
	db.create_all()