#โปรแกรมคำนวณหาพื้นที่วง เส้นรอบวงกลม และปริมาตรทรงกลม จากรัศมีที่ป้อนโดยผู็ให้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ขอ 5 ฟังก์ชัน
import math

#inputRadius
def inputRadius() :
    #r = input('ป้อนรัศมี : ')
    #return r

    return float(input('รัศมี : '))
    
#calAreaCircple
def calAreaCircle (r) :
    return math.pi * math.pow(r,2)
#calRoundCircle 2* pi * r
def calRoundCircle (r) :
    return 2 * math.pi * r 
#calCuberdCircle 4/3 * pi * r * r * r
def calvolumeCircle (r) :
    return 4/3 * math.pi * math.pow(r,3)


#showResul ขอทั้งหมดทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลม เส้นรอบวง ปริมาตรทรงกลมเป็น
