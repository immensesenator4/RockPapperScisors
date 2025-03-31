from sock import Socket
import os
h=Socket("game",12)
def findspot(str,list):
    for i in range(0,len(list)):
        if list[i]==str:
            return i
    return 0
s=["rock","papper","scisors"]
if input("hosting ye or ne")=="ye":
    h.host()
    conn = None
    while not conn:
        h.sock.listen()
        conn, addr =h.sock.accept()
    while True:
        
        z=None
        while not z:
            y=input("rock papper scisors choose one\n \t->")            
            if y in s or y in "leave":
                z=y
        
        h.send(y,conn)
        if z in "leave":
            break
        data = None
        while not data:
            try:
                data = h.recieve(conn)
            except Exception  as e:
                print(e)
        opp = findspot(data,s)
        if z== s[opp-1]:
            print("you loose")
        elif z == s[opp]:
            print("tie")
        else:
            print("you win")
        input('any button to continue')
        os.system('cls')
    h.ServerClose()
else:
    h.ip=h.getServers()[0]
    h.connectServer(h.ip,h.port)
    while True:
        z=None
        while not z:
            y=input("rock papper scisors choose one\n \t->")
            if y in s or y in "leave":
                z=y
                data = None
        if z in "leave":
            break
        while not data:
            try:
                data = h.recieve(h.sock)
            except:
                pass
        h.send(y)

        opp = findspot(data,s)
        if data == "leave":
            print("temination forced\nConection Lost\nReason :Conection terminated by Host")
            break
        if z== s[opp-1]:
            print("you loose")
        elif z == s[opp]:
            print("tie")
        else:
            print("you win")
        input('any button to continue')
        os.system('cls')
    h.Disconect()