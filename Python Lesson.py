

print("hello world") 
x = 3.6362362387628763
print(round(x, 3))


"""Hello there
bruh
why dude
long comment"""

number = 5
print("its hot" if number > 4 else "it's cold")

result = "Even" if number % 2 == 0 else "Odd"
print(result)

print("len() function gives number of characters")
question = "How are you"
print(len(question))

print("find gives length of charcters to that character. rfind gives that but moving backwards (reverse find)")
print(question.find("a"))
print(question.rfind("a"))

print(question.upper)

print(question.isdigit)
print(question.isalpha)

print(question.replace(" ", ""))
print(question.replace(" ", "-"))

ccn = "783458376837"
print(ccn[0]) #first char
print(ccn[0:5]) #First 5 char
print(ccn[-1]) #first char from right
print(ccn[::2]) # count every 2nd char

print("look up format specifiers")


def multiply(number1, number2):
    return number1 + number2
ans_for_6_and_8 = multiply(6,8)
print(ans_for_6_and_8)

animal = "cow"
item = "moon"
print("The {} jumped over the {}".format(animal,item)) #The cow jumped over the moon


randomnumbers = 72368723642873
print("Randomnumbers with commas: {:,}".format(randomnumbers))
print("Randomnumbers in scientific: {:e}".format(randomnumbers))


import random

ran_bet_1_and_6 = random.randint(1,6)
print(ran_bet_1_and_6)

RPS_list = ["rock","paper","scissors"]
RPS_random = random.choice(RPS_list) #can also use random.shuffle(RPS_list) to list these in a random way
print(RPS_random)


try:
    numerator = int(input("Enter a numerator"))
    denominator = int(input("Enter a denominator"))
    resultssss = numerator/denominator
except ZeroDivisionError:
    print("You cannot divide by zero, idiot")
except ValueError:
    print("Enter only numbers, please")
except Exception:
    print("Something went wrong :(")
else:
    print(resultssss)
finally:
    print("This will always execute")


import os
path = "C:\\Users\\keith\\Desktop\\Random\\Projects\\Python Projects\\text.txt"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")
    

with open("C:\\Users\\keith\\Desktop\\Random\\Projects\\Python Projects\\text.txt") as the_text:
    print(the_text.read())
print(the_text.closed) #Check if it is closed (will answer with True or False)


randomtexts = "Hello there bruh"
with open("C:\\Users\\keith\\Desktop\\Random\\Projects\\Python Projects\\text.txt", "w") as the_text2:
    the_text2.write(randomtexts)

randomtexts = "Hello there bruh"
with open("C:\\Users\\keith\\Desktop\\Random\\Projects\\Python Projects\\text.txt", "a") as the_text2: #"a" will append
    the_text2.write(randomtexts)
    
import shutil
shutil.copyfile("text.txt", "copy.txt") #src, dst --- Copies a file


filepath = "copy.txt"

try:
    os.remove(filepath)
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You don not have permission to delete that")
else:
    print(path+" was deleted")
    
#os.remove(path)  #delete a file
#os.rmdir(path)   #delete an empty directory 
#shutil.rmtree(path)   #delete a directory containing a filem