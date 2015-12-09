#!/usr/bin/env python
import shelve
from subprocess import check_output
import flask
from flask import request, Flask, render_template, jsonify, abort, redirect
from os import environ

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


import os
import sys
import json
import hashlib

app = flask.Flask(__name__)
GoogleMaps(app)
app.debug = True

db = shelve.open("map.db")

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route("/map")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png':[(37.4419, -122.1419)],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(37.4300, -122.1400)]}
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run()