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
def recursiveBinarySearch(unique_list, low, high, x):
    if

if__name__ == "__main__":
    mainProgram()

import random
myList = []

def mainProgram():
    while True:
        try:
            print("Hey. We workin' with list or what?!")
            print("Choose from the following options. Baka!! Type a number below!")
            choice = input(""""""1. Add to a list or
2. Add a bunch of numbers
3. Return a value at an index
4. Random Search
5. Linear Search
6. Print contents of list
7. Quit Program)""""""
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
            print("You got an error dumbass!")"""




import random
myList = []
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hey. We workin' with list or what?!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list or
2. Add a bunch of numbers
3. Get an item at index
4. Sort List
5. Random Search
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print contents of list
10.Quit Program    """)
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
            elif choice == "7":
                binSearch = input("What number are looking for dude?!?!   ")
                result = recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are looking for dude?!?!   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}, now will you get outta my face?!".format(result))
                else:
                    print("It aint here fuckface. go home..")
            elif choice == "9":
                printLists()
            else:
                break
        """except:
            print("You got an error dumbass!")"""
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
"""
if__name__ == "__main__":
    mainProgram()"""

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

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Ya wanna see your lists unique values? Y/N    ")
    if showMe.lower() == "y":
        print(unique_list)

def indexValues():
    print("Oh, you need some perticular data? Fuckin loser.")
    indexPos = input("*audible sigh*  What Index are you curious about?     ")
    print(myList[int(indexPos)])
    
def randomSearch():
    print("RANDOM SEARCH TIME????!!!?")
    print(myList[random.randint(0, len(,yList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])

def linearSearch():
    print("Oh for the love of god! you want me to check them one by one?!?")
    searchValue = input("What are you looking for?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("Your shit is at index position  {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which fuckin list you wanna see, sorted or un-sorted?    ")
        if whichOne.lower() == "sorted":
            print(unique_List)
    
def recursiveBinarySearch(unique_list, low, high, x):
    if hight >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your shit is at {}".format(mid))
            return mid

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Are you stoopid?! Ya' aint here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <- high:
        mid - (high + low) // 2

        if unique_list[mid] < x:
            low - mid + 1

        elif unique_list[mid] > x:
            high = mid - 1

        else:
            return mid
        return -1

if__name__ == "__main__":
    mainProgram()

