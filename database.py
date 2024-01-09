import sqlite3
import datetime

connection = sqlite3.Connection("database.sql")
cursor = connection.cursor()

def newTable(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS substitues (date TEXT, class TEXT, hour NUMBER, teacher TEXT, room TEXT, notes TEXT)")

def createEntry(cursor, date, _class, hour, teacher, room, notes):
    cursor.execute("INSERT INTO substitues VALUES (?, ?, ?, ?, ?, ?)", (date, _class, hour, teacher, room, notes))

def getByClass(cursor, _class):
    cursor.execute("SELECT rowid, * FROM substitues WHERE class == ?", (_class,))
    return cursor.fetchall()

def getByTeacher(cursor, teacher):
    cursor.execute("SELECT rowid, * FROM substitues WHERE teacher == ?", (teacher,))
    return cursor.fetchall()

def filterByDate(data, year, month, day): # could also be a huge list comprehension
    filtered = []
    for i in data:
        if i[1] == "-".join([day, month, year]):
            filtered.append(i)
    return filtered

    
newTable(cursor)
createEntry(cursor, "10-1-24", "7a", 5, "ABC", "123", "")
connection.commit()

print(filterByDate(getByClass(cursor, "7a"), "24", "1", "9"))