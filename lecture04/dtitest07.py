id = input("รหัสพนักงาน : ")
name = input("ชื่อพนักงาน : ")
salary =float(input("เงินเดือนปกติของพนักงาน"))

total = salary - (salary * 7 / 100) - 500

print(f'เงินเดือนสุทธิ {total:.2f} บาท ')