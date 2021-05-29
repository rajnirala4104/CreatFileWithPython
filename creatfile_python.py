askMakeFile = input("Do you want to make a file? ")
if askMakeFile == "yes":
    askName = input("Enter the name of file:")
    your_file = open(askName+".txt","x")
    your_file.close()
    askWrite = input("Do you want to write in your file: ")
    if askWrite == "yes":
        ask_What_Write = input("What do you want to write in your file?, please write here... : ")
        with open(askName+".txt", "w") as yourFile:
            yourFile.write(ask_What_Write)
            # print(yourFile.read())
else:
    print("Ok thanks to come here...")