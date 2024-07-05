
def Fa(C):
    F = (9/5)* C + 32
    return F

def Kel(C):
    k = (C+273.15)
    return k

C = int(input("รับค่าองศา C: "))
print("Fa %.2f "% Fa(C))
print("Kel %.2f "% Kel(C))




