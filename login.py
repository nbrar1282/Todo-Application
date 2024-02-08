# function to check login credentials
def check_login(username, password):
    while True:
        user = input("What is the username? ")
        pw = input("What is your password? ")
        
            
        if user == username and pw == password:
                break
        else:
             print("Sorry wrong credentials")
            
    