print("---------------------------------------------------------------------------")
Number=int(input("HOW MANY NUMBERS DO YOU WANT TO PUT IN THE ARRAY - "))
Array1=[]
for i in range(1,Number+1):
    print("_________________")
    value=int(input(f"ENTER VALUE NO {i} - "))
    Array1.append(value)
print("_______________________________")
print(Array1)
X=Array1
print("                               ")
print("------------------------------------------------------------")
M=int(input('ENTER NUMBER OF POSITIONS TO ROTATE THE ARRAY - '))
C=len(Array1)-M
Array1=Array1[C:len(Array1)]+Array1[0:C]

print("_______________________________")
print(F"-------- YOUR INPUT IS {X}")
print("                               ")
print("________________________________")
print(F"--------YOUR OUTPUT IS {Array1}")
print("                                ")






