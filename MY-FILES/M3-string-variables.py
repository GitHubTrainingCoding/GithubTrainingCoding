# INITIALIZE USER VARIABLES FIRST: Declare a value for them before they're [input]

# x = input("How much did you invest? ")
# print(x)
# ``this will get input from the user and save it in the variable [x], and print to screen``

# y = "Bitcoin"
#``this will declare the value of the variable [y]``

#rules: no spaces, case sensitive, cannot start with a number, stick to one convention

# print("Hello " + firstName + " " + lastName) 
#`` this prints a string, then a variable, then a space, then a variable

# message = 'Hello world' 
# print(message.lower()) 
# print(message.upper()) 
# print(message.swapcase())
# print(name.capitalize())
#`` STRING FUNCTIONS to modify case of user's input to variable [message]

#challenge: write a program that allows a user to modify a story.

print("\n\n\nLet's read a story together!")
print("\nTHE LAZY TEACHER \n------------------------")
print("\nThere was once a lazy teacher called Guitar. \nFor his class warm-ups he sang songs to the students . \nHe only knew three songs however; Wheels On The Bus, Baby Shark, and If That Ain't Country. \nAfter eight weeks of rotating through these same three songs, not only were the students bored, \nbut his co-workers were extremely irritated!")
print("\nLet's change some elements of that story shall we? \n")

t = "Guitar"
t = input("Give me a new name for the teacher...")
print("\nOK, so we're changing the teacher's name to be " + t.capitalize + ".")

s = "If That Ain't Country"
s = input("\nGive me a new name for the third song...")
print("\nOK, so we're changing third song to be " + s + ".")

e = "irritated"
e = input("\nChoose an alternative emotion that " + t.capitalize + "'s co-workers will feel...")
print("\nOK, so we're changing the co-workers' emotion to be " + e + ".\n")

x = input("Hit ENTER to see your version of the story...\n")

print("\nTHE LAZY TEACHER \n------------------------")
print("\nThere was once a lazy teacher called " + t.capitalize + ". \nFor his class warm-ups he sang songs to the students . \nHe only knew three songs however; Wheels On The Bus, Baby Shark, and " + s  + ". \nAfter eight weeks of rotating through these same three songs, not only were the students bored, \nbut his co-workers were extremely " + e + "!")



















print("")