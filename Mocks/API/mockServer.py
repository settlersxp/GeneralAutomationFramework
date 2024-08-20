# a small flask server to serve the mock data

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    employees = [
        {
            'id': 1,
            'name': 'John Doe',
            'email': ''
        },
        {
            'id': 2,
            'name': 'Jane Doe',
            'email': ''
        }
    ]
    return jsonify(employees)


if __name__ == '__main__':
    app.run(port=5000)