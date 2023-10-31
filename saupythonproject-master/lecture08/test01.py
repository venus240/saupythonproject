#list มีลำดับ
my_list = [10, 20, 10, 'Hi' , True, [20, 'Hello']]
print(my_list)
print(len(my_list))

#Tuple มีลำดับ
my_tuple = (10, 20, 10, 'Hi' , True, (20, 'Hello'))
print(my_tuple)
print(len(my_tuple))

# set เป็นข้อมูลที่ไม่มีลำดับ ข้อมูลที่ซ้ำถือว่าเป็นข้อมูลเดียวกัน
my_set = {10, 20, 10, 'Hi' , True} # se tใน set ไม่ได้ เฃ่น {บลาๆ{}}
print(my_set)
print(len(my_set))

for data in my_set :
    print(data, end='/')

print('------------------------------')

# เปลี่ยน เป็นlist เพื่อแก้ไขข้อมูล {} เป็น []
list_fr_set = list(my_set)
print(list_fr_set)
        # 'Hi' แก้ไขข้อมูล เปลี่ยนจาก Hi เป็น DTI
list_fr_set[0] = 'DTI'

my_set = set(list_fr_set)
print(my_set)

my_set.clear()
print(len(my_set))

my_set1 = {10,20,30,'Hi'}
my_set2 = {10, 'Hello', 'Hi', True}

# เพิ่มข้อมูลไปใน set (โดยไม่ต้องแก้ไข)
my_set1.add(999)
print(my_set1)

# นำข้อมูลออกบางส่วน
my_set1.remove('Hi')
print(my_set1)

# intersec = ข้อมูลที่เหมืิอนกัน (ถ้าข้อมูลไหนเหมือนกันมันก็จะแสดงข้อมูลนั้น)
print(my_set1.intersection(my_set2))

#  union = เอาข้อมุลมารวมกัน
print(my_set1.union(my_set2))

# len , min , max
# len = นับจำนวนข้อมูล
# min = ค่าน้อยสุด
# max = ค่ามากสุด
print(min(my_set2))








