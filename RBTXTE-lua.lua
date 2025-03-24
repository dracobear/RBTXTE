repeat
  io.write("welcome to RBTXTE-Lua \nPlease choose an operation\n")
  io.write("> ")
  oneinput = io.read()
  if oneinput == "help" then
    io.write("operations include: \n● read (reads a file)\n● append (appends text to the end of a file)\n● write (writes to a file replacing all text in it )\n● exit (exits)", "\n")
  elseif oneinput == "read" then
    io.write("enter filename (with file extension)\n")
    io.write("> ")
    twoinput = io.read()
    reader = io.open(twoinput, 'r')
    io.write(reader:read("*a"))
    reader:close()
  elseif oneinput == "append" then
    io.write("enter filename (with file extension)\n")
    io.write("> ")
    twoinput = io.read()
    apper = io.open(twoinput, 'a')
    io.write("input text to append\n")
    io.write("> ")
    threeput = io.read()
    outinput = apper:write(threeput, "\n")
    apper:close()
  elseif oneinput == "write" then
    io.write("enter filename (with file extension)\n")
    io.write("> ")
    twoinput = io.read()
    writer = io.open(twoinput, 'w')
    io.write("input text to replace all file text with\n")
    io.write("> ")
    threeput = io.read()
    outinput = writer:write(threeput)
    writer:close()
  end
until oneinput == "exit"
