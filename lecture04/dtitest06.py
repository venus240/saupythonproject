name = input("ป้อนชื่อสินค้า : ")
price = float(input("ป้อนราคาขายสินค้า : "))
sell = (price + price) *10/100

print(f'ราคาขายสินค้า {sell:.2f} บาท ')
print(f'ราคาต้นทุน {price:.2f} บาท ')

print ("คุณ",name, "ราคาขายสินค้า" ,sell,"บาท ราคาต้นทุน ",price,"บาท")
print ("คุณ"+str(name) + "ราคาขายสินค้า"+ str(sell) +"บาท ราคาต้นทุน "+str(price) +"บาท")
print ("คุณ {} ราคาขายสินค้า {:.2f} บาท ราคาต้นทุน {:.2f} บาท" .format(name,price,sell))
