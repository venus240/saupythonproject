Name = input("ป้อนชื่อจังหวัด : ")
Ph = float(input("ป้อนค่าPH : "))

if Ph >= 7 and Ph <= 8 :
    print('Result is Normal')

elif Ph >8 :
    print('Result is Acid')

elif Ph <7 :
    print('Result is Alkali')

