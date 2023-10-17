# self เปรียบเสมือนสิ่งที่ใช้แทนคลาสตัวเอง เพื่อที่จะสามารเรียกใช้ member ในคลาสตัวเองได้
class Test04 :
    deta1 = 10

    # contructor
    def __init__(self,data2, data3):
        print('Hi...')
        self.data2 = data2
        self.data3 = data3

    # method member
    def showSumData(self):
        print(self.data + self.data2 + self.data3)
        self.showWow()

    def ShoeWow(self):
        print('Wow wow wow...')


objA = Test04(20, 30)
objB = Test04(10, 20)
objC = Test04(20, 100)
objC = Test04(20, 30)