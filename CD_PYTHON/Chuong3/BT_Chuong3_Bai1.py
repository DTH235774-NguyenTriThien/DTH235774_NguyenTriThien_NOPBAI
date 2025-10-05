# Câu 1: Kiểm Tra Năm Nhuần
nam = int(input("Nhập vào một năm: "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")