# Name Isam Zia Roll no: TRN-2026-00346 


a = [1, 2, 3]

b = a
b.append(4)

# Prediction: a will contain [1, 2, 3, 4]
print("a after modifying b:", a)

c = a.copy()
c.append(5)

# Prediction:
# a = [1, 2, 3, 4]
# c = [1, 2, 3, 4, 5]
print("a:", a)
print("c:", c)

print("a is b:", a is b)
print("a is c:", a is c)
print("a == a[:]:", a == a[:])
