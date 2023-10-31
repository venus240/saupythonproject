#คำนวณเงินที่จะแชร์ ป้อนเงิน ป้อนคน แล้วคำนวณและแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชัน ขอ 2 ฟังก์ชัน

#รับค่าข้อมูล คือ input
#float แปลงให้เป็นตัวเลข
#int = ใฃ้กับตัวเลขที่ไม่มีทศนิยม

def input_moneyPS():
    money = float(input("ป้อนเงิน : "))
    person = int(input("ป้อนคน : "))
    return money,person


#คำนวณ แล้วแสดงผลออกมา
def calandShow_MS(money, person): 
    a = format (float(money),".2f")

    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น
    print(f" จำนวนเงิน {money:.2f} บาท คน {person:.2f} คน แชร์กันคนละ {round(float(money/person))} บาท ")
    print("จำนวนเงิน" ,a, "บาท คน" ,person, "คน แชร์กันคนละ" ,round(float(money/person)), "บาท") #ใช้ ,
    print("จำนวนเงิน" +str(a)+ "บาท คน" +str(person)+ "คน แชร์กันคนละ" +str(round(float(money/person)))+ "บาท" ) #ใช้ +
    print("จำนวนเงิน {:.2f} บาท คน {} คน แชร์กันคนละ {} บาท" .format(money,person,(round(float(money/person))))) #ใช้ . format
    print("จำนวนเงิน %.2F บาท คน %d คน แชร์กันคนละ  %d บาท "%(money, person , money/person)) #ใช้ %

money, person = input_moneyPS()

calandShow_MS(money, person)