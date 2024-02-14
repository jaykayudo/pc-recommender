from flask import render_template, request, session, flash, redirect, url_for,jsonify
from settings import app
import json
import models
from flask_restful import Resource, Api

api = Api(app)

def serialize_data(data, many = False):
    def map_function(dict_data):
        dictdata = dict_data.__dict__
        dictdata.pop('_sa_instance_state')
        return dictdata
    if type(data) == list:
        return list(map(map_function, data))
    else:
        return map_function(data)


class DashboardView(Resource):
    def get(self):
        casestudy = models.CaseStudy.query.all()
        return serialize_data(casestudy, many=True)
    def post(self):
        casestudies = request.form.getlist('casestudy')
        questions_list = [

        ]
        for casetudy in casestudies:
            questions = models.Question.query.filter_by(casestudy_id = casetudy)
            questions_list.append(questions)
        
        return questions_list, 201


class CaseStudyView(Resource):
    def get(self):
        casestudy = models.CaseStudy.query.all()
        return serialize_data(casestudy,many = True), 200
    def post(self):
        """
        Create a new casestudy entity

        Post data needed;
        `title`: str (required)
        `description`: str (required)
        """
        data = request.form
        try:
            casestudy = models.CaseStudy(title = data['title'], description = data['description'])
            casestudy.save()
            return {'message':"Casestudy Added"},200
        except:
            return {'message':"Bad Request"}, 400
class QuestionsView(Resource):
    def get(self):
        questions = models.Question.query.all()
        return serialize_data(questions), 200
    def post(self):
        data = request.form
        question_data = data['question']
        choices_data = data.getlist("choices")
        casestudy_ids = data.getlist('casestudy_id')
        question = models.Question(title = question_data)
        question.save()
        choices = [question.choices.append(models.Choice(choice).save()) for choice in choices_data]
        models.minor_save()
        for casestudy_id in casestudy_ids:
            casestudy = models.CaseStudy.query.get(int(casestudy_id))
            casestudy.save()
            question.casestudies.append(casestudy)
        models.minor_save()
        return {'message':"Questions Created"}, 201

        

api.add_resource(DashboardView,"/")
api.add_resource(CaseStudyView,"/casestudy")
api.add_resource(QuestionsView,"/questions")

