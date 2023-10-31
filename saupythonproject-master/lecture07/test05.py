# list function@tuple function
#len() นับจำนวน , min(), max()

    #   0   1   2       3       4           5
var1 = [10,20,"hello",True, [111,"wow"], "มานะ"]
    #   -6  -5  -4      -3      -2         -1

        #   0   1   2       3       4           5
var2 = (10,20,"hello",True, (111,"wow"), "มานะ")
    #   -6  -5  -4      -3      -2         -1

print(f'ใน var1 มีข้อมูลทั้งหมด {len(var1)} ข้อมูล ')
print(f'ใน var1 มีข้อมูลทั้งหมด {len(var2)} ข้อมูล ')

#--------------------------------------------------

# min and max ใช้ไม่ได้กับข้อมูลคนละชนิดกัน
#print(min(var1)) error

#min ให้ค่าน้อยสุด max ให้ค่ามากสุด
    # true = 1 false = 0
var3 = [10 , 20, 30, True, 10, 20] 
var4 = (10 , 20, 30, True, 10, 20)
print(min(var3)) #ค่า น้อย สุด
print(max(var4)) #ค่า มาก สุด

