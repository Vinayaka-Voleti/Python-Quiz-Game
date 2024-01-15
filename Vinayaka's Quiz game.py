with open("C:\QuizScore.txt","w") as f:
    f.writelines("('Game','GameResult')\n")
    f.close()
from tkinter import *
from tkinter import messagebox
import random
import mysql.connector
#MySQL
mydb = mysql.connector.connect(host='localhost',user='root',passwd=' ',database='quickquiz')
mc = mydb.cursor()
#mc.execute("CREATE DATABASE  IF NOT EXISTS  quickquiz;")
#mc.execute("USE quickquiz;")
#mc.execute("CREATE TABLE IF NOT EXISTS GAME_LOG (Game CHAR (5) ,Result VARCHAR (20) );")
#mc.execute("DROP TABLE GAME_LOG;")
#mc.execute("CREATE TABLE IF NOT EXISTS GAME_LOG (Game CHAR (5),Result VARCHAR (20) );")
gp = 0
p1w = 0
p2w = 0
#Questions
cs = [
    "Who invented Python?",
      "How many bits are there in a byte?",
      """Which function would you choose to remove an
element from a list, given that you know its index? """,
      "Are lists immutable?",
      "Are tuples mutable?",
      "Are strings mutable?",
      "Is 4!=2*2//2(5%3) True?",
    "Can i add a string to an integer directly?",
    "Bool(0) gives False as the output",
    "Key is unique in dictionary",
    "Python is an object oriented language",
    "append() can add multiple values to a list",
    "We can not define our own functions in python",
    "We can read and write in text files using python"
      ]
#Answers
ans2= [
    [
        "Guido Van Rossum",
        "Rajiv Talwar",
        "Elon Musk",
        "Jagdish Bhagat"
     ],
       [
           "4",
           "69",
           "420",
           "None of the above"
           ],
       [
           "pop()",
           "mom()",
           "remove()",
           "expell()"
           ],
       [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
       [
           "Yes",
           "No",
           "Who knows?",
           "All the above"
           ],
       [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
       [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
    [
        "No",
        "Yes",
        "Who knows?",
        "All the above"
        ],
    [
        "Yes",
        "No",
        "Who knows?",
        "All the above"
        ],
    [
        "Yes",
        "No",
        "Who knows?",
        "All the above"
        ],
    [
           "Yes",
           "No",
           "Who knows?",
           "All the above"
           ],
    [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
    [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
    [
           "Yes",
           "No",
           "Who knows?",
           "All the above"
           ]
       ]
ans= [
    [
        "Guido Van Rossum",
        "Rajiv Talwar",
        "Elon Musk",
        "Jagdish Bhagat"
     ],
       [
           "4",
           "69",
           "420",
           "None of the above"
           ],
       [
           "pop()",
           "mom()",
           "remove()",
           "expell()"
           ],
       [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
       [
           "Yes",
           "No",
           "Who knows?",
           "All the above"
           ],
       [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
       [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
    [
        "No",
        "Yes",
        "Who knows?",
        "All the above"
        ],
    [
        "Yes",
        "No",
        "Who knows?",
        "All the above"
        ],
    [
        "Yes",
        "No",
        "Who knows?",
        "All the above"
        ],
    [
           "Yes",
           "No",
           "Who knows?",
           "All the above"
           ],
    [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
    [
           "No",
           "Yes",
           "Who knows?",
           "All the above"
           ],
    [
           "Yes",
           "No",
           "Who knows?",
           "All the above"
           ]
       ]
r = Tk()
r.attributes('-fullscreen',True)
r.configure(bg = "yellow")
q = Label(r,text = "2-Player Quiz game ",font = ("Script MT Bold",100,"italic","bold",),fg = "black",bg = "yellow")
p = Button(r,text = "PLAY ",font = ("Courier New",25,"italic"),borderwidth=0,bg = "orange",activebackground = "orange")
how = Button(r,text = "WORK DONE BY ",font = ("Courier New",25,"italic"),borderwidth=0,bg = "white",activebackground = "orange")
onescore = 0
twoscore = 0
btmm = Button(r, text = "Main Menu ",font = ("Courier New",20), bg = "black",fg="white",activebackground = "light blue")
ext = Button(r, text = "Exit ",font = ("Courier New",20), bg = "black",fg="white",activebackground = "light blue")
p1l = Label(r,text = "Player1 score ",font = ("Courier New",25,"italic","bold",),fg = "white",bg = "red")
p2l = Label(r,text = "Player2 score ",font = ("Courier New",25,"italic","bold",),fg = "white",bg = "red")
turn = Label(r,text = "PLAYER 1 TURN ",font = ("Courier New",50,"italic","bold",),fg = "white",bg = "red")
ones = Label(r,text = str(onescore)+" ",font = ("Courier New",100,"italic","bold",),fg = "white",bg = "red")
twos = Label(r,text =str(twoscore)+" ",font = ("Courier New",100,"italic","bold",),fg = "white",bg = "red")
question = Label(r,text = " ",font = ("Courier New",25,"italic","bold",),fg = "white",bg = "red")
opt1 = Button(r,text = " ",font = ("Courier New",25,"italic","bold"),fg="white",bg = "black",activebackground = "white")
opt2 = Button(r,text = " ",font = ("Courier New",25,"italic","bold"),fg="white",bg = "black",activebackground = "white")
opt3 = Button(r,text = " ",font = ("Courier New",25,"italic","bold"),fg="white",bg = "black",activebackground = "white")
opt4 = Button(r,text = " ",font = ("Courier New",25,"italic","bold"),fg="white",bg = "black",activebackground = "white")
p1w=Label(r,text = "PLAYER1 WON ",font = ("Courier New",100,"italic","bold",),fg = "white",bg = "red")
p2w=Label(r,text = "PLAYER2 WON ",font = ("Courier New",100,"italic","bold",),fg = "white",bg = "red")
draw = Label(r,text = "DRAW ",font = ("Courier New",100,"italic","bold",),fg = "white",bg = "red")
vinny = Label(r,text = "Vinayaka Vamsi Kiran Voleti ",font = ("Courier New",50,"italic","bold",),fg = "white",bg = "red")
back = Button(r,text = "Back",font = ("Maiandra GD",25,"italic"),bg = "black",fg = "white",activebackground = "light blue")
m = [
    p,
     q,
     how,
    ext
     ]
gam = [
    p1l,
    p2l,
    turn,
    ones,
    twos,
    question,
    opt1,
    opt2,
    opt3,
    opt4
    ]
def vvk():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    for i in r.winfo_children():
        i.place_forget()
    vinny.place(x=100,y=200)
    back.place(x=500,y=400)
def letsgo():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    q.place(x = 100,y=100)
    p.place(x= 450,y= 300)
    how.place(x=555,y=300)
    ext.place(x=500,y=400)
def bck():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    for i in r.winfo_children():
        i.place_forget()
    letsgo()
def endscreen():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    for i in r.winfo_children():
        i.place_forget()
        ones.place(x = 10,y=100)
        twos.place(x=1100,y=100)
        p1l.place(x=10,y=250)
        p2l.place(x=980,y=250)
    if int(ones['text'])>int(twos['text']):
        p1w.place(x=200,y=300)
        #mc.execute("INSERT INTO game_log VALUES('GAME','PLAYER1 WON');")
        with open("C:\QuizScore.txt","w") as f:
            f.writelines("('GAME','PLAYER1 WON')")
            #mydb.commit()
    elif int(ones['text'])<int(twos['text']):
        p2w.place(x=200,y=300)
        #mc.execute("INSERT INTO game_log VALUES('GAME','PLAYER2 WON');")
        with open("C:\QuizScore.txt","w") as f:
            f.writelines("('GAME','PLAYER2 WON')")
            #mydb.commit()
    else:
        draw.place(x=500,y=300)
        #mc.execute("INSERT INTO game_log VALUES('GAME','DRAW');")
        with open("C:\QuizScore.txt","w") as f:
            f.writelines("('GAME','DRAW')")
            #mydb.commit()
    ext.place(x=500,y=500)
def strtgm():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    if len(cs) == 0:
        endscreen()
    else:
        for i in m:
            i.place_forget()
        ones.place(x = 10,y=100)
        twos.place(x=1100,y=100)
        p1l.place(x=10,y=250)
        p2l.place(x=980,y=250)
        turn.place(x=350,y=100)
        qn= random.choice(cs)
        question['text'] = qn
        for i in range(len(cs)):
            if cs[i] == qn:
                answr = ans[i]
                rndm = random.choice(answr)
                opt1['text'] = rndm
                answr.remove(rndm)
                rndm = random.choice(answr)
                opt2['text'] = rndm
                answr.remove(rndm)
                rndm = random.choice(answr)
                opt3['text'] = rndm
                answr.remove(rndm)
                opt4['text'] = answr[0]
        question.place(x=10,y=375)
        opt1.place(x=10,y=475)
        opt2.place(x=800,y=475)
        opt3.place(x=10,y=575)
        opt4.place(x=800,y=575)
def optn1():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    qn = question['text']
    for i in cs:
        z=cs.index(i)
        if cs[z] == qn:
            anslst = ans2[z]
            onescore = int(ones['text'])
            twoscore = int(twos['text'])
            if opt1['text'] == anslst[0]:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore+=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore+=1
                    twos['text'] = str(twoscore)+" "
            else:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore-=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore-=1
                    twos['text'] = str(twoscore)+" "
            if turn['text'] == "PLAYER 1 TURN ":
                turn['text'] = "PLAYER 2 TURN "
            else:
                turn['text'] = "PLAYER 1 TURN "
            cs.pop(z)
            ans.pop(z)
            ans2.pop(z)
            strtgm()
def optn2():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    qn = question['text']
    for i in cs:
        z=cs.index(i)
        if cs[z] == qn:
            anslst = ans2[z]
            onescore = int(ones['text'])
            twoscore = int(twos['text'])
            if opt2['text'] == anslst[0]:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore+=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore+=1
                    twos['text'] = str(twoscore)+" "
            else:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore-=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore-=1
                    twos['text'] = str(twoscore)+" "
            if turn['text'] == "PLAYER 1 TURN ":
                turn['text'] = "PLAYER 2 TURN "
            else:
                turn['text'] = "PLAYER 1 TURN "
            cs.pop(z)
            ans.pop(z)
            ans2.pop(z)
            strtgm()
def optn3():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    qn = question['text']
    for i in cs:
        z=cs.index(i)
        if cs[z] == qn:
            anslst = ans2[z]
            onescore = int(ones['text'])
            twoscore = int(twos['text'])
            if opt3['text'] == anslst[0]:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore+=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore+=1
                    twos['text'] = str(twoscore)+" "
            else:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore-=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore-=1
                    twos['text'] = str(twoscore)+" "
            if turn['text'] == "PLAYER 1 TURN ":
                turn['text'] = "PLAYER 2 TURN "
            else:
                turn['text'] = "PLAYER 1 TURN "
            cs.pop(z)
            ans.pop(z)
            ans2.pop(z)
            strtgm()
def optn4():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    qn = question['text']
    for i in cs:
        z=cs.index(i)
        if cs[z] == qn:
            anslst = ans2[z]
            onescore = int(ones['text'])
            twoscore = int(twos['text'])
            if opt4['text'] == anslst[0]:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore+=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore+=1
                    twos['text'] = str(twoscore)+" "
            else:
                if turn['text'] == "PLAYER 1 TURN ":
                    onescore-=1
                    ones['text'] = str(onescore)+" "
                else:
                    twoscore-=1
                    twos['text'] = str(twoscore)+" "
            if turn['text'] == "PLAYER 1 TURN ":
                turn['text'] = "PLAYER 2 TURN "
            else:
                turn['text'] = "PLAYER 1 TURN "
            cs.pop(z)
            ans.pop(z)
            ans2.pop(z)
            strtgm()
def exitt():
    global cs
    global ans
    global ans2
    global onescore
    global twoscore
    ans = messagebox.askyesno(title=None,message="Do you really want to leave?")
    if ans == True:
        r.destroy()
how.configure(command = vvk)
back.configure(command = bck)
ext.configure(command = exitt)
opt1.configure(command = optn1)
opt2.configure(command = optn2)
opt3.configure(command = optn3)
opt4.configure(command = optn4)
p.configure(command = strtgm)
letsgo()
r.mainloop()
