# Exercise input()


"""
1. เขียนโปรแกรมรับค่าตัวเลขจำนวนเต็ม 3 จำนวน จากนั้นนำตัวเลขทั้งหมดมาบวก
รวมกัน และแสดงผลทางหน้าจอภาพ
"""
# x,y,z = [int(x) for x in input("enter 3 integer: ").split()]
# print(f'Summation is {x+y+z}')
"""
2. เขียนโปรแกรมรับค่าข้อมูลจำนวนเต็มแบบไม่จำกัดจำนวน เก็บไว้ใน list ชื่อ mynum 
จากนั้น นำข้อมูลทั้งหมดใน mynum มาบวกรวมกัน แสดงผลทางหน้าจอภาพ
"""
# mynum = [int(x) for x in input("enter multi integer: ").split()]
# total = 0
# for x in mynum:
#     total+=x
# print(f'Summation of integer in list is {total}')

"""
3. เขียนโปรแกรมรับค่าข้อมูลจำนวนเต็มแบบไม่จำกัดจำนวน แต่เก็บเฉพาะข้อมูลเลขคู่เท่านั้น 
มาเก็บไว้ใน list ชื่อ myEven  
เช่น input: 10 11 23 14 16 7 20 --> output: 10 14 16 20
"""
myEven = [int(x) for x in input("ente multi integers: ").split()
          if int(x)%2 ==0]
print(f'Even number in myEven list: {myEven}')

