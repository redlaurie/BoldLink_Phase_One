
def StartGreeting():
    message = input("what is your name?")
    if message == "":
        print("Hello world!")
    else:
        print("Hello " + message)

StartGreeting()


