import numpy as np

# _A is array 
# A is list
_A = [
  # 0,1,2 
   [1,2,3], # 0
   [4,5,6], # 1
   [7,8,9], # 2
]
a = np.array(_A)
print('a[0,0]:' ,a[0,0])
print('a[:,0]:' ,a[:,0]) #lấy tất cả giá trị ở cột thứ 2
print('a[0,:]:' ,a[0,:]) # lấy tất cả giá trị ở hàng thứ 2
_A = [1,2,3] 
a = np.array(_A)
print(a)

# khi + hoac - thi 2 ma tran phai cung kich thuoc
_A = [[1,2,3],[4,5,6],[7,8,9]]
_B = [[1,2],[4,5],[7,8]]
A = np.array(_A)
B = np.array(_B)
print("A * B : \n" , A@B)

A = np.eye(5)
print(A)

_A = [[1,2,3], [4,5,6]]
_B = [[7,8,9], [10,11,12]]
A = np.array(_A)
B = np.array(_B)
print(A*B)

a = np.eye(5) # khi trong ma tran co so 1 thi se hien TRUE
print(a == 1)


_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
a_i = np.linalg.pinv(a) #Create inverse of a
print(a_i)
print(a @ a_i)


_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
a_t = np.transpose(a) #Create transpose of a
print(a)
print(a_t)


_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
print(np.size(a, 0)) # số hàng // 0 là tính theo cột
print(np.size(a, 1)) # số cột // 1 tính theo hàng


_a = [ [1, 2, 3],
       [4, 5, 6], 
       [7, 8, 9] ]
a = np.array(_a)
print(np.sum(a, 0))
print(np.max(a))
print(np.min(a, 1))


