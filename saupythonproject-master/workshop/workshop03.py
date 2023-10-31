name = input("ชื่อสินค้า : ")
price = float(input("ราคาสินค้า : "))
sell = price * 7 / 100

a = format (float(sell),".2f")

print(f'ภาษีที่คำนวนได้ {sell:.2f} บาท ')
print("ภาษีที่คำนวนได้ {:.2f} บาท". format (sell))
print("ภาษีที่คำนวนได้" ,a, "บาท")
