#list มีลำดับ
my_list = [10, 20, 10, 'Hi' , True, [20, 'Hello'],(10,20),{10,20}]

#Tuple มีลำดับ
my_tuple = (10, 20, 10, 'Hi' , True, (20, 'Hello'),[10,20],{'SAU','DTI'})
print()# ถ้าอยากแสดง DTI ออกมาให้print อะไร

# set เป็นข้อมูลที่ไม่มีลำดับ ข้อมูลที่ซ้ำถือว่าเป็นข้อมูลเดียวกัน
my_set = {10, 20, 10, 'Hi' , True} # se tใน set ไม่ได้ เฃ่น {บลาๆ{}}

                                                                                # key คือ associative = ตัวชี้ที่อ้างอิงไปยัง value
                                                                                # value = ค่าข้อมูลที่สามารถเอาไปใฃ้งาน
# Dictionary {มีวงเล็บเหมือน set} ช้อมูลประกอบด้วย key : Valye / key -> String-Number / Value -> Everthing
my_dict = {'name' : 'สมชาย', 'age':20, 555:999, 'flag':True}
print(my_dict['name'])

        # 1090 = 20 + 555
print(my_dict['age'] + my_dict[555] )
my_dict['name'] = 'สมหญฺิง'

# วิธีเพิ่มข้อมูล
my_dict['major'] = 'DTI'
print(my_dict)

# วิธีเอาข้อมูลออก ต้องระบุคำที่จะออก
my_dict.pop('name')
my_dict.pop(555)
print(my_dict)

# เอาตัวสุดท้ายออก
my_dict.popitem()
print(my_dict)


for data in my_dict :
    print(data, end=' ')

print()

for data in my_dict.keys() :
    print(data, end=' ')

print()

for data in my_dict.values() :
    print(data, end=' ')

my_dict1 = {'a':10, 'b':20, 'c':30}

# ถ้าเปลี่ยนข้อมูล dict1 dict2 ก็จะเปลี่ยนตาม
my_dict2 = my_dict1

# ถ้าเปลี่ยนข้อมูล dict1 .copy จะไม่เปลี่ยนตาม 
my_dict3 = my_dict1.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict2['a'] = 999
my_dict3['a'] = 888

print('++++++++++++++++++++++++++++++++++++')

print(my_dict1)
print(my_dict2)
print(my_dict3)


