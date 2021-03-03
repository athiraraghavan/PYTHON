# co1 2 leap year
f=int(input("enter the year"))
c=int(input("enter current year"))
for i in range(c,f):
  if(i%4==0 or i%100==0 or i%400==0):
   print(i)
  i=i+1
