#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template, request
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/')
def display_index():
    """Generate page with popdown menu of states/cities"""
    return render_template('index.html')

@app.route('/dashboard')
def display_main():
    """Generate main page with data of the user"""
    args = request.args
    args.to_dict
    clientID = args.get("id")
    print(clientID)
    # get user data and render menu page with data
    return render_template('menu.html')

@app.route('/config')
def display_settings():
    """Generate main page with data of the user"""
    args = request.args
    args.to_dict
    clientID = args.get("id")
    print(clientID)
    # get user settings and render change settings page with it
    return render_template('change_settings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)