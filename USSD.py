import sqlite3

# Connect to the database
conn = sqlite3.connect('USSD.db')
cursor = conn.cursor()

# Authenticate user
name = input("Enter username: ")
ID = input("Enter password: ")

cursor.execute('''SELECT * FROM users WHERE name = ? AND ID = ?''', (name, ID))
user = cursor.fetchone()

if user:
    print("Authentication successful!")
else:
    print("Authentication failed. Invalid username or password.")






#All other options squeezed here as the purpose of the assignment does not highlight their use
def Report_Fraud():
    print("Report Fraud")
def My_Approvals():
    print("My Approvals")
def Check_Balance():
    print("Check Balance")    
def Momopay_and_Paybill():
    print("Momopay and Paybill")
def Airtime_Bundles():
    print("Airtime and Bundles")
def Statements():
    print("Statement")
def Change_and_Reset_Pin():
    print("Change and reset pin")


# Function to display menu in my wallet
def Allow_Cash_Out():
    Initial_Balance = 1,000
    print("Allow Cahout")
    print("1) Yes")
    print("2) No")
    Yes_or_No = input("Choose option: ")
    if Yes_or_No == "1":
        print("Cash out is allowed\n")
        withdraw = int(input("Enter amount to withdraw: "))
        Current_Balance = 1,000 - withdraw
        print("Cash Out made for GHS "+ str(withdraw)+ " to Momo Enterprise.")
        print("Current Balance: GHS "+ str(1000-withdraw)+ " Transaction id: 001100234.")
    else:
            return Allow_Cash_Out()

   

def Financial_Services():
    print("Financial Services")


# Function to display menu in my wallet
def My_Wallet():
    print("1) Check Balance")
    print("2) Allow Cash Out")
    print("3) My Approvals ")
    print("4) Report Fraud")
    print("5) Statements")
    print("6) Change & Reset PIN")
    print("7) Upgrade Pofile Type")
# Options to choose from 1 - 7 to display menu of selected item in my wallet
    choose_Option = input("Choose option: ")
    if choose_Option == "1":
        return Check_Balance()
    elif choose_Option == "2":
        return Allow_Cash_Out()
    elif choose_Option == "3":
        return My_Approvals()
    elif choose_Option == "4":
        return Report_Fraud()
    elif choose_Option == "5":
        return Statements()
    elif choose_Option == "6":
        return Change_and_Reset_Pin()
    else:
        return My_Wallet()
    




#Function to enter amount to transfer
def amount():
    enter_amount = input("Enter amount to transfer: ")
    print("You have successfully sent " + enter_amount)


# Function to take recipient's number
def momo_user():
    mobile_number = input("Enter mobile number: ")
    if mobile_number == "0249143054":
        return amount()
    else:
        print("Invalid number try again\n")
        return momo_user()
    
    

# Function to display main menu of the USSD
def menu():
    print("1) Transfer Money")
    print("2) Momopay and Paybill")
    print("3) Airtime & Bundles")
    print("4) Allow Cash Out")
    print("5) Financial Services")
    print("6) My wallet")
 # Options to choose from 1 - 6 to display menu of selected item menu()
    choose_option = input("Choose option: ")
    if choose_option == "1":
        return Transfer_Money()
    elif choose_option == "2":
        return Momopay_and_Paybill()
    elif choose_option == "3":
        return Airtime_Bundles()
    elif choose_option == "4":
        return Allow_Cash_Out()
    elif choose_option == "5":
        return Financial_Services()
    elif choose_option == "6":
        return My_Wallet()
    else:
        return menu()
    


#Function to transfer money menu
def Transfer_Money():
    print("1) Momo User")
    print("2) Non Momo User")
    print("3) Send with Care")
    print("4) Favorite")
    print("5) Other Networks")
    print("6) Bank Account")
# Options to choose from 1 - 6 to display menu of selected item Transfer_Money()
    Choose_option = input("Choose option: ")
    if Choose_option == "1":
        return momo_user()
    elif Choose_option == "2":
        return Non_momo_user()
    elif Choose_option == "3":
        return Send_with_Care()
    elif Choose_option == "4":
        return Favorite()
    elif Choose_option == "5":
        return Other_Networks()
    elif Choose_option =="6":
        return Bank_Account()
    else:
        return Transfer_Money()

    

    
    
#Function to take the short code input to kickstart USSD process
def main():
    print("Welcome to MTN USSD")
    short_code = "*170#"
    user_input = input("Enter short code: ")
    if user_input == short_code:
        return menu()
    else:
        print("Invalid Input, try again")
        return main()
    
main()



  # Close the connection
conn.close()
