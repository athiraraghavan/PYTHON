#c01 4:count of each word in a line of text
s=input("enter the string")
count=dict()
word=s.split()
for i in word:
  if i in count:
    count[i]+=1
  else:
    count[i]=1
print(count)