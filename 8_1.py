mylist = []
fhand = open('8.txt')
for line in fhand :
    words = line.split()
    for word in words :
     if word in mylist:
         continue
     mylist.append(word)
    print(sorted(mylist))