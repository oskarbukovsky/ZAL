STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
def writeTextToFile(text):
    f = open("hw02.txt", "w")
    f.write(STATICKY_TEXT + str(text))
    f.close()
    return "hw02.txt"