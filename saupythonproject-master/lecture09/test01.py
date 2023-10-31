class DtiTest01 :
    pass

class DtiTest02 :
    # data/attribute/property/fleid คือ ส่นแบ่งประเภทฟนึ่ง
    infoA = ''
    infoB = 20

    # method คือ ฟังก์ชันประเภทหนึ่ง
    def showHi(self) :
        print('Hi...')

    def showInfoAandB(self) :
        print(self.InfoA)
        print(self.InfoB)

# สร้าง object 
objA = DtiTest02()
objB = DtiTest02()
sombat = DtiTest02()

objA.infoA = 'xxx'
objB.infoB = 100
print(objA.infoB + objB.infoB)

sombat.showInfoAandB()