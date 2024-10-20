Array=[]
NUMBER=int(input("HOW MANY NUMBERS DO YOU WANT TO PUT IN THE ARRAY - "))
for i in range(1,NUMBER+1):
    print("                         ")
    print("-------------------------")
    try:
       num=int(input(F"ENTER NO {i} - "))
    except ValueError:
       print("??? PLEASE ENTER INT VALUE")
       try:
         num=int(input(F"ENTER NO {i} - "))
       except ValueError:
          print("??? PLEASE ENTER INT VALUE")
          print("SORRY PLEASE TRY AGAIN")
          exit()
    Array.append(num) 
MAXIMUN_VALUE=max(Array)
mylist=[]
MISSING_NO=[]
 
for i in range(0,MAXIMUN_VALUE+1):
   if i in Array:
      mylist.append(i)

for i in range(mylist[0],MAXIMUN_VALUE+1):
    
      if i not in mylist:

         MISSING_NO.append(i)
print("___________________________________________")
print(F"YOUR INPUT IS {Array}")
print("                     ")
print(F"------missing number in the array - {MISSING_NO}-------")
print("                                                        ")



