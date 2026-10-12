import re 
import pandas as pd

def main():
    welcome = print(f"Welcome to our Pharmacy <3\nPlease log-in or sign-up to get the insurance or discounts that you need.")

    while True:
        prompt = input("Would you like to log-in or sign-up? ")
        if prompt.replace(" ","").replace("-","").lower() == "signup":
            while True:
                user_login = ...
                pass_login = ...
                user_signup = input(f"Enter a username: ")
                if not users(user_signup) == user_signup:
                    continue
                else:
                    while True:
                        pass_signup = input(f"Enter a password: ")
                        if not passes(pass_signup) == pass_signup:
                            continue    
                        else:
                            print(f"Congrats! Your account has been made.")
                            account(user_login, pass_login, user_signup, pass_signup)
                            medication()
                        break
                    break
            break
        elif prompt.replace(" ","").replace("-","").lower() == "login":
            while True:
                user_login = input(f"Enter a username: ")
                pass_login = input(f"Enter a password: ")
                user_signup = ...
                pass_signup = ...
                if account(user_signup, pass_signup, user_login, pass_login) == False:
                    print(f"Unknown username or password, please try again.")
                    continue
                else:
                    print(f"Congrats! You are now logged in.")
                    medication()
                break
            break
        else:
            print(f"There may be a typo, please try again!")
            continue
    
def users(a):
    if len(a) <= 3 or len(a) >= 12:
        # checks length of the username 
        return print(f"Username must be more than 3 and less than 12 characters.")
    elif not a.isalnum() or a.isspace():
        # checks if there are special characters 
        return print(f"Username can only contain letters and numbers.")
    else:
        return a

def passes(b):
    reg = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[ !"#$%&*+,-./:;<=>?@[\]^_`{|}~])[A-Za-z\d !"#$%&*+,-./:;<=>?@[\]^_`{|}~]{6,20}$'
    # reg contains the rules for the password, ^ is starts with and $ is ends with
    # ? is zero or more occurances of, = is matches, . is any character, * is one or more occurances of, and anything in the [] is what we want the password to have
    # so the parts above are simply checking if there is at least one lowercase, uppercase, digit and special character 
    # the part with just the [] is saying that the password can be made up of whatever is inside, and the {} limits the password between 6 and 20 characters. 
    pat = re.compile(reg)
    # compiling it allows us to re-use the rules
    mat = re.search(pat, b)
    # re.search basically matches the pattern to the password 
    if not mat:
        return print(f"Password must be between 6 and 20 characters, have 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character.")
    else: 
        return b
        # returning it in this format allows us to store the data in the user database

def account(user_signup, pass_signup, user_login, pass_login):
    user_db = {"raisa":"ABCefg2$"
               }
    sign = {user_signup:pass_signup}
    user_db.update(sign)
    # adds the newly formed account to the user database 

    if not user_login in user_db.keys() or not pass_login in user_db.values():
        # checks to see if username or password are present in the user database
        return False
    else:
        print(f"You are now logged in.")
        return {user_login: pass_login}
    
def medication():
    popular = pd.read_excel("popular_pricelist.xlsx").drop(columns=["#SL","Pack Size","Dosage Description","Use For","DAR"])
    radiant = pd.read_excel("radiant_pricelist.xlsx").drop(columns=["#SL","Pack Size","Dosage Description","Use For","DAR"])
    square = pd.read_excel("square_pricelist.xlsx").drop(columns=["#SL","Pack Size","Dosage Description","Use For","DAR"])
    df = pd.concat([popular, radiant, square])
    # merged the excel files to make it easier


    # entry = input(f"What is the name of the medication that you need? ")
    # generic = df[df['Generic Name'] == 'Paracetamol']
    # dose = generic[generic['Strength'] == '1 mg']
    # print (generic.empty)
    # print(dose.min(axis=0))

    # brand = df[df['Brand Name'] == 'Ace']
    # type = brand.reset_index(drop=True).at[0, 'Generic Name']
    # gen = df[df['Generic Name'] == type]
    # dose = gen[gen['Strength'] == '500 mg']
    # print(dose.min(axis=0))
    
    print(f"\nPlease enter the name and dosage of the medication you need. ")


    while True:
        name = input(f"Name of Medication: ")
        generic = df[df['Generic Name'] == name]
        brand = df[df['Brand Name'] == name]
        # changes the dataframe to only contain the entry, if paracetamol/ace was entered then now the dataframe only contains the data for paracetamol/ace
        if generic.empty == True and brand.empty == True:
            print(f"There may be a typo, or this medication is currently not in store, please try again.")
            continue
        elif generic.empty == False and brand.empty == True:
            while True:
                generic_dosage = input(f"Required Dosage of Medication: ")
                generic_dose = generic[generic['Strength'] == generic_dosage]
                if generic_dose.empty == True:
                    print(f"There may be a typo, or this dosage is currently not in store, please try again.")
                    continue
                else:
                    print(f"\nHere is your medication, at the lowest price possible! Thank you for your patronage.")
                    lowest_price = generic_dose.min(axis=0)
                    print(lowest_price.to_string())
                    return lowest_price.to_string()
            break
        elif generic.empty == True and brand.empty == False:
            type = brand.reset_index(drop=True).at[0, 'Generic Name']
            # resetting index in order to have the rows start from 0, at gets the value for the generic name from the first row, since the value will be the same for all the rows 
            gen = df[df['Generic Name'] == type]
            while True:
                brand_dosage = input(f"Dosage: ")
                brand_dose = gen[gen['Strength'] == brand_dosage]
                if brand_dose.empty == True:
                    print(f"There may be a typo, or this dosage is currently not in store, please try again.")
                    continue
                else:
                    print(f"\nHere is your medication, at the lowest price possible! Thank you for your patronage.\n")
                    lowest_price = brand_dose.min(axis=0)
                    print(lowest_price.to_string())
                    return lowest_price.to_string()
            break



if __name__ == "__main__":
    main()