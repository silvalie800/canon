def runMainFunction():
	# This is the main function
	return

def checkExit():
	resp = ""
	while (resp != "n" or resp != "y"):
		resp = input("Do you want to continue ? [y/n]")
		if resp == "n" :
			return False
	return True

running = True
while running :
	runMainFunction()
	running = checkExit()

