
import flask
from flask import Flask, jsonify, request, redirect
from Blockchain import app
import datetime as DT


@app.route('/')
def default_home():
    return redirect("/healthcheck")

# create /healthcheck endpoint
@app.route('/healthcheck', methods=['GET', 'POST'])
def health_check():
    response = {
       'datetime': str(DT.datetime.now()),
       'health': 'OK'
    }
    return jsonify(response), 200, {'Content-Type': 'application/json', 'Cache-Control': 'no-cache'}


