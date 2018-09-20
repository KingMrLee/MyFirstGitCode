'''
MRO
'''

class A():
    pass

class B(A):
    pass

print(A.__mro__)
print(B.__mro__)