# co1 20 removing even numbers from the list
list=[1,2,3,4,5,6,7,8,9,10]
print("LIST IS:",list)
for i in list:
  if(i%2==0):
   list.remove(i)
print("LIST AFTER REMOVING EVEN NUMBERS:",list)
