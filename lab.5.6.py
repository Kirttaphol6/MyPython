def beforMidterm(a,s,b):
    t = a+s+b
    return t

score = int(input("คะแนนเก็บ: "))
jitpisai = int(input("คะแนนจิตยิสัย: "))
midterm = int(input("คะแนนกลางภาค: "))


print("รวม %.2f "% beforMidterm(score, jitpisai, midterm))    
