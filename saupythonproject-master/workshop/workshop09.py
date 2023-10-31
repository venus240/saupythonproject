number = input("ป้อนรหัสพนักงาน : ")
name = input("ชื่อพนักงาน : ")
Amountofmoney = float(input("ป้อนจำนวนเงินพนักงาน : "))

if Amountofmoney <= 1000 :
    print('ค่าคอมมิชชั่น 0.0 บาท')

elif Amountofmoney >= 1001 and Amountofmoney <= 2000:
    print('ค่าคอมมิชชั่น 1% จากยอดขาย')

elif Amountofmoney >= 2001 and Amountofmoney <= 3000:
    print('ค่าคอมมิชชั่น 3% จากยอดขาย')

elif Amountofmoney >= 3001 :
    print('ค่าคอมมิชชั่น 5% จากยอดขาย')
