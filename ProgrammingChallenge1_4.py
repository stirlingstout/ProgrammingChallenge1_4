##########################
#  AQA User Registration #
##########################

def DisplayMenu():
    print("")
    print("######################################")
    print("Please enter a menu choice")
    print("Enter 1 to login with username and password")
    print("Enter 2 to register a new username and password")
    print("Enter 3 to quit the program")
    print("######################################")
    
def UserDetails():
    # define a list and open file called usernames.txt
    # read the text file and add it to the list
    # repeat for passwords file. Each username and password
    # combination is on the same line in each file.
    
    myFile = open("usernames.txt", "r")
    userNames = myFile.read().splitlines()
    myFile.close()
        
    myFile = open("passwords.txt", "r")
    passwords = myFile.read().splitlines()
    myFile.close()
    
    # A list is created with usernames in lower case
    # for validation that is not case sensitive
    userNamesLower = [un.lower() for un in userNames]

    return (userNames, passwords, userNamesLower)

def RegisterNew(userNamesLower):
    tries = 0 # only 3 tries are allowed
    validUserName = False # flag set if username is valid

    # loop up to 3 times for a new username
    while (tries < 3) and (not validUserName):
        userName = input("Please enter a new username: ")
        if userName.lower() in userNamesLower:
            print("The username is already used")
            tries += 1
        else:
            validUserName = True

    if validUserName:
        tries = 0
        validPassword = False
        while (tries < 3) and (not validPassword):
            userPassword = input("Please enter a password,   12 characters or more: ")
            if len(userPassword) < 12:
                print("The password is not long enough")
                tries += 1
            else:
                print("Your username is " + userName)
                print("Your password is " + userPassword)
                validPassword = True
    
                # add the new username to the text file
                userNames.append(userName)
                myFile = open("usernames.txt", "a")
                myFile.write(userName + '\n')
                myFile.close()
                
                myFile = open("passwords.txt", "a")
                myFile.write(userPassword + '\n')
                myFile.close()
    # error message if the user has failed validation
    if tries == 3:
        print("Only three tries are allowed")
    else:
        print("Thank you for registering.")
            
def Login(un, pw, userNamesLower, passwords):
    # checks username is found and the password matches
    if un.lower() in userNamesLower:
        i = userNamesLower.index(un.lower())
        if pw == passwords[i]:
            return True
        else:
            return False
    else:
        return False
        
#####################        
# Main program
#####################

userNames, passwords, userNamesLower = UserDetails()
print("Welcome to AQA User Registration")

#loop that allows a menu number to be entered
userInput = ''
while userInput != "3":
    DisplayMenu()    
    userInput = input("Menu choice: ")

    if userInput == "1":
        un = input("Please enter your username: ")
        pw = input("Please enter your password: ")
        print("")
        loginOK = Login(un, pw, userNamesLower, passwords)
        if loginOK:
            print("Login successful")
        else:
            print("Login incorrect: register or retry")
    elif userInput == "2":
        RegisterNew(userNamesLower)
    elif userInput == "3":
        print("Goodbye")
    else:
        print("ERROR! you must enter 1, 2 or 3")

# end of program

