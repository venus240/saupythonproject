#Slicing data in list and Tuple

    #   0   1   2       3       4           5
var1 = [10,20,"hello",True, [111,"wow"], "มานะ"]

var2 = (10,20,"hello",True, (111,"wow"), "มานะ")
#20,"Hello",True
print(var1[1:4])

#True,(111,"wow")
print(var2[3:5])

#10,20,"Hello"
print(var1[:3])

# 'Hello', True, [111,"Wow"] , 'มานะ'
print(var1[2:])