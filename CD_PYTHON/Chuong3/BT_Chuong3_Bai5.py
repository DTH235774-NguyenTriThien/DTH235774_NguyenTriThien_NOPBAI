# Câu 5: Cho biết kết quả xuất ra màn hình với các giá trị khác nhau của i, j, k

def test_case(i, j, k):
    orig = (i, j, k)
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"Với i, j, k ban đầu = {orig} => Kết quả: i = {i}, j = {j}, k = {k}")

# Các trường hợp đề bài yêu cầu
test_case(3, 5, 7)  # (a)
test_case(3, 7, 5)  # (b)
test_case(5, 3, 7)  # (c)
test_case(5, 7, 3)  # (d)
test_case(7, 3, 5)  # (e)