with open("sampleFile.txt") as f:
    content = f.read()
    word = input("Which word you want to search: ")
    if(word in content):
        print(f"The word {word} is present in the file.")
    else:
        print(f"The word {word} is not present in the file.")