emp_name = input("ป้อนชื่อพนักกงาน : ")
sale_price = float(input("ป้อนยอดขาย : "))
print('------------------')
commission = float(sale_price) * 10/100
s = format(float(sale_price),".2f")
a = format(float(commission),".2f")
print(f"คุณ {emp_name} ยอดขาย {sale_price:.2f} บาท ได้ค่าคอม {commission:.2f} บาท")

print("คุณ",emp_name,"ยอดขาย",s,"บาท ได้ค่าคอม",a,"บาท")

print("คุณ" +str(emp_name) +"ยอดขาย" +str(s) +"บาท ได้ค่าคอม" +str(a)+"บาท")

print("คุณ {} ยอดขาย {:.2f} บาท ได้ค่าคอม {:.2f} บาท" . format(emp_name,sale_price,commission))