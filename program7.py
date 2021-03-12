# co1 7:list
list1=[1,2,3,4,5]
list2=[2,4,6,8]
print("element in list1",list1)
print("element in list2",list2)
s1=0
s2=0
if(len(list1)==len(list2)):
 print("list have same length")
else:
 print("list have different length")
for i in range(len(list1)):
  s1=s1+list1[i]
print("sum of list1",s1)
for i in range(len(list2)):
  s2=s2+list2[i]
print("sum of list2",s2)
if(s1==s2):
 print("sum of list is same")
else:
 print("sum of list is different")
for i in list1:
 for j in list2:
   if i==j:
    print("common element in list is",i)
