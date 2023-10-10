#list Method
var1 = [10,20,"hello",True, [111,"wow"], "มานะ"]
# append เพิ่ม 1 ข้อมูล
var1.append((555))
var1.append(["Hi","Hey",999])
print(var1)
#extend เพิ่มแต่ละข้อมุล
var1.extend([10,20,30])
print(var1)

# remove ลบข้อมูล
var1.remove("hello")
var1.remove(10)
print(var1)

var2 =[10,20,"Hello"]

# insert แทรกข้อมูล
var2.insert(2,"Hi")
print(var2)

#pop 
var2.pop()
print(var2) #[10,20,"Hi"]
var2.pop(1)
print(var2)

#index
print(var2.index("Hi"))

#count นับจำนวน ข้อมูลนั้นๆที่ซ้ำที่อยู่ใน list นั้นว่ามีกี่ตัว
print(var1.count(10))
var3 = [10,10,20, "Hi",10,"Hi"]
print(f'ใน var3 มี 10 ทั้งหมด {var3.count(10)}ตัว')
print(f'ใน var3 มี Hi ทั้งหมด {var3.count("Hi")}ตัว')
# เมธอตต่อไปนี้ใช้ได้เฉพาะข้อมู,ในที่เป็นประเภทเดียวกันเท่านั้น

#sort จักเรียง ข้อมูลใน list ต้องเหมือนกันทั้งหมด
var4 = [[10,10,20, "Hi",10,"Hi"]]
#ver.sort() Error

var5 = [99,34,635, 45610,99]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)