from flask import Flask, request
from controller import PhonesCodes, structure_scan, find_difference

app = Flask(__name__)

code = PhonesCodes()


@app.route("/login", methods=["GET", "POST"])
def get_n_check_code():
    code.request = request
    if request.method == "GET":
        return code.generate_code()
    elif request.method == "POST":
        return code.check_phone()


@app.route("/structure", methods=["GET"])
def structure():
    url = request.args.get('link') or 'https://freestylo.ru/'
    tags = request.args.get('tags')
    try:
        required_tags = tags.split(sep=',')
        return structure_scan(url, required_tags)
    except AttributeError:
        pass
    return structure_scan(url)


@app.route("/check_structure", methods=["POST"])
def check_structure():
    req = request.get_json()
    url = req['link']
    structure = req['structure']
    return find_difference(url, structure)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
