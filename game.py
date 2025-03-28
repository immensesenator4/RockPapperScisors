from sock import Socket
import os
h=Socket("game",12)
def findspot(str,list):
    for i in range(0,len(list)):
        if list[i]==str:
            return i
        
s=["rock","papper","scisors","leave"]
if input("hosting ye or ne")=="ye":
    h.host()
    conn = None
    while not conn:
        h.sock.listen()
        conn, addr =h.sock.accept()
    while True:
        
        z=None
        while not z:
            y=input("rock papper scisors choose")
            if y in s :
                z=y
        if z in "leave":
            break
        h.send(y,conn)
        
        data = None
        while not data:
            try:
                data = h.recieve(conn)
            except Exception  as e:
                print(e)
        opp = findspot(data,s)
        if z== s[opp-1]:
            print("you loose")
        elif z == data:
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
            y=input("rock papper scisors choose")
            if y in s :
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
        if z== s[opp-1]:
            print("you loose")
        elif z == data:
            print("tie")
        else:
            print("you win")
        input('any button to continue')
        os.system('cls')
    h.Disconect()