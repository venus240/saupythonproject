#คำสั่ง return ที่ไท่ทีอะไรต่อท้าย หมายถึง เป็นการบ่งบอกว่าการทำงานนั้นๆ ว่าเสร็จแล้ว
def example() :
    print(111)
    print(222)
    return
    print(3333)
    print(4444)




#default Parameter มีการกำหนดค่าเริ่มต้นให้พารามิเตอร์
def dtiTest( x, y ,z = 20, a = 10):
    print(f"{x} + {y} + {z} + {a} = {x+y+a}")

dtiTest(5, 100)

dtiTest(9, 8, 10)