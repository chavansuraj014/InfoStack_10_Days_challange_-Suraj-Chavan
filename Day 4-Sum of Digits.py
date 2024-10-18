print("___________________________________________________________________________")
NUMBER = int(input("HOW MANY NUMBERS DO YOU WANT TO ENTER - "))
print("                                                             ")

for i in range(1,NUMBER+1):
    
    print("******************************************************************")
    value=int(input(f"ENTER VALUE NO {i} - "))
    X=str(value)
    MYLIST=list(X)
    C=0
    for J in MYLIST:
        X1=int(J)
        C+=X1
    print("                                   ")
    print(f"-----------YOUR INPUT IS {value}")
    print(f"-----------YOUR OUTPUT IS {C}")
    print("                             ")
    