#!/usr/bin/env python3

from os import write
from libapp import *
from libeink import *
import logging
from flask import Flask
from flask import request
from flask import jsonify

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

@app.route("/", methods=["GET"])
async def index_get():
    try:
        temp = get_temp()
        voltage = get_voltage()
    except:
        temp = None
        voltage = None

    return {
        "temperature": temp,
        "voltage": voltage
    }

@app.route("/text", methods=["POST"])
async def text_post():
    body = request.get_json()
    try:
        logging.debug(f"text: {body['text']}")
        logging.debug(f"font: {int(body['fontsize'])}")

        response = await set_display_text(body['text'], int(body['fontsize']))
        return { "message": response }
    except Exception as e:
        logging.error(e);
        return { "error": e }
