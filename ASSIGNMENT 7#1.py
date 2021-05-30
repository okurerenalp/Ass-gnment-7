# Those are example guest lists.
rossList = ["Marcel", "Judy", "Jack", "Carol", "Susan", "Rachel", "Chandler", "Monica", "Joey", "Phoebe"]
rachelList = ["Paolo", "Barry", "Mindy", "Mr. Heckles","Ross", "Chandler", "Monica", "Joey", "Phoebe"]
chandlerList = ["Janice", "Mr. Heckles", "Ross", "Rachel", "Monica", "Joey", "Phoebe" ]
monicaList = ["Fun Bobby", "Judy", "Jack", "Mr. Heckles", "Ross", "Rachel", "Chandler", "Joey", "Phoebe"]
joeyList = ["Big Joey", "Ursula", "Mr. Heckles", "Ross", "Rachel", "Chandler", "Monica", "Phoebe"]
phoebeList = ["Ursula", "Granny", "Ross", "Rachel", "Chandler", "Monica", "Joey"]

# This list is to hold all the guests. 
guestList = []

# This function is to add the elements of one list to another.
# If there are any common elements, it'll not add them.
# Both parameters should be lists. First one is the
# list that you wanted to add its elements to, and the
# second one is the list that you wanted to store the elements in.
def create_guest_list(indList, guestList):
# If the second list is empty, the function will add all the
# elements in the list 1 to list 2.
    if len(guestList) == 0:
        for i in indList:
            guestList.append(i)
    else:
 # The program will check that if there is any common
 # elements between two lists, using a nested loop.
 # If it finds a common element, it'll turn the bool var
 # "exists" to True. The function will add the elements 
 # to the second list according to the value of the "exists".
        for i in indList:
            exists = False
            for j in guestList:
                if i == j:
                    exists = True
                    break
            if exists == False:
                guestList.append(i)

# Sort the  guestList.
    guestList = sorted(guestList)
# Print the guestList.
    print(guestList)
# Return the final version of the guestList.
    return guestList
            

# TESTS
create_guest_list(rossList, guestList)
create_guest_list(rachelList, guestList)
create_guest_list(chandlerList, guestList)
create_guest_list(monicaList, guestList)
create_guest_list(joeyList, guestList)
create_guest_list(phoebeList, guestList)