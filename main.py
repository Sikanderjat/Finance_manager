from finance_manager.database.db_setup import create_user_table,create_expenses_table,create_income_table
create_user_table()
create_expenses_table()
create_income_table()

from finance_manager.authentication.register import register_user,login_user ,logout
from finance_manager.reports import transaction
from finance_manager.reports.final_report import generate_final_report

while(True):
    user_input=input("Login OR Registor To Access More Features(Login/Registor):")
    # username="sikander"
    # password="123"
    username=input("Enter Your User Name :")
    password=input("Enter Your Password :")
    if user_input.lower() == "login":
        while(True):
            if login_user(username,password):
                after_login=input("What Do You Want \n(Add_Transition--1\nEdit_transition--2\nDelete_transition--3\nShow_Transition--4 \nGet Final Report--5\nExit--6\nLogout--7):")
                match after_login:
                    case "1":
                        transaction.add_transaction(username)

                    case "2":
                        transaction.edit_transaction()

                    case "3":
                        transaction.delete_transaction()

                    case "4":
                        transaction.show_transaction(username)

                    case "5":
                        report=generate_final_report(username)
                        print(report)

                    case "6":
                        exit()

                    case "7":
                        logout()
                        break
                    case _:
                        print("All Transition Commit Successfully")
            
            
            else:
                break

    elif user_input.lower() == "registor":
        register_user(username,password)
    
    else:
        print("Enter a Valid Input")





# user_name=input("Enter Username :")
# password=input("Enter Password :")
# register_user(user_name,password)
# login_user(user_name,password)
# logout()

# transaction.add_transaction()
# transaction.edit_transaction()
# transaction.delete_transaction()
# transaction.show_data()