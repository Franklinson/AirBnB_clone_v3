#!/usr/bin/python3
"""index file"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from flask import Flask


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns a JSON"""
    return jsonify({"status": "OK"})
