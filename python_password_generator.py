##python program to create a random password generator that can generate a random password of 8(eight correctors)
##including the uppercase, lowercase, digits and  punctuation symbols
import random
import string
## a function used to shuffle all the characters of the string
def shuffle(string):
    templist= list(string)
    random.shuffle(templist)
    return "".join(templist)

##  the main program start here :
uppercase1 = chr(random.randint(65,90))## first uppercase number .
uppercase2 = chr(random.randint(60,90))## second upper case number.
lowercase1 = chr(random.randint(97,122))## firts random lowercase alphabet.
lowercase2 = chr(random.randint(97, 122))
digit1 = random.randint(0 ,9)### generting a random  digit
digit2 = random.randint(0, 9)## genearing a random digit
punctuation1 = random.choice(string.punctuation)
punctuation2 = random.choice(string.punctuation)
password = uppercase1 +uppercase2 + lowercase1+ lowercase2 + str(digit1) +str(digit2) + punctuation1 + punctuation2
shuffle(password)
print(password)