#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Fibonaccinin ilk n terimi icin n = "))
A = 0 
print(A,end= " ")
B = 1
print(B,end= " ")
for i in range(n - 1):
    F = A + B
    print(F,end=" ")
    A = B
    B = F


# In[3]:


p = 0
n = 0
s = 0
for i in range(10):
    sayi = int(input("Sayıyı Giriniz = "))
    if sayi > 0:
        p = p + 1
    else:
        if sayi < 0 :
            n = n + 1
        else:
            s = s + 1
print("p=", p)
print("n=", n)
print("s=", s)


# In[4]:


se = int(input("Serinin İlk Elemanı = "))
te = int(input("Toplam Eleman Sayısı = "))
ad = int(input("Artış Değeri = "))
ss = se
top = se
for i in range(te - 1):
    top = top + ad
    ss = ss + top
print(ss, end=" ")


# In[6]:


se = int(input("Serinin İlk Elemanı = "))
te = int(input("Toplam Eleman = "))
ad = int(input("Artış Değeri = "))
ss = se
top = se
print(top , end= " + ")
for i in range(te - 1):
    top = top + ad
    ss = ss + top
    if i == te - 2:
        print(top,end="=")
    else:
        print(top,end="+")
print(ss)


# In[1]:


c = 0 
x = -10
while x <=10:
    f = x**2 - 2*x - 3
    print("x=",x,"   f=",f)
    if f == 0:
        c= c + 1
    x = x + 1
print("x eksenini",c ,"Noktada kesiyor")


# In[ ]:




