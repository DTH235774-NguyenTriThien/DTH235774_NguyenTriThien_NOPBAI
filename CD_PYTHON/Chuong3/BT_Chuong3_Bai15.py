# Câu 15: Giải thích cách chạy các dòng lệnh range

print("(a)", list(range(5)))           # [0, 1, 2, 3, 4] - từ 0 đến 4, bước 1
print("(b)", list(range(5, 10)))       # [5, 6, 7, 8, 9] - từ 5 đến 9, bước 1
print("(c)", list(range(5, 20, 3)))    # [5, 8, 11, 14, 17] - từ 5 đến <20, bước 3
print("(d)", list(range(20, 5, -1)))   # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6] - từ 20 đến >5, bước -1
print("(e)", list(range(20, 5, -3)))   # [20, 17, 14, 11, 8] - từ 20 đến >5, bước -3
print("(f)", list(range(10, 5)))       # [] - không có số nào vì mặc định bước +1, 10 > 5 nên rỗng
print("(g)", list(range(0)))           # [] - không có số nào
print("(h)", list(range(10, 101, 10))) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] - từ 10 đến 100, bước 10
print("(i)", list(range(10, -1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - từ 10 đến >=0, bước -1
print("(j)", list(range(-3, 4)))       # [-3, -2, -1, 0, 1, 2, 3] - từ -3 đến 3, bước 1
print("(k)", list(range(0, 10, 1)))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - từ 0 đến 9, bước 1

# Giải thích:
# range(start, stop, step) tạo ra dãy số từ start đến nhỏ hơn stop (nếu step > 0) hoặc lớn hơn stop (nếu step < 0), với bước nhảy step.