# cmd=''
# while cmd!='stop':
#     cmd=input('Enter command: ')
#     print(cmd)
# r=range(10)
# r=range(10,30)
# r=range(10,30,5)
# print(*r)
# word='Vladimir'
#
# for char in word:
#print(char)
# import cv2
# img=cv2.imread('../i.jpeg')
# print(type(img))
# for i in range(10):
#     print('Hello World')
#     print(i)
#
# for i in range(1280):
#     for j in range(720):
#         for k in range(3):
#             print(img[i,j,k])
l=[1,2,3,7,3,5,3,4]
print(l.append(12))
print(l)
print(l.count(3))
l.clear()
print(l)
t=(1,2,3,-7,3,-5,-3,4)
print(t)
i=t.index(3)
print(i)
valid=[]
for item in t:
    if item <0:
        valid.append(item)
print(tuple(valid))