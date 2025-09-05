# for all lines
# f = open("sampleFile.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


# for single line
# f = open("sampleFile.txt")
# line = f.readline()
# print(line, type(line))
# f.close()


f = open("sampleFile.txt")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()



#it will automatically close the file
with open("sampleFile.txt") as f:
    r = f.read()
    print(r, type(r))