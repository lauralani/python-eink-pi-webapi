#!/usr/bin/env python3

from os import write
from libapp import *
from libeink import *
import logging
from config import *
from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file


logging.basicConfig(level=loglevel)


app = Flask(__name__)


@app.route("/", methods=["GET"])
async def index_get():
    if request.headers["x-api-key"] != apikey:
        return {
            "status": "unauthorized"
        }, 403

    try:
        temp = get_temp()
        voltage = get_voltage()
        status = "success"
    except:
        temp = None
        voltage = None
        status = "not supported"

    return {
        "status": status,
        "temperature": temp,
        "voltage": voltage
    }


@app.route("/text", methods=["POST"])
async def text_post():
    if request.headers["x-api-key"] != apikey:
        return {"status": "unauthorized"}, 403
    body = request.get_json()

    if not 'text' in body:
        logging.debug("'text' is missing in request body")
        return {"status": "bad request"}, 400
    if not 'fontsize' in body:
        logging.debug("'fontsize' is missing in request body")
        return {"status": "bad request"}, 400

    try:
        logging.debug(f"text: {body['text']}")
        logging.debug(f"font: {int(body['fontsize'])}")

        response = await set_display_text(body['text'], int(body['fontsize']))

        if response == 'success':
            return {
                "status": "success",
                "text" : body['text'],
                "fontsize": int(body['fontsize'])
            }
        else:
            return {"status": response}, 500
    except Exception as e:
        logging.error(e)
        return {"error": str(e)}, 500

@app.route("/text", methods=["GET"])
async def text_get():
    return send_file(".display.png", mimetype='image/png')

@app.route("/text/clear", methods=["POST"])
async def text_clear_post():
    response = await clear_display()
    return {"status": response}
