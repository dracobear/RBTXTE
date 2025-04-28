package main

import (
	"fmt"
	"os"
)

func main() {
	var input string
	var output string
	var writeput string
	for {
		fmt.Println("welcome to rbtxte-GO \nnow written in golang!")
		fmt.Print("> ")
		fmt.Scan(&input)
		switch input {
		case "help":
			fmt.Println("use help to see this message \nuse exit to exit\nuse read to read a file\nappend does not work right now maybe\noverwrite overwrites a file")
		case "exit":
			fmt.Println("exiting")
		case "read":
			fmt.Println("file to read?")
			fmt.Print("> ")
			fmt.Scan(&output)
			var read, err = os.ReadFile(output)
			if err != nil {
				fmt.Println("Error in ReadFile")
			}
			fmt.Println(string(read))
		case "append":
			fmt.Println("file to append to?")
			fmt.Print("> ")
			fmt.Scan(&output)
			var flile, err = os.OpenFile(output, os.O_APPEND, 0644)
			if err != nil {
				fmt.Println("Error in os.Open")
				flile.Close()
			} else {
				fmt.Println("words to append?")
				fmt.Print("> ")
				fmt.Scan(&writeput)
				flile.WriteString(writeput)
				flile.Close()
			}
		case "new":
			fmt.Println("file to create?")
			fmt.Print("> ")
			fmt.Scan(&output)
			var flile, err = os.Create(output)
			if err != nil {
				fmt.Println("error in os.Create")
				flile.Close() //justin case
			} else {
				fmt.Println("file created succesfully")
				flile.Close()
			}
		case "overwrite":
			fmt.Println("file to overwite?")
			fmt.Print("> ")
			fmt.Scan(&output)
			var flile, err = os.OpenFile(output, os.O_WRONLY, 0644)
			if err != nil {
				fmt.Println("error in os.OpenFile")
				flile.Close() //justin case strikes again!!!
			} else {
				fmt.Println("words to write?")
				fmt.Print("> ")
				fmt.Scan(&writeput)
				flile.WriteString(writeput)
				flile.Close()
			}

		}
		if input == "exit" {
			break
		}
	}
}
