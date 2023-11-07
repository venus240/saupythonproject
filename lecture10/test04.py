# เขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt', 'a',encoding='utf-8') #เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์

f_dti.write('CCC\n')
f_dti.write('DDDD...\n')


f_dti.close()

print('บันทึกข้อมูลไฟล์เรียบร้อยแล้ว...')