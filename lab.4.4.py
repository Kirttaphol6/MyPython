A = {1,2,3,4,5,6,8}
D = {1,3,5,6,7,8}
C = {6,8,9,10}
print(A.union(D).union(C))
print(A | D)
print(A.intersection(D).intersection(C))
print(A & D & C)
print(D.difference(A))
print(D-A-C)