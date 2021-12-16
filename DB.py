from flask import Flask, render_template,redirect, request, flash, url_for, session
from flask_sqlalchemy import SQLAlchemy
from random import randint, randrange

app = Flask(__name__)
app.config['SQLALCHAMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "Random String"

db =SQLAlchemy(app)

class Device(db.Model):
    deviceid = db.Column('device_id', db.Integer,  primary_key=True)
    licenseid = db.Column(db.Integer)
    device_name = db.Column(db.String())

    def __init__(self, deviceid, licenseid, device_name):
        self.deviceid = deviceid
        self.licenseid = licenseid
        self.device_name = device_name


db.create_all()


@app.route('/', methods = ["GET", "POST"])
def entry_page():
    if request.method == "POST":
        devices = Device.query.all()
        for device in devices:
            if request.form['device_name'] == device.device_name:
               # flash(f"device name {device.device_name} found, their device id is {device.deviceid} and licensing id is {device.licenseid}")
                return render_template("final_page_found.html", device=device)
        device = Device(device_name=request.form["device_name"], deviceid=randint(100,999), licenseid=randint(1000, 9000) )
        db.session.add(device)
        db.session.commit()
        return render_template("final_page_not.html", device=device)
    return render_template("entry_page.html")
"""
@app.route('/api_response', methods= ["GET", "POST"])
def api_response():
    if request.method == "POST":
        for device in devices:
            if request.form['device_name'] == device.device_name:
                # flash(f"device name {device.device_name} found, their device id is {device.deviceid} and licensing id is {device.licenseid}")
                return render_template("final_page_found.html", device=device)
        device = Device(device_name=request.form["device_name"], deviceid=randint(100, 999),
                        licenseid=randint(1000, 9000))
        db.session.add(device)
        db.session.commit()
        return render_template("final_page_not.html", device=device)

"""

