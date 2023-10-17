name = input("ป้อนชื่อสินค้า : ")
price = float(input("ป้อนราคาขายสินค้า : "))
sell = (price + price) *10/100

sellV2 = format(float(sell),".2f")

print(f'ราคาขายสินค้า {sellV2} บาท ราคาต้นทุน {price:.2f} บาท ')
print ("ฃื่อสินค้า",name, "ราคาขายสินค้า" ,sellV2,"บาท ราคาต้นทุน ",sellV2,"บาท")
print ("ฃื่อสินค้า"+str(name) + "ราคาขายสินค้า"+ str(sellV2) +"บาท ราคาต้นทุน "+str(sellV2) +"บาท")
print ("ฃื่อสินค้า {} ราคาขายสินค้า {:.2f} บาท ราคาต้นทุน {:.2f} บาท" .format(name,price,sell))