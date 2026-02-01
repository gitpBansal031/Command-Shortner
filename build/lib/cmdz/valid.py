def invalid_message():
    print("Invalid command")

def isValid(sys,l,r):
    if(len(sys.argv)<l or len(sys.argv)>r):
        invalid_message()
        return False
    return True
