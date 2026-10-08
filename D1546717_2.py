A=int(input())
B=int(input())
if (A != 0 and A != 1) or (B != 0 and B != 1) :
     print("輸入錯誤")
else:
    OrA = A
    OrB = B
    AndA = A
    AndB = B
    XorA = A
    XorB = B
    
    if OrA==1 or OrB==1 :
        Or = 1
    else:
        Or = 0
    
    if AndA==1 and AndB==1 :
        And = 1
    else:
        And = 0

    if XorA != XorB:
        Xor = 1
    else:
        Xor = 0
    print(f"OR={Or}")
    print(f"AND={And}")
    print(f"XOR={Xor}")