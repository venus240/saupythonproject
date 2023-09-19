name = input("ป้อนชื่อหัวหน้ากรุ๊ป : ")
number = input("เบอร์ติดต่อกลับของหัวหน้ากรุ๊ป : ")
quantity = int(input("จำนวนคนที่จะไปทัวร์ : "))

if quantity <= 2 :
    print('คิดแพ็กเกจละ 300 บาทต่อคน')

elif quantity >= 3 and quantity <= 5:
    print('คิดแพ็กเกจละ 250 บาทต่อคน')

elif quantity >= 6 and quantity <= 10 :
    print('คิดแพ็กเกจละ 210 บาทต่อคน')

elif quantity >= 11 :
    print('คิดแพ็กเกจละ 150 บาทต่อคน')

