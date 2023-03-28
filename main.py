import random
import string


def pwgen(length, with_digits=True, with_uppercase=True):
    lowercase = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    uppercase = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = string.digits
    ##########################################################################################################"
    choices = lowercase
    if with_digits:
        choices += digits
    #################################################################################################
    if with_uppercase:
        choices += uppercase

    password = random.choices(choices, k=length)
    #################################################################################################
    if with_digits and with_uppercase:
        password[0] = random.choice(lowercase)
        password[1] = random.choice(digits)
        password[2] = random.choice(uppercase)
    #################################################################################################
    elif with_digits:
        password[0] = random.choice(lowercase)
        password[1] = random.choice(digits)
    ################################################################################################
    elif with_uppercase:
        password[0] = random.choice(lowercase)
        password[1] = random.choice(uppercase)
    return ''.join(password)