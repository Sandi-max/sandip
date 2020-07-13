#fname = input("Enter file name: ")
hand =open('mbox-short.txt')
count = 0
for  lin in hand:
    lin = lin.rstrip()
    line = lin.split()
    #print(line)
    if len(line) < 3:
    	#print('\n lines\r')
    	continue
        
    if line[0] != 'From':
    	#print('lines')
    	continue
    count += 1
    print(line[1])

print("There were", count, "lines in the file with From as the first word")
