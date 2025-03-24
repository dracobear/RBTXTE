from rich import print
import questionary
version = "v0.05 (misery)"
while True:
    put = questionary.select(
            "What would you like to do?",
            choices=[
                "read",
                "edit",
                "new",
                "version",
                "exit"
                ]).ask()
    if put.startswith("read") == True:
        aput = questionary.path(
                "enter file path"
                ).ask()
        try:
            woa = open(aput, 'r')
            print(woa.read())
        except FileNotFoundError:
            print("[bold red3]" + aput + ": Error, file not found" + "[/bold red3]")
        except PermissionError:
            print("[bold red3]" + aput + ": Error, access denied" + "[/bold red3]")
    elif put.startswith("edit") == True:
        aput = questionary.path(
                "enter file path"
                ).ask()
        try: 
            writ = questionary.select(
                    "add or overwrite?",
                    choices=[
                        "add",
                        "overwrite"
                        ]).ask()
            if writ == "add":
                wrot = questionary.text("text to append?").ask()
                open(aput, 'a').write(wrot)
            elif writ == "overwrite":
                wrot = questionary.text("text to replace?").ask()
                open(aput, 'w').write(wrot)
            else:
                ("thats not an option supported by the editor")
        except FileNotFoundError:
            print("[bold red3]" + aput + ": Error, file not found" + "[/bold red3]")
        except PermissionError:
            print("[bold red3]" + aput + ": Error, access denied" + "[/bold red3]")
    elif put.startswith("new") == True:
        atput = questionary.text("file to create (dont forget file type!)").ask()
        try:
            new = open(atput, 'x')
        except FileExistsError:
            print("[bold red3]" + aput + ": Error, file allready exsists" + "[/bold red3]")
        except PermissionError:
            print("[bold red3]" + aput + ": Error, access denied" + "[/bold red3]")
    elif put.startswith("version") == True:
        print("version is: " + version)
    elif put == "exit":
        print("goodbye")
        exit()
