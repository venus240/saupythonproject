#คำสั่ง break กับ continue ที่มักใช้ร่วมกับ control flow
for x in range(5) :
    if x == 3 :
        break; #break ทำงานเมื่อไหร่ จบ loop ทันที
    print(f"SAU...{x}")

print("+++++++++++++")

for y in range(5) :
    if y == 3 :
        continue; # continue ทำงานเมื่อไหร่จบรอบนั้น ไปรอบต่อไปทันที
    print(f"DTI...{y}")