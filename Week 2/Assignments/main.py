# start by importing the necessary documents

import random
import string 


def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria
    Input: pwd -> character or string
    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here

    STRONG = "STRONG"
    MODERATE= "MODERATE"
    POOR = "POOR"

    symbols = ("!", "+", "-", "=", "?", "#", "%", "*", "@", "&", "^", "$", "'")
    rank=""

    length = ""

    if len(pwd) > 10 :
        length = "S"
    elif len(pwd) > 8 and len(pwd) <= 10:
        length = "M"
    else:
        length ="P"

    contains_number = [character.isdigit() for character in pwd]
    contains_symbol = [character in symbols for character in pwd]
    lower_case = [string.ascii_lowercase.__contains__(character) for character in pwd]
    upper_case = [string.ascii_uppercase.__contains__(character) for character in pwd]  

    # pwd has -> lowecase, uppercase, number, symbol
    if any(lower_case) and any(upper_case) and any(contains_number) and any(contains_symbol):
        if length == "S":
            rank = STRONG
        elif length == "M":
            rank = MODERATE
        else:
            rank = POOR
    
    # pwd has -> (lowecase only), or (uppercase only ), or (number only), or (symbol only)
    if all(lower_case) or all(upper_case) or all(contains_number) or all(contains_symbol):
        rank = POOR

    # pwd has -> (lowercase, uppercase, number) or (lowercase, uppercase, symbol)
    elif any(lower_case) and any(upper_case):
        if any(contains_number) or any(contains_symbol):
            if length == "P":
                rank = POOR
            else:
                rank = MODERATE
        else:
            rank = POOR
    
    # pwd has -> (lowercase, number, uppercase) or (lowercase,number,symbol)
    elif any(lower_case) and any(contains_number):
        if any(upper_case) or any(contains_symbol):
            if length == "P":
                rank = POOR
            else:
                rank = MODERATE
        else:
            rank = POOR
    
    # pwd has -> (lowecase,symbol,uppercase) or (lowercase,symbol,number)
    elif any(lower_case) and any(contains_symbol):
        if any(upper_case) or any(contains_number):
            if length == "P":
                rank = POOR
            else:
                rank = MODERATE
        else:
            rank = POOR
    
    # pwd has -> (uppercase,number,lowercase) or (uppercase,number,symbol)
    elif any(upper_case) and any(contains_number):
        if any(lower_case) or any(contains_symbol):
            if length == "P":
                rank = POOR
            else:
                rank = MODERATE
        else:
            rank = POOR
    
    # pwd has -> (uppercase,symbol,lowercase) or (uppercase,symbol,number)
    elif any(upper_case) and any(contains_symbol):
        if any(lower_case) or any(contains_number):
            if length == "P":
                rank = POOR
            else:
                rank = MODERATE
        else:
            rank = POOR
    
    # pwd has -> (number,symbol,lowercase) or (number,symbol,uppercase)
    elif any(contains_number) and any(contains_symbol):
        if any(lower_case) or any(upper_case):
            if length == "P":
                rank = POOR
            else:
                rank = MODERATE
        else:
            rank = POOR

    ## End code here
    return rank

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Hint: See the steps above and formulate them in code.
    ## START CODE HERE
    filePath = input("Enter the path to your file: ")
    user_info=[]
    try:
        usrpwds = open(filePath,"r").readlines()
        with open('Users-Pwds-Chked.txt','w') as file:
            for items in usrpwds:
                user_info = items.split(',')

                user_name = user_info[0].strip()
                user_password = user_info[1].strip()

                # rank password
                rank_password = rank(user_password)

                file.write(','.join((user_name,user_password,rank_password)))
                file.write('\n')
            
    except Exception as e:
        print('Could not complete action ', str(e))
        return False
    print(f"Number of passwords checked:{len(usrpwds)}")
    print(f"The given rankings can be found in Users-Pwds-Chked.txt")
    
    ## END CODE HERE

    
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    # print('[INFO] '+'Number of passwords checked:',str(len(usrpwds))) 
    # print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)


def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    '''

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = []
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE

        characterList = Ualphabets+Lalphabets+chars+digits
        for _ in range(11):

            # choose random character from characterList
            pwd.append(random.choice(characterList))
        
        ## END CODE HERE

        return "".join(pwd)
    
    # Ask for username and check 20 character limits

    ## START CODE HERE
    user_name = input("Enter your name:")
    if len(user_name)>20:
        print("The username is greater than 20 characters. Please enter it again")
        option2()


    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header. 

    ## START CODE HERE

    while True:
        user_password = generate()
        print(f'Here is the auto generated password: {user_password}.')

        user_confirmation = input('Do you want to save it: y/n')

        if user_confirmation.lower() == "y":

            # open User-Pwd.txt file
            file = open("User-Pwd.txt","w")

            file.write(",".join((user_name.strip(),user_password)))
            break

        elif user_confirmation.lower() == "n":
            pass
        


    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = int(input("Enter your option here:"))
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE
        if inp== 1 :
            option1()
        elif inp == 2:
            option2()
        elif inp == 3:
            print("This program is courtesy of: Anurupa ")
            break
        else:
            print("Please enter the right option")
        print('-'*40)

        

        ## END CODE HERE

if __name__=='__main__':
    main()