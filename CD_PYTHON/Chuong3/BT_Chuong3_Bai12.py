# Câu 12: Xuất bảng cửu chương từ 2 đến 9

for i in range(1, 11):
    for j in range(2, 10):
        print(f"{j}*{i:2} = {j*i:2}", end="\t")
    print()