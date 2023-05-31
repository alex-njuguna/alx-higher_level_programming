from oop_encapsulation import A

x = A()
print(x.pub + ' and my value can be changed')
print(x._prot + ' can i be changed?')
x._prot = 'can my value be channged'
print(x._prot)
print(x.__priv)
