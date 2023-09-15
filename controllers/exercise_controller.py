from flask import Blueprint, render_template, redirect, request
from app import db
from models.exercise import Exercise
from models.workout import Workout

exercise_blueprint = Blueprint("/exercise", __name__)

# show all exercises

# edit exercises

# update exercsies

# delete exercise

# add exercise
# @exercise_blueprint.route("/exercise/new", methods=["POST"])
# def add_exercise():

@exercise_blueprint.route("/exercise")
def show_all():
    exercises = Exercise.query.all()
    workouts = Workout.query.all()
    return render_template("index.jinja", exercises=exercises, workouts=workouts)