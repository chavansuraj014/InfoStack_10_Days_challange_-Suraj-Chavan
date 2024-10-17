
try:
  NUMBER=int(input("HOW MANY INPUT DO YOU WANT TO ENTER - "))
  for i in range(1,NUMBER+1):
    print("************************************************************************************************")
    VALUES=str(input(f"ENTER YOUR INPUT NO {i} -  "))
  
    X=list((VALUES))
    length_X=(len(X)//2)
    X1=(X[0:length_X])
    X2=(X[length_X+1:])
    C=[]                                    #NEW LIST FOR REVERSE X2
    for i in range(1,len(X2)+1):
        C.append(X2[len(X2)-i])

   
    if X1==C:
        print("______________________________________________________________")
        print(F"YOUR INPUT IS {VALUES}")
        print(F"FRONT SIDE IS {X1} ") 
        print(F"BACK SIDE IS  {C} ")
        print("______________________________________________________________")
        print("------SINCE BOTH SIDES ARE THE SAME, SO IT IS PALINDROME------ ")
        print("                                                                ")
    else:
        print("______________________________________________________________")
        print(F"YOUR INPUT IS {VALUES}")
        print(F"FRONT SIDE IS {X1} ") 
        print(F"BACK SIDE IS  {C} ")
        print("______________________________________________________________")
        print("!!SINCE BOTH SIDES ARE NOT SAME, SO IT IS NOT PALINDROME!!")
        print("                                                       ")
    
except ValueError:
       print("??? PLEASE ENTER INT VALUE")


   
