number = input("รหัสพนักงาน : ")
name = input("ชื่อพนักงาน : ")
salary = float(input("เงินเดือนพนักงาน : "))
netSalary = salary - (salary *7/100)-500

a = format (float(netSalary),".2f")

print(f'เงินเดือนสุทธิ {netSalary:.2f} บาท ')
print("เงินเดือนสุทธิ {:.2f} บาท". format (netSalary))
print("เงินเดือนสุทธิ" ,a, "บาท")