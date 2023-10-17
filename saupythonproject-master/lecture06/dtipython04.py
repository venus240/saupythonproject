#คำสั่ง if-else-if พิสุจน์ตรวจสอบหลายครั้ง (else-if = elif)

score = int( input('ป้อนคะแนน : '))

if score >= 80 :
    print('ได้เกรด A')

elif score >= 70 and score < 80 :
    print('ได้เกรด B')

elif score >= 60 and score < 70 :
    print('ได้เกรด C')

elif score >= 50 and score < 60 :
    print('ได้เกรด D')

#elif score < 50 : (มีif หรือไม่มีก็ได้ elif, else) 
else :
    print('ได้เกรด F')