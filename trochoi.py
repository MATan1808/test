##trò chơi con rong thap canh
##randit() tao so ngau nhien
import random
print ("bat dau tro choi nao")
begin=input ("nhan 1 de bat dau ")
if begin=="1":
    print("                                           Let'go with me       ")
    print("____cung toi kham pha tro choi nao____")
    print(" -ban dang vao lau dai co rong va- + - lau dai co ca kho bau-")
    playerChoice = input(" hay chon tu 1 --> 4")
    if playerChoice =="1":
        print(" ban da tim thay kho bau  ")
        print (" chuc mung ban da thanh cong vuot qua nhung ngoai vat")
        print (" ban muon choi lai thi hay khoi dong choi lai nhe ")
    elif playerChoice == "2":
        print("  oi khong ! . co con da phun lua vao mat ban")
        print( "                            ------BAN DA DIE------")
    elif playerChoice == "3":
        print("  oi khong !!!!!!!!!!!!!!!!!!! ban da buoc vao cho co khi doc va dang bi bat tinh ")
        print("                             -------BAN DA DIE------")
    elif playerChoice =="4":
        print ("can phong nay dang co 2 cua ")
        number=int(input("ban chon so nao?"))
        if number == random.randint(1,2):
            print("cua dung ",random.randint(1,2))
            print("nguoi chon",number)
            print("nguoi da chon dung cua va co the thoat ra ngoai ")
            print("nguoi hay su dung kho bao do vao muc dich chinh dang nhe")
        else:
            print("cua dung ",random.randint(1,2))
            print("nguoi chon",number)
            print (" nguoi da chon sai bay gio ta se bat nguoi choi lai tu dau !!!! ")
            print("                             tam biet nguoi !!!!!!!!!!!!!!")
    else:
        print("hay lua chon 1 --> 3 ")
else:
    print (" hay go 1 de bat dau tro choi ")
    

