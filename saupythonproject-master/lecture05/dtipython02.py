#Fuction 1: have paramiter/no return มีอะไรในวงเล็บ/ไม่มีคำสั่ง
#paramiter คือ ตัวแปร(varible) มีหน้าที่เก็บข้อมูล
def funcA(x,y):
    print("AAA")
    z = x + y
    print(f"{x} + {y} = {z}")

def funcB(x,y,z):
    print("{:.2f} {:.4f} {:.5f}".format(x,y,z))    

funcA(10 , 20) #ข้อมูลที่ส่งให้ paramrter เรียก argument
funcA(5 , 10)
funcB(1, 5 , 10)