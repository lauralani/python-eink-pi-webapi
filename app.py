#!/usr/bin/env python3

import subprocess
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index_get():
    temp = get_temp()
    voltage = get_voltage()

    return {
        "temperature": temp,
        "voltage": voltage
    }

def get_temp():
    raw = subprocess.run(['/opt/vc/bin/vcgencmd', 'measure_temp'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # temp=37.9'C
    tempstring = raw.replace("temp=", "").replace("'C", "")
    return float(tempstring)

def get_voltage():
    raw = subprocess.run(['/opt/vc/bin/vcgencmd', 'measure_volts'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # volt=1.2000V
    voltstring = raw.replace("volt=", "").replace("V", "")
    return float(voltstring)
