Array=[]
Array_2=[]
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
print("                          ") 
print("__________________________")
print(f"YOUR INPUT IS  -  {Array}")

value=len(Array)

for i in range(1,len(Array)+1):
  num_2=Array[value-i]
  Array_2.append(num_2)
print("_________________________")
print(f"REVERSE ARRAY OUTPUT IS - {Array_2}")
 
