# เขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt', 'w',encoding='utf-8') #เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti.write('wow...')
f_dti.write('woo...\n')
f_dti.write('สวัสดีทุกคน...\n')

f_dti.close()

print('บันทึกข้อมูลไฟล์เรียบร้อยแล้ว')


