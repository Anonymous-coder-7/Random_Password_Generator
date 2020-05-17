import string
import random

def generate_password(Password_Length):
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    special_characters = string.punctuation
    digit = string.digits
    password_set = []
    password_set.extend(list(small_letters))
    password_set.extend(list(capital_letters))
    password_set.extend(list(special_characters))
    password_set.extend(list(digit))
    random.shuffle(password_set)
    return "".join(password_set[0:Password_Length])

if __name__=="__main__":
    print("ENTER THE LENGTH OF YOUR PASSWORD ")
    Password_Length=int(input())
    print("Wait ! Your Password Is Being Generated ")
    print()
    print("Your Password Is :- ",generate_password(Password_Length))
