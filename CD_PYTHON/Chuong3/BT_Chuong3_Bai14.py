# Câu 14: Cho biết bao nhiêu dấu * được in ra trên màn hình

a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1

# Kết luận: Mỗi lần a chạy từ 0 đến 99, b chạy từ 0 đến 39, in ra dấu * nếu (a+b) chẵn.
# Tổng số dấu * được in ra là 2000 (vì mỗi dòng có 20 dấu *, 100 dòng).