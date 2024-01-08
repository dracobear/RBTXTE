while True:
    print("rbtxte lite \nfilenames must end in .txt")
    print("edit or read")
    chos = input('> ')
    if chos == "read":
       print("input filename")
       filena = input('> ')
       try:
         red = open(filena)
         print(red.read())
       except FileNotFoundError:
         print("file not found")
       except PermissionError:
         print("access denied")
    elif chos == "write":
      print("input filename")
      filena = input('> ')
      print("input text for file")
      filetx = input('> ')
      try:
         open(filena, 'a').write.filetx
      except FileNotFoundError:
         print("file not found")
      except PermissionError:
         print("access denied")
