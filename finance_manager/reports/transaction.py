import sqlite3
conn = sqlite3.connect('finance_manager.db')
cursor = conn.cursor()
def get_user_id(username):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    return result[0] if result else None

def add_transaction(t_type,username,amount,description,date):
    
    transaction_type = t_type
    if transaction_type=="income":
        # username=input("Enter Your User Name:")
        user_id=get_user_id(username)
        # amount = float(input("Enter amount: "))
        # description = input("Enter description: ")
        # date = input("Enter date (YYYY-MM-DD): ")

        conn=sqlite3.connect('finance_manager.db')
        c=conn.cursor()
        c.execute('''
            INSERT INTO income (user_id,amount, description, date) 
            VALUES (?, ?, ?,?)''', (user_id,amount, description, date))
        conn.commit()
        print(f"{transaction_type.capitalize()} added successfully!")
        conn.close()
    elif transaction_type=="expense":
        user_id=get_user_id(username)
        # amount = float(input("Enter amount: "))
        # description = input("Enter description: ")
        # date = input("Enter date (YYYY-MM-DD): ")

        conn=sqlite3.connect('finance_manager.db')
        c=conn.cursor()
        c.execute('''
            INSERT INTO expenses (user_id,amount, description, date) 
            VALUES (?, ?, ?,?)''', (user_id,amount, description, date))
        conn.commit()
        print(f"{transaction_type.capitalize()} added successfully!")
        conn.close()

    else:
        print("Enter Valid Input")
    conn.close()
def edit_transaction(t_type,username,id,amount,description,date):
    transaction_type = t_type
    if transaction_type=="income":
        user_id=get_user_id(username)
        # income_id=input("Enter input id : ")
        # amount=float(input("Enter New Amount : "))
        # description=input("Enter New Description : ")
        # date=input("Enter New Date (YYYY-MM-DD): ")
        with sqlite3.connect('finance_manager.db',check_same_thread=False) as conn:
            c=conn.cursor()
            c.execute("SELECT * FROM income WHERE id = ? and user_id=?", (id, user_id))
            if c.fetchone():  # Check if the record exists
                c.execute("UPDATE income SET amount = ?, description = ?, date = ? WHERE id = ? and user_id =?",
                       (amount, description, date, id,user_id))
                conn.commit()
                mas=f"{transaction_type.capitalize()} update successfully!"
                return msg
            else:
                msg=f"Error: Income ID {id} not found for user {username}."
                print(msg)
                return msg
        conn.close()

    elif transaction_type=="expense":
        user_id=get_user_id(username)
        # expense_id=input("Enter input id : ")
        # amount=float(input("Enter New Amount : "))
        # description=input("Enter New Description : ")
        # date=input("Enter New Date (YYYY-MM-DD): ")
        with sqlite3.connect('finance_manager.db',check_same_thread=False) as conn:
            c=conn.cursor()
            c.execute("SELECT * FROM expenses WHERE id = ? and user_id=?", (id, user_id))
            if c.fetchone():
                c.execute("UPDATE expenses SET amount = ?, description = ?, date = ? WHERE id = ? and user_id=?",
                    (amount, description, date, id ,user_id))
                conn.commit()
                msg=f"{transaction_type.capitalize()} update successfully!"
                return msg
            else:
                msg=f"Error: Expense ID {id} not found for user {username}."
                print(msg)
                return msg
        conn.close()

    else:
        print("Enter Valid Input")
        conn.close()
    
# edit_transaction('income','sikander',1,100,'hello',11)
def delete_transaction(username,id,t_type):
    user_id=get_user_id(username)
    table_name = t_type
    # table_name = input("Enter You Want To Delete (income/expenses): ")
    if table_name=="income":
        income_id=id
        conn = sqlite3.connect('finance_manager.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM income WHERE id = ? and user_id=?", (income_id, user_id))
        if cursor.fetchone():  # Check if the record exists
            cursor.execute("DELETE FROM income WHERE id = ? and user_id=?", (income_id, user_id))
            conn.commit()
            msg=f"{table_name.capitalize()} delete successfully!"
            return msg
        else:
            error=f"Error: Income ID {income_id} not found for user {username}."
            return error
        conn.close()

    elif table_name=="expense":
        expense_id=id
        conn = sqlite3.connect('finance_manager.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        if cursor.fetchone():  # Check if the record exists
            cursor.execute("DELETE FROM expenses WHERE id = ? and user_id=?", (expense_id,user_id))
            conn.commit()
            msg="{table_name.capitalize()} delete successfully!"
            return msg
        else:
            error=f"Error: Expense ID {expense_id} not found."
            return error
        
    else:
        print("Enter Valid Input")
    conn.close()
    
# add_transaction()

# delete_transaction('sikander')

def show_transaction(t_type,username):
    conn=sqlite3.connect("finance_manager.db")
    c=conn.cursor()
    data=t_type
    # data=input("What Do You Want To See (income/expense) :")
    if data=="income":
        user_id=get_user_id(username)
        c.execute('SELECT * FROM income where user_id = ?',(user_id,))
        rows = c.fetchall()
        tran_list=[]

        if rows:  # Check if there are any rows returned
            for row in rows:
                # print(row)
                tran_list.append(row)
                # print(tran_list)
                # print(row)
            return tran_list
        else:
            error="No data found."
            tran_list.append(error)
            return tran_list
    elif data=="expense":
        c.execute('SELECT * FROM expenses')
        rows = c.fetchall()
        tran_list=[]
        if rows:  # Check if there are any rows returned
            for row in rows:
                # print(row)
                tran_list.append(row)
            return tran_list
        else:
            error="No data found."
            tran_list.append(error)
            return tran_list
    else:
        error="Enter Valid Input"
        tran_list.append(error)
        return tran_list
    conn.close()

conn.close()
# tran=show_transaction('expense','shri')
# print(tran)
