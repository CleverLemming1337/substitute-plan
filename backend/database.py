import sqlite3
import datetime

def newConnection():
    return sqlite3.Connection("database.sql")

def newCursor(connection):
    return connection.cursor()

def newTable(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS subst (date TEXT, class TEXT, lesson NUMBER, subject TEXT, teacher TEXT, room TEXT, notes TEXT)")

def createEntry(cursor, date, _class, lesson, subject, teacher, room, notes):
    cursor.execute("INSERT INTO subst VALUES (?, ?, ?, ?, ?, ?, ?)", (date, _class, lesson, subject, teacher, room, notes))

def getByClass(cursor, _class):
    cursor.execute("SELECT rowid, * FROM subst WHERE class == ?", (_class,))
    return cursor.fetchall()

def getByTeacher(cursor, teacher):
    cursor.execute("SELECT rowid, * FROM subst WHERE teacher == ?", (teacher,))
    return cursor.fetchall()

def deleteEntry(cursor, id):
    cursor.execute("DELETE FROM subst WHERE rowid == ?", (id,))

def updateEntry(cursor, id, values):
    if len(values) != 8:
        raise IndexError("Invalid number of values")
    cursor.execute("UPDATE subst SET date=?, class=?, lesson=?, subject=?, teacher=?, room=?, notes=? WHERE rowid == ?", (*values, id))

def filterByDate(data, year, month, day): # could also be a huge list comprehension
    filtered = []
    for i in data:
        if i[1] == "-".join([day, month, year]):
            filtered.append(i)
    return filtered

def filterByTeacher(data, teacher): # could also be a huge list comprehension
    filtered = []
    for i in data:
        if i[1] == teacher:
            filtered.append(i)
    return filtered

def getAll(cursor):
    cursor.execute("SELECT rowid, * FROM subst")
    return cursor.fetchall()

if __name__ == "__main__":
    connection = sqlite3.Connection("database.sql")
    cursor = connection.cursor()
        
    newTable(cursor)

    createEntry(cursor, "10-1-24", "7a", 5, "Math", "ABC", "123", "")
    connection.commit()
    print(getAll(cursor))