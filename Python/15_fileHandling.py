f = open("samplefile.txt")
text = f.read()
print(text)
f.close()

newText = "This a new string for writing in a new file."
f = open("sampleFile02.txt", "w")
f.write(newText)
f.close()