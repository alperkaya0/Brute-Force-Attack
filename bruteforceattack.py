import getpass
import os
username = getpass.getuser()
print("Hello "+username+"!")

current = os.path.dirname(os.path.realpath(__file__))

exit = 0

while(exit != "exit" and exit != "Exit"):
    rulebased = False
    rulebased = input("Write \"True\" or \"False\" to search rule-based or not.Rule-based means check for both capitalized and normal string.\n")

    if rulebased == "False" or rulebased == "false":
        example = input("Enter the password you wanna search: ")
        for name in os.listdir(current+"\\passworddatabase"):
            p = open(current+"\\passworddatabase\\"+name,"r",encoding="latin-1")
            found = False
            for x in p.readlines():
                if example == (x).strip():
                    x = x.strip()
                    found = True
                    break

            if found:
                print("Password found in "+name+" !")
                print("Result = "+str(x))
            else:
                print("Couldn't find in "+name+" ...")
        
        exit = input("Write \"exit\" and press enter to exit otherwise program will run in loop(press enter)...\n")
        print()
    elif rulebased == "True" or rulebased == "true":
        example = input("Enter the password you wanna search: ")
        for name in os.listdir(current+"\\passworddatabase"):
            p = open(current+"\\passworddatabase\\"+name,"r",encoding="latin-1")
            found = False
            foundname = ""
            for x in p.readlines():
                if example == (x).strip():
                    foundname = x.strip()
                    found = True
                    break
                if example.capitalize() == (x).strip():
                    foundname = (x).strip().capitalize()
                    found = True
                    break

            if found:
                if found:
                    print("Password found in "+name+" !")
                    print("Result = "+foundname)
            else:
                print("Couldn't find in "+name+" ...")
        
        exit = input("Write \"exit\" and press enter to exit otherwise program will run in loop(press enter)...\n")
        print()
