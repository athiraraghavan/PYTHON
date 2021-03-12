#co1 5.store over after 100
n=int(input("enter the limit:"))
list=[]
for x in range(n):
  x=int(input("enter the number"))
if x<100:
    list.append(x)
else:
    list.append('over')
print(list)
