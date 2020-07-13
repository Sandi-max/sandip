#fhand = open('‪san.txt')
#for line in fhand:
 #   line = line.rstrip()
  #  if not line.startswith('Form'):continue
   # words = line.split()
    #print(words[2])
from collections import deque
q=deque(["sandip","atal","dipesh"])
q.append("bishal")
print(q.popleft())
