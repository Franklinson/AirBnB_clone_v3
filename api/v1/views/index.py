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


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrive number of objects"""
    stats = {}
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]

    for cls in classes:
        stats[cls] = storage.count(cls)

    return jsonify(stats)
