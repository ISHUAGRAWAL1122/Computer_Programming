import random
while True:
    q=input("Do you want to play tic-tac-toe(y/n): ")
    if q=="y" or q=="Y":
        print()
        print('!!! These are the positions for placing your respective ( X / O ) sign !!!')
        print()
        print(' 1 | 2 | 3 ')
        print('---+---+---')
        print(' 4 | 5 | 6 ')
        print('---+---+---')
        print(' 7 | 8 | 9 ')
        print()
        r=[]
        l1=[' ',' ',' ']
        l2=[' ',' ',' ']
        l3=[' ',' ',' ']
        rs=random.randint(0,1)
        if rs==0:
            s1="X"
            s2="O"
            print("Player 1 sign is ",s1)
            print("Player 2 sign is ",s2)
        else:
            s1="O"
            s2="X"
            print("Player 1 sign is ",s1)
            print("Player 2 sign is ",s2)
        print()
        print(f' {l1[0]} | {l1[1]} | {l1[2]} ')
        print('---+---+---')
        print(f' {l2[0]} | {l2[1]} | {l2[2]} ')
        print('---+---+---')
        print(f' {l3[0]} | {l3[1]} | {l3[2]} ')
        print()
        def c_p(p,s):
            if p==1 or p==2 or p==3 :
                l1[p-1]=s
            elif p==4 or p==5 or p==6 :
                l2[p-4]=s
            elif p==7 or p==8 or p==9 :
                l3[p-7]=s
            print(f' {l1[0]} | {l1[1]} | {l1[2]} ')
            print('---+---+---')
            print(f' {l2[0]} | {l2[1]} | {l2[2]} ')
            print('---+---+---')
            print(f' {l3[0]} | {l3[1]} | {l3[2]} ')
            print()
        def c_win(w_p,s):
            if l1[0]==l1[1]==l1[2]==s or l1[2]==l2[2]==l3[2]==s or l3[0]==l3[1]==l3[2]==s\
               or l1[0]==l2[0]==l3[0]==s or l2[0]==l2[1]==l2[2]==s or l1[0]==l2[1]==l3[2]==s\
               or l1[2]==l2[1]==l3[0]==s or l1[1]==l2[1]==l3[1]==s:
                print(f'Hurray! Player {w_p} Win the Match\n')
                return False
            else:
                return True
        w=True
        while w:
            p1=input("player 1 enter your position (0-9) : ")
            if p1!="" and 48<ord(p1)<58:
                p1=int(p1)
                if p1 not in r:
                    r.append(p1)
                    c_p(p1,s1)
                else:
                    print("!!! POSITION OCCUPIED !!!")
                    continue
            w=c_win(1,s1)
            if len(r)<9:
                while w==True:
                    p2=input("player 2 enter your position (0-9) : ")
                    if p2!="" and 48<ord(p2)<58:
                        p2=int(p2)
                        if p2 not in r:
                            r.append(p2)
                            c_p(p2,s2)
                            w=c_win(2,s2)
                            break
                        else:
                            print("!!! POSITION OCCUPIED !!!")
                            continue
            else:
                print("!!! Try Again !!!")
                w=False
    elif q=="n" or q=="N":
        break
    else:
        print("Please enter correct choice (y/n) ")
