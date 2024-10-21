Array=[]
Array3=[]
print("                                                        ")
NUMBER=int(input("HOW MANY NUMBERS DO YOU WANT PUT IN THE ARRAY - "))

if NUMBER>1 and NUMBER<=500:
    for i in range(1,NUMBER+1):
        print("          ")
        print("******************************************")
        VALUE=int(input(f"ENTER VALUE NO {i} - "))
        Array.append(VALUE)
    
    
    for i in range(0,NUMBER):
        Array2=[]
       
        C=1
        for j in Array:
          if Array[i] != j:
            Array2.append(j)
       
        for K in Array2:
          
           C=C*K
        Array3.append(C)
    print("                                                                                         ")
    print("__________________________________________________________________________________________")
    print(f"---------- YOUR INPUT IS {Array} ----------") 
    print("                                                                                         ")
    print(f"---------- YOUR OUTPUT IS {Array3} ----------")
    print("                                                                                          ")
            
        
else:
    print("??? PLEASE ENTER GRATER THAN 1 AND LOWER THAN 500")
       
    
    
             
