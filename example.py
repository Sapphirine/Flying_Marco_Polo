# coding: utf-8

from flask import Flask, redirect, request, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import test

app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

PATH = [(39.904211, 116.407395), (-33.868820, 151.209296),
(35.689487, 139.691706), (49.282729, -123.120738), 
(40.712784, -74.005941),(51.507351, -0.127758),
(-26.204103, 28.047305),(41.008238, 28.978359), 
(1.352083, 103.819836),(39.904211, 116.407395)]
PATHMARKERS = [(39.904211, 116.407395, "Beijing"), (-33.868820, 151.209296, "Sydney")]
HEADER = ""
DETAIL = ""

@app.route('/')
def mapview():
    plinemap = Map(
        identifier="plinemap",
        varname="plinemap",
        lat=7.7700891,
        lng=150.7348494,
        style="height:530px;width:1000px;margin:0;",
        zoom=2,
        polylines = [PATH],
        markers = PATHMARKERS,
        scroll_wheel = False
    )

    return render_template(
        'example.html',
        airline=HEADER,
        detail=DETAIL,
        plinemap=plinemap,
    )

@app.route('/plan', methods=['POST'])
def calculate():
    mode = request.form['mode']
    global PATH, PATHMARKERS, HEADER, DETAIL
    PATH, PATHMARKERS, DETAIL = test.citylist(mode)

    return redirect('/')

@app.route('/custom_plan', methods=['POST'])
def customize():    
    city_list = request.form['city_list']
    global PATH, PATHMARKERS, HEADER, DETAIL
    PATH, PATHMARKERS, DETAIL=test.citylist('4',city_list)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host = '0.0.0.0', port = 80)
