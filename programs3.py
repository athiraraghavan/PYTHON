# co1 3 list comprehension
# A) positive list of numbers
list1=[3,-7,-5,0,4,-2]
newlist=[x for x in list1 if x>0]
print(newlist)

#co1 3 B)square of n numbers
n=int(input("enter the number of numbers"))
list=[]
for i in range(n):
  a=int(input("enter the number"))
  list.append(a)
print(list)
list=[x*x for x in list]
print(list)

#c01 3 C)list of vowels
word=input("enter the word:")
vowels=[x for x in word if x in['a','e','i','o','u']]
print(vowels)
