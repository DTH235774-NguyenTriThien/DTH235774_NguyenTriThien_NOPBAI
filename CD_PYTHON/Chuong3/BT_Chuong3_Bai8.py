# Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’. Xuất kết quả đúng phép toán

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Không thể chia cho 0!")
else:
    print("Phép toán không hợp lệ!")