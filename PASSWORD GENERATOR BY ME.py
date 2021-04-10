# Generator Project
import random
#thiPasswords are the list of letter, number and string for generating the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#this is the welcome statement from the computer
print("Welcome to the PyPassword Generator!")

#this help to collect input from the user
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# this line of code help us to get a "letter" at random
#whereby nr... is the number of it the user insert in the input
randomLetter = random.sample(letters, nr_letters)
#this help to concatenate items in a list to a single string
alphabet = ""
for i in randomLetter:
    alphabet += str(i)


#this line of code help us to get a "number" at random
#whereby nr... is the number of it the user insert in the input
randomNumber = random.sample(numbers, nr_symbols)
#this help to concatenate items in a list to a single string
number = ""
for i in randomNumber:
    number += str(i)

#this line of code help us to get a "symbol" at random
#whereby nr... is the number of it the user insert in the input
randomSymbols = random.sample(symbols, nr_numbers)
#this help to concatenate items in a list to a single string
symbols = ""
for i in randomSymbols:
    symbols += str(i)
    

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easyPassword = alphabet + number + symbols

print (f"The Easy code is {easyPassword}")



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#this code will help to reshuffle the above easyPassword
hardPassword = ''.join(random.sample(easyPassword,len(easyPassword))) 

print(f"The Hard code is {hardPassword}")



# NOTE
#in using the sample () funtion
#it comes in this format random.smaple(population, k)
# where population index must be equal to a number of item in k
#else will result in an error
# so in the above code population of 52 must correspond to the input value which is K (in range of 0 -52)

