import string
import random

## characters to have in a password
## letters include both lowercase and uppercase letter
alphabet = list(string.ascii_letters)
specialCharacters = list("!@#$%^&*()")
digits = list(string.digits)

characters = list(string.ascii_letters + "!@#$%^&*()" + string.digits )

def password_random_generator():
    ##the user need to input the length of the password
    length = int(input("Please type the password length: "))

    alphabetLetters_count = int(input(" Type how many alphabet letter you want in the password: "))
    specialCharacters_count = int(input(" Type how many specialCharacters you want in the password: "))
    digits_count = int(input(" Type how many digits you want in the password: "))

    characters_count = alphabetLetters_count + specialCharacters_count + digits_count

    if characters_count > length:
        print("The total characters count is greater than the password length, please try again :) ")
        return
    
    




    password = []

    ##pick random alphabet letters
    for i in range(alphabetLetters_count):
        password.append(random.choice(alphabet))


    ##pick random special characters
    for i in range(specialCharacters_count):
        password.append(random.choice(specialCharacters))

    ##pick random digits
    for i in range(digits_count):
        password.append(random.choice(digits))


    ##now we are going to shuffle the password
    random.shuffle(password)


    #to return the password we need to convert it into a string using "".join()

    print("".join(password))


##calling the function password generator
password_random_generator() 
    
                        

    
