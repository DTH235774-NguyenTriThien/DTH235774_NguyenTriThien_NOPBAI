# Câu 10: Tính dãy số S(x, n) = x + x^2/2! + x^3/3! + ... + x^n/n!

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

s = 0
for i in range(1, n + 1):
    tu = x ** i
    mau = 1
    for j in range(1, i + 1):
        mau *= j
    s += tu / mau

print(f"S({x}, {n}) = {s}")