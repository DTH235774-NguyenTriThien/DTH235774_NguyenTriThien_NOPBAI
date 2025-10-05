# Câu 4 Hãy cho biết kết quả của Boolean Expression
# Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression
print("(a)", x == 3)                  # True
print("(b)", x < y)                   # True
print("(c)", x >= y)                  # False
print("(d)", x <= y)                  # True
print("(e)", x != y - 2)              # False (3 != 5-2 => 3 != 3 => False)
print("(f)", x < 10)                  # True
print("(g)", x >= 0 and x < 10)       # True (3 >= 0 and 3 < 10)
print("(h)", x < 0 and x < 10)        # False (3 < 0 là False)
print("(i)", x >= 0 and x < 2)        # False (3 < 2 là False)
print("(j)", x < 0 or x < 10)         # True (3 < 10 là True)
print("(k)", x > 0 or x < 10)         # True (3 > 0 là True)
print("(l)", x < 0 or x > 10)         # False (3 < 0 là False, 3 > 10 là False)