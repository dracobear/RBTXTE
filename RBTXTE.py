from colorama import Fore
version = "v0.03 (heros end)"
print("RBTXTE "+version)
print("allways remember to end your filenames in .txt!")
helpmessage = "new (filename). makes a new file \nopen (filename) reads a file, \nedit (filename) edits a file \nhelp shows this message \nexit quits the program"
print(helpmessage)
while True:
    put = input("what do you want to do? ")
    if put.startswith("open ") == True:
        aput = put.replace("open ", "")
        try:
            woa = open(aput, 'r')
            print(woa.read())
        except FileNotFoundError:
            print(Fore.RED + aput + ": Error, file not found" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + aput + ": Error, access denied" + Fore.WHITE)
    elif put.startswith("edit ") == True:
        aput = put.replace("edit ", "")
        try:
            writ = input("add or overwrite? ")
            if writ == "add":
                wrot = input("text to append? ")
                open(aput, 'a').write(wrot)
            elif writ == "overwrite":
                wrot = input("new text? ")
                open(aput, 'w').write(wrot)
            else:
                ("thats not an option supported by the editor")
        except FileNotFoundError:
            print(Fore.RED + aput + ": Error, file not found" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + aput + ": Error, access denied" + Fore.WHITE)
    elif put.startswith("new ") == True:
        aput = put.replace("new ", "")
        try:
            new = open(aput, 'x')
        except FileExistsError:
            print(Fore.RED + aput + ": Error, file allready exsists" + Fore.WHITE)
        except PermissionError:
            print(Fore.RED + aput + ": Error, access denied" + Fore.WHITE)
    elif put == "help":
        print(helpmessage)
    elif put == "exit":
        exit()
    else:
        print("that is not an option supported by the editor")