'''this is code to find out whether or not you can vote in nz 
by daniel at some point'''


is_resident = False
#ask the user for their name
name = input('What is your name?\n')
#ask the user their age
age = input("What is your age?\n")
#asks their age and check if age is a number
while not age.isnumeric():
    print('Thats not a number.')
    age = input("What is your age?\n")
age = int(age)


#ask if they are a resident
while True:
    residency = input('are you a resident of NZ? Y/N\n')
    if residency.lower() == "y":
        is_resident = True
        break
    elif residency.lower() == "n":
        is_resident = False
        break
    else:
        print('Please type in Y or N.\n')
#decide if the user can vote based on inputs
if age > 17 and is_resident == True:
    print('You can vote!')
else:
    print("You can't vote")

