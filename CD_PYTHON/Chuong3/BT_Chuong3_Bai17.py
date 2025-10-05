# Câu 17: Viết lại code dùng break thay cho biến done

n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n =", n)