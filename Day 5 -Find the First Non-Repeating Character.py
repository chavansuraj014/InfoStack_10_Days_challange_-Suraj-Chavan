value = input("ENTER YOUR VALUE - ")
value=value.upper()
list1=list(value)
set1=set()
list2=[]
x=0
for i in range(0,len(list1)):
    if list1[i] not in set1:
        set1.add(list1[i])   
    else:
        x+=1
        list2.append(list1[i])      
for i in list2 :
    if i in set1:
        set1.remove(i)
          
if x==len(list1)/2:
    print("_______________________________________")
    print("-1 (All characters repeat)")
    print("                                       ")
    
else :
    print("_______________________________________")
    print(F"{set1} characters that doesn't repeat")
    print("                                       ")
