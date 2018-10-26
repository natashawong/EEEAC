import pg8000
import passwords from app.passwords
from app.envirionments import ENVIRONMENTS

db = {
"DB_HOST" : "localhost",
"DB" : "PostgreSQL 9.6",
"DB_USER" : "postgres",
"DB_PORT" : 5432
}

conn = pg8000.connect(host=db["DB_HOST"], port=db["DB_PORT"], user=db["DB_USER"], password='dragon')

cursor = conn.cursor()
cursor.execute("CREATE TEMPORARY TABLE blacklist (id SERIAL, title TEXT)")
cursor.execute(
    "INSERT INTO blacklist (title) VALUES (%s), (%s), (%s) RETURNING id, title",
    ("superman@bankryptonite.org", "noname@anon.net", "invisibleman@invisibleemail.com"))
results = cursor.fetchall()
for row in results:
    id, title = row
    print("id = %s, title = %s" % (id, title))
s = "SELECT title from blacklist where title like 'n%'"
cursor.execute(s)
print(cursor.fetchall())

def deleter(term):
    s = "DELETE FROM blacklist where title = '" + term + "'"
    cursor.execute(s)
    print('deleted ' + term)
    return

def addtoDB(email):
    cursor.execute(
        "INSERT INTO blacklist (title) VALUES ('%s') RETURNING id, title"%
        str(email))
    return


def dataSearch(term):
    s = "SELECT title from blacklist where title like " + "'%" + term + "%'"
    cursor.execute(s)
    x = cursor.fetchall()
    data = []
    for i in range(0, len(x)):  # to get the data out of the tuple that cursor.fetchall puts it in
        data += x[i]
    return data