import json
import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_nav import Nav, register_renderer
from flask_nav.elements import Navbar, View

from generate_map import generate_map
from navbar_renderer import NavbarRenderer

load_dotenv()
app = Flask(__name__)

# Create dynamic navbar instance
nav_bar = Navbar('Navigation',
                 View('Home', 'index'),
                 View('Work Experience', 'experience'),
                 View('Map', 'map_test')
                 )
# Initialize and register Nav library
nav = Nav()
nav.register_element('navigation', nav_bar)
nav.init_app(app)
# Register the custom navbar renderer
register_renderer(app, 'navbar', NavbarRenderer)

# Load the JSON data with group member info
json_path = os.path.join(app.root_path, "static/data", "group.json")
json_data = json.load(open(json_path))

# Generate the Folium map HTML
generate_map(os.path.join(app.root_path, "templates/generated", "generated_map.html"), json_data)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/experience')
def experience():
    return render_template('experience.html', jobs=[])


@app.route('/map')
def map_test():
    return render_template('map.html')
