from flask import Flask
from flask import jsonify

app = Flask(__name__)

asd = ''


@app.route('/api/<group_num>')
def index(group_num):
    try:
        data = open('api/' + group_num + '.json')
        return data.read()
    except:
        return jsonify(
            responseCode='404'
        )


@app.errorhandler(404)
def not_found_error(error):
    error_code = '404'
    print(error)
    return jsonify(error_code)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
