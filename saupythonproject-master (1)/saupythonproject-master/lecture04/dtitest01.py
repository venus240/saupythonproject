width = float(input("ป้อนความกว้าง : "))
long = float(input("ป้อนความยาว : "))
high = float(input("ป้อนความสูง : "))
print = (" ............ ")

area = round((long * high * 2 )+(long * width * 2)+(long * long * 2) ) / 5

#คำนวณ
print(f"กล่องสี่เหลี่ยมให้มีความกว้าง{width} ยาว {long} สูง {high} ต้องใช้สีทั้งหมด {area} แกลอน ")
print("กล่องสี่เหลี่ยมให้มีความกว้าง",width,"ยาว",long, "สูง" ,high, "ต้องใช้สีทั้งหมด", area, "แกลอน ")
print("กล่องสี่เหลี่ยมให้มีความกว้าง"+str(width)+ "ยาว" +str(long)+ "สูง" +str(high)+ "ต้องใช้สีทั้งหมด" +str(area)+ "แกลอน ")
print("กล่องสี่เหลี่ยมให้มีความกว้าง {} ยาว {} สูง {} ต้องใช้สีทั้งหมด {} แกลอน ".format(width,long,high,area))


