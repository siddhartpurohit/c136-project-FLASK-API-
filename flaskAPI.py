from flask import Flask, jsonify, request
from data import datas

app = Flask(__name__)
@app.route('/')

def datas_of_stars():
    return jsonify({
        'data': data,
        'message': 'success'
    }), 200

@app.route('/stars')

def stars_data():
    name = request.args.get('Star_name')
    star_data = next(item for item in data if item[name] == name)
    return jsonify({
        'data': star_data,
        'message': 'success'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)