#c01 6.store a list of 1st name and count theoccurance of a within the list
l=input("enter the name:")
print(l)
count=0
for i in l:
 if i=="a":
   count+=1
print("occurance of a is:",count)