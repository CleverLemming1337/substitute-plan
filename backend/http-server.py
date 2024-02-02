import database
from flask import Flask, request, jsonify

app = Flask(__name__)
connection = database.newConnection()
cursor = database.newCursor(connection)

@app.route('/', methods=['GET'])
def redirect_to_subst():
    return '', 308, {'Location': '/subst'}

@app.route('/subst', methods=['GET'])
def get_subst():
    x_version = request.headers.get('X-version')
    if x_version == '1':
        dbresponse = database.getAll(cursor)
        return jsonify(dbresponse), 200
    elif x_version == '2':
        dbresponse = database.getAll(cursor)
        keys = "id date class lesson teacher room notes".split()
        response_dict = {k:dbresponse[index] for index, k in enumerate(keys)}
        return jsonify(response_dict), 200
    else:
        return '', 400

@app.route('/subst', methods=['POST'])
def post_subst():
    x_version = request.headers.get('X-version')
    if x_version == '1':
        try:
            content = request.get_json()
            database.createEntry(cursor, content['date'], content['class'], content['lesson'], content['teacher'], content['room'], content['notes'])
            connection.commit()
            return '', 200
        except KeyError:
            return '', 400
    elif x_version == '2':
        try:
            content = request.get_json()
            database.createEntry(cursor, content['date'], content['class'], content['lesson'], content['teacher'], content['room'], content['notes'])
            connection.commit()
            return '', 200
        except KeyError:
            return '', 400
    else:
        return '', 400

@app.route('/subst', methods=['DELETE'])
def delete_subst():
    try:
        ids = request.get_json()
        for id in ids:
            database.deleteEntry(cursor, id)
        connection.commit()
        return '', 200
    except:
        return '', 400

if __name__ == '__main__':
    app.run(port=8000)
