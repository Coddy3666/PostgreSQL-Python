import psycopg2

conn = psycopg2.connect(database='netologydb', user='postgres', password='Coddy3666SQL')

with conn.cursor() as cur:
    cur.execute("DROP TABLE client;")

with conn.cursor() as cur:
    cur.execute("""CREATE TABLE client(id SERIAL PRIMARY KEY,
                firstname VARCHAR(20),
                lastname VARCHAR(20),
                email VARCHAR(100),
                phone INTEGER check (phone<99999999999)
                );""")
    conn.commit()



class Client:

    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone

    def adddb(self):
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO client(firstname, lastname, email, phone) VALUES(first, last, email, phone)
                        ;""")
            conn.commit()

client1 = Client('Mark','Veselov','wmarka@rambler.ru',89039472925)
client1.adddb()
cur.execute("SELECT * FROM client;")
print(cur.fetchall())

conn.close()