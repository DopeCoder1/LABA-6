import random


def dataOutput(students):
    for j in range(len(students)):
        print(
            f"{students[j].get_id()}) LOGIN:{students[j].get_login()}     PASSWORD:{students[j].get_password()}       ROLE:{students[j].get_role()}")


def dataProcessing(students):
    while True:
        print("\n----------------------AUTHORIZATION----------------------")
        LOGIN = str(input("LOGIN: "))
        PASSWORD = str(input("PASSWORD: "))

        for j in range(len(students)):
            if LOGIN == students[j].get_login() and PASSWORD == students[j].get_password():
                print(f"\n[U ARE SUCCESSFULLY LOGGED: {students[j].toString()}]")
                print("PRESS [1] TO EDIT LOGIN")
                print("PRESS [2] TO CHANGE PASSWORD")
                print("PRESS [3] TO DELETE OWN ACCOUNT")
                print("PRESS [0] TO EXIT")
                key = int(input("ENTER THE NUMBER: "))

                if key == 1:
                    new_login = str(input(f"ENTER THE NEW LOGIN FOR {students[j].toString()} \n----->: "))
                    students[j].set_login(new_login)
                    print(f"U R NEW LOGIN: {students[j].toString()}")

                elif key == 2:
                    new_password = str(input(f"ENTER THE NEW PASSWORD FOR {students[j].toString()} \n----->: "))
                    students[j].set_password(new_password)
                    print(f"U R NEW PASSWORD: {students[j].toString()}")

                elif key == 3:
                    print(f"U R {students[j].toString()}    HAS BEEN DELETED...")
                    del students[j]
                    dataOutput(students)
                    break

                elif key == 0:
                    print("EXIT...")
                    break


def randomWord(length=3):
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


def creatObj(students, User, length):
    for j in range(length):
        students.append(User(j+1, randomWord(), randomWord(), randomWord()))



