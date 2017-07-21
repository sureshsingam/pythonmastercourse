import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL ) ")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    # Open to SQL injection
    #cursor.execute("INSERT INTO store VALUES('{0}', {1}, {2})".format(item, quantity, price))

    # the following is protected from SQL injection
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)",
                   (item, quantity, price))

    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("select * from store")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def deleteAllRows():
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("delete from store")
    conn.commit()
    conn.close()


def deleteRow(item):
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("delete from store where item = %s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname='postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute(
        "update store set quantity=%s,price=%s where item = %s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()

insert("Sake-Glass", 20, 1.5)

deleteRow("Coffee Cup")

update(5, 10, "Water-Glass")

print(view())
result = view()


for i in result:
    print(i[0] + " " + str(i[1]) + " " + str(i[2]) + "\n")
