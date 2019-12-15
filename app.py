from flask import *
from src.stores import *

app = Flask(__name__, template_folder="./app/templates/", static_folder="./app/static/")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get-postcodes-coordinates', methods=['POST'])
def get_postcodes_coordinates():
    return jsonify(bulk_coordinates_download(request.form.getlist("postcodes[]")))


@app.route('/get-postcodes-radius', methods=['POST'])
def get_postcodes_radius():
    postcodes = request.form.getlist("postcodes[]")
    radius = float(request.form.get("radius"))
    radius_postcode = request.form.get("radiusPostcode")

    print(radius)
    print(radius_postcode)

    return jsonify(bulk_coordinates_download(postcodes))


if __name__ == '__main__':
    app.run()
