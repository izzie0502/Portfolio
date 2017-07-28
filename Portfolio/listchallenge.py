
from random import *


#Create the list of words you want to choose from.
first = ["I like to eat food", "Frogs do not suffer"]
second = ["It\'s always sunny in Boston", "I don\'t know what I\'m doing"]


#Generates a random integer.
x = randint(0, len(first)-1)
y = randint(0, len(second)-1)
z = randint(0, len(first)-1)

haiku = ""
haiku += first[x] + "\n" + second[y] + "\n" + first[z]
print ("You\'re haiku is...\n" + haiku)
