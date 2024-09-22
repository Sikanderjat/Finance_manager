import sqlite3
conn = sqlite3.connect('finance_manager.db')
c = conn.cursor()
c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='income';''')

def create_user_table():
    
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    con_password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
   

    # conn.close()
# create_user_table()
def create_income_table():
    c.execute('''CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')
    conn.commit()
    # conn.close()

def create_expenses_table():
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                    )''')
    conn.commit()
    # conn.close()
def get_all_users():
    try:
        c.execute('''SELECT * FROM users''')
        users = c.fetchall()
        for user in users:
            print(f"ID: {user[0]}")
            print(f"Username: {user[1]}")
            print(f"email: {user[2]}")
            print(f"Password Hash: {user[3]}")
            print(f"Created At: {user[5]}")
            print("------------------------")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    conn.commit()
    conn.close()


def get_users(username):
    try:
        c.execute('''SELECT * FROM users where username=?''',(username,))
        users = c.fetchall()
        for user in users:
            print(f"ID: {user[0]}")
            print(f"Username: {user[1]}")
            print(f"email: {user[2]}")
            print(f"Password Hash: {user[3]}")
            print(f"Created At: {user[5]}")
            print("------------------------")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    conn.commit()
    conn.close()
# get_all_users()
# get_users("sikander")

# conn.close()
