# Câu 6: Đọc số n có tối đa 2 chữ số

n = int(input("Nhập số n (tối đa 2 chữ số): "))

don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

if n < 0 or n > 99:
    print("Vui lòng nhập số từ 0 đến 99.")
elif n == 0:
    print("Không")
elif n < 10:
    print(don_vi[n].capitalize())
else:
    chuc = n // 10
    dv = n % 10
    if chuc == 1:
        if dv == 0:
            print("Mười")
        elif dv == 5:
            print("Mười lăm")
        else:
            print("Mười", don_vi[dv])
    else:
        if dv == 0:
            print(hang_chuc[chuc].capitalize())
        elif dv == 1:
            print(hang_chuc[chuc].capitalize(), "mốt")
        elif dv == 5:
            print(hang_chuc[chuc].capitalize(), "lăm")
        else:
            print(hang_chuc[chuc].capitalize(), don_vi[dv])