#การเขียนโค้ดแก้ เราอยากให้เข้าใส่แค่ตัวเลข ถ้าข้อมูลไม่ถูกต้อง
try :   
    num1 = int(input ("Input number 1 : "))
    num2 = int(input ("Input number 2 : "))

    result1 = num1 * num2
    result2 = num1 / num2

    print(f'{num1} x {num2} = {result1}')
    print(f'{num1} / {num2} = {result2}')
    #การดักจับต้องรู้ชื่อชอง error
except ValueError :
    print("ตรวจสอบการป้อนข้อมูล ป้อนได้แต่ตัวเลขเท่านัน้")
except ZeroDivisionError :
    print("ตรวจสอบการป้อนข้อมูล ตัวเลขตัวที่ 2 ห้ามเป็น 0 นะจุ๊")
except Exception :
    print/("มีข้อผิดพลาดเกิดขึ้น กรุณาติดต่อ 0651234587 ทีม IT")

finally :
    print('thank you na kub')