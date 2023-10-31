name = input('ชื่อผู้ใช้โทรศัพท์ : ')
number = input('เบอร์โทรศัพท์ : ')
minute = int(input("จำนวนนาทีที่ใช้โทรศัพท์ : "))

if minute <= 15 :
    print('คิดนาทีละ 5 บาท')

elif minute >= 16 and minute <= 30 :
    print('คิดนาทีละ 3 บาท')

elif minute >= 31 :
    print('คิดนาทีละ 1.50 บาท')

