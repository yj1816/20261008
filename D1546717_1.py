x = int(input())
if x < 0 or x > 15:
    print("輸入錯誤")
else:
    r_20 = x % 2 
    q1 = x // 2
    
    r_21 = q1 % 2
    q2 = q1 // 2
    
    r_22 = q2 % 2
    q3 = q2 // 2
    
    r_23 = q3 % 2
    
    r_80 = x % 8
    q_8 = x // 8
    
    r_81 = q_8 % 8
    
    r_16 = x % 16
    
    if r_16 == 10:
        h = "A"
    elif r_16 == 11:
        h = "B"
    elif r_16 == 12:
        h = "C"
    elif r_16 == 13:
        h = "D"
    elif r_16 == 14:
        h = "E"
    elif r_16 == 15:
        h = "F"
    else:
        h = str(r_16)
        
    print(f"二進制={r_23}{r_22}{r_21}{r_20}")
    print(f"八進制={r_81}{r_80}")
    print(f"十六進制={h}")
