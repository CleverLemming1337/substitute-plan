# This file is for gunicorn setup

import database

connection = database.newConnection()
cursor = database.newCursor(connection)

database.newTable(cursor)

connection.commit()

connection.close()