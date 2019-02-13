from flask import Flask, jsonify

from manifest_server.inventory import get_manifest


app = Flask(__name__)


@app.route("/collection/<machineid>/manifest")
def hello_world(machineid):
    manifest = get_manifest(machineid)
    return jsonify(manifest)
