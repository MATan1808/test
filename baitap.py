print(" TÂN MA  ")
print ()
"""
aliens=2
password="TANDEPTRAI"
nhap=input("nhap mat khau :").upper()
#upper(): la doi thuong thanh hoa
while nhap != password:
    print()
    print("mat khau sai roi !!!!")
    print()
    aliens=aliens ** 2
    print(" co", aliens, "nguoi ngoai hanh tinh ")
    if aliens > 7400000000:
        break
    print ()
    print ("nhap lai mat khau ")
    print()
    nhap=input("nhap mat khau :").upper()
    if aliens > 7400000000:
        print (" thua !")
    else :
        print("dung mat khau")
"""
#tro choi du doan
import random
number= random.randint(1,20)
nhap=int(input("nhap so ban chon"))
while nhap !=number:
    if nhap < number:
        print("so ban chon qua nho")
    else :
        print("so ban chon qua lon ")
    nhap=int(input("nhap lai...."))
print ("so tui chon ",nhap)
print ()
print("so may chon",number)
print("chuc mung ban doan dung !!!")



                                                                 
