# OOP
class DtiSau :
    stu_name = ' '
    score = 0
    gpa = 0


    def hiStudent(self) :
        print(f'สวัสดี {self.stu_name}')

    def showScoreAndGrade(self):
        print(f'คะแนน {self.score}  ได้ GTA : {self.gpa}')


# สร้าง object
obj01 = DtiSau() #ชื่อคลาสที่มี () เราเรียกว่าเป็นการสั่งให้ contructor ของคลาสทำงาน
obj02 = DtiSau() 

obj01.stu_name = 'สมชาย'
obj01.hiStudent()

obj02.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = '3.99'




    
    