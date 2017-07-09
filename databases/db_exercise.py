import sqlite3
import psycopg2


def create_table():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL ) ")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("select * from store")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def deleteAllRows():
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("delete from store")
    conn.commit()
    conn.close()


def deleteRow(item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute("delete from store where item = ?", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()
    cursor.execute(
        "update store set quantity=?,price=? where item = ?", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
insert("Coffee Cup", 10, 10.5)
deleteRow("Coffee Cup")

update(5, 20, "Water-Glass")

print(view())
result = view()


for i in result:
    print(i[0] + " " + str(i[1]) + " " + str(i[2]) + "\n")
