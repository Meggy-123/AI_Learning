import torch


# 创建Tensor

x = torch.tensor([
    [1,2,3],
    [4,5,6]
])


print("Tensor:")
print(x)


print("Shape:")
print(x.shape)



# Tensor计算

y = torch.ones(2,3)


print("x+y:")
print(x+y)



# 矩阵乘法

a = torch.randn(3,2)

b = torch.randn(2,4)


c = torch.matmul(a,b)


print("Matrix result:")
print(c)


print("Result shape:")
print(c.shape)