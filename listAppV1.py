"""
myList = []
def mainProgram():
    
    print("Hello, there! Lets work with lists.")
    print("Choose from the following options. Type a number below!")
    choice = input("1. Add to a list  , 2. Return the value at an index position!     ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
    #TO ADD: 1. A way to loop the action ,  2. A way to quit ,  3. Think of repetition,
def addToList():
    print("Adding to a list.. That was.. a choice. Yikes!"
    newItem = input("Type an Integer here.    ")
    newList.append(int(newItem))

def indexValue():
    print("Oh, you need some perticular data? Fuckin loser.")
    indexPos = input("*audible sigh*  What Index are you curious about?     ")
    print(myList[int(indexPos)])

if__name__ == "__main__":
    mainProgram()
"""
def addToList():
    print("Adding to a list.. That was.. a choice. Yikes!"
    newItem = input("Type an integer here.   ")
    newList.append(int(newItem))

def addABunch():
    print("We're gonna add some whole ass numbers here below")
    numToAdd = input("How many new number do you wanna add?   ")
    numRange = input("Add how high do you want it to add?    ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Hey dumbass. List is done.")

def indexValue():
    print("Oh, you need some perticular data? Fuckin loser.")
    indexPos = input("*audible sigh*  What Index are you curious about?     ")
    print(myList[int(indexPos)])

def sortList(myList):
    
def randomSearch():
    print("RANDOM SEARCH TIME????!!!?")
    print(myList[random.randint(0, len(,yList)-1)])

def linearSearch():
    print("Oh for the love of god! you want me to check them one by one?!?")
    searchItem = input("What are you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your shit is at index position  {}".format(x))

if__name__ == "__main__":
    mainProgram()

import random
myList = []

def mainProgram():
    while True:
        try:
            print("Hey. We workin' with list or what?!")
            print("Choose from the following options. Baka!! Type a number below!")
            choice = input("""1. Add to a list or
2. Add a bunch of numbers
3. Return a value at an index
4. Random Search
5. Linear Search
6. Print contents of list
7. Quit Program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                print(myList)
            else:
                break
        except:
            print("You got an error dumbass!")
