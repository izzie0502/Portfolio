

global key
key = 0
end = 0


print(" ERROR \n ERROR \n ERROR \n ERROR \n ERROR \n ERROR \n ERROR \n ERROR \n")
print("Hello?!\nIs anyone there?!\n")

awake = input()
if awake == "yes" or (awake == "yeah") or (awake == "y") or (awake == "ok") or (awake == "sure"):
    print("\nFinally!\nWhat's your name?\n")
else:
    print("\n...Well, I know you're there because I know you can type.\nWhat's your name?\n")

name = input()
print("\nOkay, " + name + ". I assume you're confused right now.\nBut hear me out.\nA potential murder, or at least a kidnapping of some sort, has occured in the room you are standing in right now.\n")
print("The victim of this situation is one of my agents, Agent IZ.\nHe was on a...dangerous mission, the contents of which I cannot disclose just yet.")
print(name + ", we need your help.\nLook around the room. See if you can find a trace of Agent IZ.\n")
print("[Try typing clear, concise action terms in lowercase to find out where you are. Start with 'look around']\n")



def ENDING1():
    print("\n[You see a reflection of your face on a puddle in the street. you have a large tattoo on your neck of a tiger!]\nPlease type ctrl+C before you leave so that the game ends...")

def ENDING2():
    print("\n[You open the chest. Strangely enough, it contains only a single mirror.\nYou bring the mirror up to your face and drop it almost immediately.\nThere is a tattoo of a tiger running down your neck.]")
    print("\nPlease type ctrl+C before you leave so that the game ends...")


start = input()
while start != "look around":
    print("[Why don't you try typing 'look around'?]\n")
    start = input()


def jacket():
    print("\n[You look at the jacket. There is a photograph in the pocket of a woman with a tattoo of a tiger on her neck. \nOn the back of the photo, it is scribbled in pen: 'Always keep your head up.']\n")
    jacket1 = input()
    print("\n[There's not much more you can do here.\nYou go back to the center of the room, where you began.]\n")

def music():
    print("\n[You pick up the music box. The wind up key is inserted, but you can't seem to make it play.\nIt seems to be locked, requiring a four digit code to open.\nYou try typing in a code.]\n")
    music1 = input()
    if music1 == "book" or music1 == "The code is book" or music1 == "BOOK":
        print("\n[It worked! Beautiful music starts to play, and a small rusted key falls out of the box.\nMaybe this will open something...\n")
        print("Holding the key tightly in your palm, you return to the center of the room.]")
        decide = input()
        if decide == "open door" or decide == "leave" or decide == "unlock door" or decide == "go to door":
            ENDING1()
        elif decide == "open chest" or decide == "unlock chest" or decide == "open wooden chest" or decide == "unlock wooden chest" or decide == "check chest" or decide == "check wooden chest":
            ENDING2()
        else:
            print("\n[You don't need to do that right now. You have a key.\nTry unlocking something with it.]\n")
    else:
        print("\n[The code did not work. Maybe you should look around more.\nYou return to the center of the room, where you began.]\n")
        return 0


def romance():
    print("\n[There are four romance novels, in order: 'Beneath the Horizon', 'Over the Moon', 'On His Radar', and 'Kissing in the Rain'.\nHowever, you have no time to be sitting around and reading right now.\nYou go back to the center of the room, where you began.]\n")
    roman1 = input()

def left_Books():
    print("\n[You go left to look at the bookshelf. On the top shelf, there is a series of dusty romance novels.\nThe rest of the shelves are empty.]\n")
    left1 = input()
    if left1 == "look at books" or left1 == "look at romance novels" or left1 == "look at top shelf" or left1 == "read books" or left1 == "read romance novels" or left1 == "look at novels" or left1 == "check books":
        romance()
    else:
        print("\n[There's not much more you can do here.\nYou go back to the center of the room, where you began.]\n")


def right_Bed():
    print("\n[You go right to look at the bed. On the mattress, there is a jacket.\nThere seems to be something in its pocket. There is also a small music box at the foot of the bed.]\n")
    right1 = input()
    if right1 == "look at mattress" or right1 == "look at jacket" or right1 == "look at pocket" or right1 == "check jacket" or right1 == "check pocket":
        jacket()
    elif right1 == "check music box" or right1 == "look at music box" or right1 == "go to music box" or right1 == "pick up music box" or right1 == "take music box" or right1 == "use music box":
        music()


while (key < 1):
    print("\n[Before you, there is a computer screen. To your left there is an old mahogany bookshelf, and to your right there is a queen sized bed. Behind you there is a door, and a sturdy wooden chest.]\n")
    go1 = input()
    if (go1 == "look left") or (go1 == "go left") or (go1 == "go to bookshelf") or (go1 == "go to bookcase") or (go1 == "look at bookshelf") or (go1 == "look at bookcase") or (go1 == "look at books") or go1 == "check bookshelf":
        left_Books()
    elif go1 == "go right" or go1 == "go to bed" or go1 == "look right" or go1 == "look at bed" or go1 == "check right" or go1 == "check bed":
        right_Bed()
    elif go1 == "open door" or go1 == "leave" or go1 == "open chest" or go1 == "unlock door" or go1 == "unlock chest" or go1 == "go to door" or go1 == "look at chest" or go1 == "look behind" or go1 == "go to chest" or go1 == "go behind":
        print("\n[It is locked. You should try again later when you have a key.]\n")
    elif go1 == "look behind me" or go1 == "check chest" or go1 == "check wooden chest" or go1 == "look at wooden chest":
        print("\n[It is locked. You should try again later when you have a key.]\n")
    else:
        print("[You can't do that.]")
