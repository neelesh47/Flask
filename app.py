from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return 'Value from hi there'

@app.route('/bye')
def bye():
    res_json = {
        'test' : "successful"
    }
    return jsonify(res_json)

@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    data_dict = request.get_json()
    if 'y' not in dataDict:
        return 'ERROR',305
    x=data_dict['x']
    y=data_dict['y']
    z=x+y
    resjson = {
        'result' : z
    }
    return jsonify(resjson)

if __name__ == "__main__":
    app.run()