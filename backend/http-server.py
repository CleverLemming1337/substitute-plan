from flask import Flask, request, jsonify
import database

application = Flask(__name__)

@application.route('/', methods=['GET'])
def redirect_to_subst():
    return '', 308, {'Location': '/subst'}

@application.route('/subst', methods=['GET'])
def get_subst():
    connection = database.newConnection()
    cursor = database.newCursor(connection)
    x_version = request.headers.get('X-version')
    if x_version == '1':
        dbresponse = database.getAll(cursor)
        return jsonify(dbresponse), 200
    elif x_version == '2':
        dbresponse = database.getAll(cursor)
        print(dbresponse)
        keys = "id date class lesson subject teacher room notes".split()
        response = [{k:e[index] for index, k in enumerate(keys)} for e in dbresponse] # e stands for entry and k for key
        return jsonify(response), 200
    else:
        return '', 400

@application.route('/subst', methods=['POST'])
def post_subst():
    connection = database.newConnection()
    cursor = database.newCursor(connection)
    x_version = request.headers.get('X-version')
    if x_version == '1':
        try:
            content = request.get_json()
            database.createEntry(cursor, *content)
            connection.commit()
            return '', 200
        except KeyError:
            return '', 400
    elif x_version == '2':
        try:
            content = request.get_json()
            database.createEntry(cursor, content['date'], content['class'], content['lesson'], content['subject'], content['teacher'], content['room'], content['notes'])
            connection.commit()
            return '', 200
        except KeyError:
            return '', 400
    else:
        return '', 400

@application.route('/subst', methods=['DELETE'])
def delete_subst():
    connection = database.newConnection()
    cursor = database.newCursor(connection)
    try:
        ids = request.get_json()
        for id in ids:
            database.deleteEntry(cursor, id)
        connection.commit()
        return '', 200
    except KeyError: # not possible
        return '', 400

@application.route('/subst', methods=['PUT'])
def edit_subst():
    connection = database.newConnection()
    cursor = database.newCursor(connection)
    x_version = request.headers.get('X-version')
    content = request.get_json()
    if x_version == "1":
        try:
            database.updateEntry(cursor, content[0], content[1:])
            connection.commit()
        except IndexError:
            return '', 400
    elif x_version == "2":
        try:
            database.updateEntry(cursor, content['id'], (content['date'], content['class'], content['lesson'], content['subject'], content['teacher'], content['room'], content['notes']))
            connection.commit()
        except IndexError:
            return '', 400
    return '', 200
if __name__ == '__main__':
    application.run(port=8000)
