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
MINIMUN_VALUE=min(Array)

# THIS CODE IS WITHOUT USING MAX AND MIN FUNCTION.
#MAXIMUN_VALUE=0
#MINIMUN_VALUE=100000000000000000000000000000000
#for i in Array:
#  if i>MAXIMUN_VALUE:
#     MAXIMUN_VALUE=i  
#  if i<MINIMUN_VALUE:
#     MINIMUN_VALUE=i

print("__________________________")
print(f"YOUR INPUT IS  -  {Array}")
print("___________________________________")
print(F"MAXIMUN VALUE IS - {MAXIMUN_VALUE}")
print("___________________________________")
print(F"MINIMUN VALUE IS - {MINIMUN_VALUE}")
 