Array1=[]
Array2=[]
print("__________________________________________________________________")
N=int(input("HOW MANY NUMBERS DO YOU WANT PUT IN THE ARRAY-1 - "))
M=int(input("HOW MANY NUMBERS DO YOU WANT PUT IN THE ARRAY-2 - "))


for i in range(1,N+1):
    print("-----")
    Value=int(input(f"ENTER ARRAY-1 OF VALUE {i} - "))
    Array1.append(Value)
print("                                                 ")
print(Array1)
print("___________________________________________________________________")
            
for i in range(1,M+1):
    print("                                        ")
    print("-----")
    Value=int(input(f"ENTER ARRAY-2 OF VALUE {i} - "))
    Array2.append(Value)
print("                                                 ")
print(Array2)
print("_________________________________________________")
                   
Array3=Array1+Array2
MAXIMUM=max(Array3)
Array4=[]

for i in range(0,MAXIMUM+1):
    for j in Array3:
       if i==j:
            Array4.append(j)

print("____________________________________")
print(F"YOUR ARRAY-1 {Array1}")
print(F"YOUR ARRAY-2 {Array2}")
print("____________________________________")
print(F"---------------YOUR OUTPUT IS {Array4}")    
    

             
