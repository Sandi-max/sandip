#fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
words=list()
for words in fh:
    words=words.split()
    for i in words:
        if lst==None:
            lst=i
        elif i in lst:
            continue
        lst.append(i)
lst.sort()
print(lst)
