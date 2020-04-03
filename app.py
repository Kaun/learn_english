from flask import Flask, render_template, request
import json
import random
import create_json

app = Flask(__name__)

week = {"mon": "Понедельник", "tue": "Вторник", "wed": "Среда", "thu": "Четверг", "fri":"Пятница", "sat": "Суббота", "sun": "Воскресенье"}
icons = {"travel": "✈", "study": "🏫", "work": "🏢", "relocate": "🚗", "programming": "⌨"}

with open("teachers.json", "r") as f:
    teachers = json.load(f)

with open("goals.json", "r") as f:
    goals = json.load(f)


@app.route('/')
def route_index():
    teachers_random = random.sample(teachers, 6)
    return render_template('index.html', icons=icons, goals=goals, teachers=teachers_random)


@app.route('/allprofile')
def route_allprofile():
    return render_template('index.html', icons=icons, goals=goals, teachers=teachers)


@app.route('/goal/<goal>')
def route_goal(goal):
    teachers_goals = []
    for teacher in teachers:
        if goal in teacher["goals"]:
            teachers_goals.append(teacher)
    # sorting by rating
    teachers_goals = sorted(teachers_goals, key=lambda teacher: teacher["rating"], reverse=True)
    return render_template('goal.html', icon=icons[goal], teachers=teachers_goals, goal=goals[goal])


@app.route('/profiles/<id>')
def rout_profiles(id):
    teacher = teachers[int(id)]
    free_time = {}
    for day, hours in teacher["free"].items():
        free_hours = {}
        for hour, stat in hours.items():
            if stat:
                free_hours[hour] = stat
        free_time[day] = free_hours
    goals_names = []
    for goal in teacher["goals"]:
        goals_names.append(goals[goal])
    return render_template('profile.html', teacher=teacher, week=week, free_time=free_time, goals=goals_names)


@app.route('/booking/<id>/<day>/<hour>')
def rout_booking(id, day, hour):
    teacher = teachers[int(id)]
    return render_template('booking.html', teacher=teacher, week=week, day=day, hour=hour)


@app.route('/booking_done', methods=['POST'])
def rout_booking_done():
    booking = {}
    booking["clientTeacher"] = request.form["clientTeacher"]
    booking["clientName"] = request.form["clientName"]
    booking["clientPhone"] = request.form["clientPhone"]
    booking["clientTime"] = request.form["clientTime"]
    booking["clientWeekday"] = request.form["clientWeekday"]
    with open("booking.json", "a") as file:
        json.dump(booking, file)
        file.write(",")
    return render_template('booking_done.html', day=week[request.form["clientWeekday"]],
                           hour=request.form["clientTime"], name=request.form["clientName"],
                           phone=request.form["clientPhone"])


@app.route('/request')
def rout_request():
    return render_template('request.html')


@app.route('/request_done', methods=['POST'])
def rout_request_done():
    request_user = {}
    request_user["clientName"] = request.form["clientName"]
    request_user["clientPhone"] = request.form["clientPhone"]
    request_user["goal"] = request.form["goal"]
    request_user["time"] = request.form["time"]
    with open("request.json", "a") as fr:
        json.dump(request_user, fr)
        fr.write(",")
    return render_template('request_done.html', goal=goals[request.form["goal"]],
                           time=request.form["time"], name=request_user["clientName"],
                           phone=request.form["clientPhone"])


if __name__ == '__main__':
    app.run()

