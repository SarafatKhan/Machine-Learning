def replaceWord(oldWord,newWord):
    with open("textfile.txt", "r+") as f:
        content = f.read()
        f.seek(0)
        newContent = content.replace(oldWord,newWord)
        f.write(newContent)

oldWord = input("Which word you want to change: ")
newWord = input("What should be new word: ")

replaceWord(oldWord, newWord)


# now we will work for a list of words that stored in a file name - senceredWords.txt
oldWords = ["dolor", "dolorem", "output", "culpa"]
def removeWords():
    with open("textfile.txt", "r+") as f:
        for i in oldWords:
            content = f.read()
            f.seek(0)
            newContent = content.replace(i,"#"*len(i)) 
            f.write(newContent)
removeWords()  