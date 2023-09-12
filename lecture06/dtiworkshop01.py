#โปรแกรมคำนวนหาพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงทางแป้นพิมพ์และแสดงผมพื้นที่สามเหลี่ยมที่คำนวณ

#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น function
#1. รับค่า ฐาน สูง
#2. คำนวณพื้นที่ และแสดงผลออกมา

def inputBaseHigh() :
    base = float(input("ป้อนฐาน : "))
    high = float(input("ป้อนสูง : "))
    return base,high

def calAndShowTriangleArea(base, high) :
    area = base * high /2
    print(f"สามเหลี่ยม {base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f} ")

print(".............................")
print("--*calculate Tringle Area *--")
print(".............................")
base, high = inputBaseHigh()
print(".............................")
calAndShowTriangleArea(base, high)
print(".............................")
