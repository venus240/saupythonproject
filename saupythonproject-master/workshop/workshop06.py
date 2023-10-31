name = input("ป้อนชื่อผู้กู้ : ")
quantity = int(input("จำนวนเงินกู้ : "))


if quantity >= 1000 :
    print(f'อัตราดอกเบี้ย {quantity * 2.5 / 100}บาท ')

else :
    print(f'อัตราดอกเบี้ย {quantity * 5.5 / 100}บาท ')