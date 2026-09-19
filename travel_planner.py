import random

info = {}
places = []


def admin():
    print("""ADMIN MENU
1. ADD
2. VIEW
3. UPDATE""")


def add_infos():
    n = int(input("ENTER A NUMBER OF TRAVEL DESTINATION TO ADD : "))

    for i in range(n):
        cities = input("ENTER THE TRAVEL DESTINATIONS : ")
        places.append(cities)

    for j in places:
        print("ENTER INFO FOR THIS DESTINATION", j)
        b = int(input("ENTER A BUDGET FOR THE DESTINATION : "))
        d = int(input("ENTER DAYS FOR THE DESTINATION : "))
        info[j] = [b, d]


def view_infos():
    print("DESTINATION INFORMATIONS")
    print(info)


def update_infos():
    print("""MENU
1. ADD DESTINATIONS
2. DELETE DESTINATIONS
3. UPDATE BUDGET
4. UPDATE NO OF DAYS""")

    while True:
        ch = int(input("ENTER YOUR CHOICE : "))

        if ch == 1:
            new = input("ENTER A NEW DESTINATION : ")
            newb = int(input("ENTER A BUDGET FOR THE NEW DESTINATION : "))
            newd = int(input("ENTER DAYS FOR THE NEW DESTINATION : "))
            info[new] = [newb, newd]

        elif ch == 2:
            cit1 = input("ENTER A DESTINATION TO BE DELETED : ").strip().lower()
            found = False

            for i in list(info):
                if i.lower() == cit1:
                    info.pop(i)
                    found = True
                    break

            if not found:
                print("DESTINATION NOT FOUND")

        elif ch == 3:
            cit2 = input("ENTER THE DESTINATION TO MODIFY BUDGET : ")
            newb2 = int(input("ENTER THE NEW BUDGET : "))
            found = False

            for i in info:
                if i == cit2:
                    info[i][0] = newb2
                    found = True
                    break

            if not found:
                print("DESTINATION NOT FOUND")

        elif ch == 4:
            cit3 = input("ENTER THE DESTINATION TO MODIFY DAYS : ")
            newd2 = int(input("ENTER THE NEW NO OF DAYS : "))
            found = False

            for i in info:
                if i == cit3:
                    info[i][1] = newd2
                    found = True
                    break

            if not found:
                print("DESTINATION NOT FOUND")

        ans = input("KEEP UPDATING ?(YES/NO) : ")
        if ans.lower() != "yes":
            break


def user():
    print("""USER MENU
1. VIEW DESTINATIONS
2. SEARCH [NAME]
3. SEARCH[BUDGET]
4. SEARCH[DAYS]
5. SURPRISE DESTINATION
6. TRIPS BOOKED""")


def viewdes():
    for i, j in info.items():
        print("DESTINATION :", i, "BUDGET :", info[i][0], "NO OF DAYS :", info[i][1])


def search_name():
    x = input("ENTER DESTINATION NAME TO VIEW DETAILS : ")
    found = False

    for i, j in info.items():
        if i == x:
            print("BUDGET :", info[i][0])
            print("NO OF DAYS :", info[i][1])
            print("GREAT CHOICE!!!")
            found = True
            break

    if not found:
        print("DESTINATION NOT FOUND")


def search_budget():
    y = int(input("ENTER YOUR BUDGET FOR THE TRIP : "))
    found = False

    for i, j in info.items():
        if y >= j[0]:
            print("DESTINATION :", i)
            print("BUDGET :", info[i][0])
            print("NO OF DAYS :", info[i][1])
            print("HAVE FUN!")
            found = True

    if not found:
        print("DESTINATION NOT FOUND")


def search_days():
    z = int(input("ENTER YOUR DAYS FOR THE TRIP : "))
    found = False

    for i, j in info.items():
        if z >= j[1]:
            print("DESTINATION :", i)
            print("BUDGET :", info[i][0])
            print("NO OF DAYS :", info[i][1])
            print("HAVE FUN!")
            found = True

    if not found:
        print("DESTINATION NOT FOUND")


def surpriseme():
    if not info:
        print("NO DESTINATIONS")
        return

    print("THIS IS YOUR SURPRISE DESTINATION")
    i, (j, k) = random.choice(list(info.items()))
    print("DESTINATION :", i)
    print("BUDGET :", j)
    print("DAYS :", k)


try:
    while True:
        print("""GENERAL MENU
1. ADMIN
2. USER
3. EXIT""")

        choice8 = int(input("ENTER A CHOICE PLEASE : "))

        if choice8 == 1:
            admin()

            while True:
                cho = int(input("ENTER A CHOICE ADMIN : "))

                if cho == 1:
                    add_infos()
                elif cho == 2:
                    view_infos()
                elif cho == 3:
                    update_infos()

                choice = input("keep editing?(YES/NO) ")
                if choice.lower() != "yes":
                    break

        elif choice8 == 2:
            user()

            while True:
                c_hoice = int(input("ENTER A CHOICE USER : "))

                if c_hoice == 1:
                    viewdes()
                elif c_hoice == 2:
                    search_name()
                elif c_hoice == 3:
                    search_budget()
                elif c_hoice == 4:
                    search_days()
                elif c_hoice == 5:
                    surpriseme()

                uno = input("KEEP BOOKING?(yes/no) : ")
                if uno.lower() != "yes":
                    break

        elif choice8 == 3:
            break

        guiop = input("YES OR NO ")
        if guiop.lower() != "yes":
            break

except (IndexError, ValueError):
    print("INPUT ERROR")
finally:
    print("suceeded")
