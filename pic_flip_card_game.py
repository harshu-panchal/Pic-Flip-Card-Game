from customtkinter import *
from PIL import Image
import random
import pygame
import time


pygame.mixer.init(44100,-16,2,2048)
clk = pygame.mixer.Sound("audio/button-click-71316.mp3")
pygame.mixer.music.load("audio/cute-music-26476.mp3")
pygame.mixer.music.play(-1)


class windows:
    
    def startup_win(self):
        startup=CTkToplevel()
        startup.title("Start")
        startup.minsize(width=400,height=250)
        startup.geometry("400x250+450+100")
        startup.maxsize(width=400,height=250)
        lable = CTkLabel(startup,text="You Have 02:30 Minutes To Complete", font=("chiller",25,"bold"))
        lable.pack(pady=60)
        button = CTkButton(startup,text="Start",font=("chiller",25,"bold"),fg_color="#f70f32",command=startup.destroy)
        button.pack()

    def HighScore_win(self):
        HighScore=CTkToplevel()
        HighScore.title("High Score")
        HighScore.minsize(width=400,height=250)
        HighScore.geometry("400x250+450+100")
        HighScore.maxsize(width=400,height=250)
        HighScore.config(bg="#cdcdc0")
        HS_image = CTkImage(Image.open("images/high-score_win.png"), size=(150, 135))
        H_S_image = CTkLabel(HighScore,text="", image=HS_image,bg_color="#cdcdc0")
        H_S_image.place(x=120,y=40)

    def GameWin_win(self):
        GameWin=CTkToplevel()
        GameWin.title("Winner")
        GameWin.minsize(width=400,height=250)
        GameWin.geometry("400x250+450+100")
        GameWin.maxsize(width=400,height=250)
        GameWin.config(bg="#98dbc6")
        G_W_image = CTkImage(Image.open("images/you-win.png"), size=(150, 135))
        GameWin = CTkLabel(GameWin,text="", image=G_W_image,bg_color="#98dbc6")
        GameWin.place(x=120,y=40)

        
    def GameOver_win(self):
        root.withdraw()
        GameOver=CTkToplevel()
        GameOver.title("Game Over!")
        GameOver.minsize(width=400,height=250)
        GameOver.geometry("400x250+450+100")
        GameOver.maxsize(width=400,height=250)
        GameOver.config(bg="#8d230f")
        G_O_image = CTkImage(Image.open("images/game-over.png"), size=(150, 135))
        GameOver = CTkLabel(GameOver,text="", image=G_O_image,bg_color="#8d230f")
        GameOver.place(x=120,y=40)


class press:
    a = 0
    turn = [0, 0, 0]
    c = 0
    I = [-1, -1, -1]
    J = [-1, -1, -1]
    scor = 0
    sc = 0
    high_sc = ""
    prev_high_sc = ""
    timer=""
    

    def timmer_(self):
        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(int(elapsed_time), 60)
            self.timer = ' {:02d} : {:02d} '.format(mins, secs)
            timera.set(str(self.timer))
            root.update()
            if str(self.timer)==" 02 : 30 ":
                break

            
    def updt_score(self):
        f = open("C:\\Users\\MY\\Desktop\\my python projects\\pic flip card game\\score\\score.txt",'r')
        self.prev_high_sc = f.read()
        f.close()
        if (self.high_sc) < (self.prev_high_sc):
            f = open("C:\\Users\\MY\\Desktop\\my python projects\\pic flip card game\\score\\score.txt",'w')    
            f.write(self.high_sc)
            f.close()


    def ShowHighSc(self):
        f = open("C:\\Users\\MY\\Desktop\\my python projects\\pic flip card game\\score\\score.txt",'r')
        prev_high = f.read()        
        prev = " 0"+prev_high[0]+" : "+prev_high[1]+prev_high[2]+" "
        score_for_player2 = CTkLabel(root,text=prev,font=('arial',27,"bold"),bg_color='#6cf5c2',text_color="black")
        score_for_player2.place(x=510,y=47)
        f.close()


    def click(self, i, j, x_, y_):
        clk.play()
        self.c += 1
        self.sc+=1

        if self.c % 2 != 0 and self.c < 3:
            self.I[0] = i
            self.J[0] = j
        elif self.c % 2 == 0:
            self.I[1] = i
            self.J[1] = j
        else:
            self.I[2] = i
            self.J[2] = j

        img = CTkImage(Image.open(str(images[i][j])), size=(70, 70))
        btn[i][j] = CTkButton(root, text='', height=10, width=50, image=img)
        btn[i][j].place(x=x_, y=y_)

        if self.turn[0] != self.turn[1]:
            if self.a == 0:
                self.a = 1
            else:
                self.a = 0
            self.turn[0] = self.turn[1]

        if self.c % 2 == 0:
            if (images[self.I[1]][self.J[1]] == images[self.I[0]][self.J[0]]):
                self.scor += 1
                sc = "{:02d}".format(self.scor)
                score.set(str(sc))
                g = windows()
                if self.scor == 18 or self.timer == " 02 : 30 ":
                    self.high_sc = self.timer[2]+self.timer[6]+self.timer[7]
                    f = open("C:\\Users\\MY\\Desktop\\my python projects\\pic flip card game\\score\\score.txt",'r+')
                    self.prev_high_sc = f.read()
                    f.close()
                    
                    if self.scor == 18 and (self.high_sc) < (self.prev_high_sc):
                        self.updt_score()
                        pygame.mixer.music.load("audio/victory_sound.mp3")
                        pygame.mixer.music.play()
                        g.HighScore_win()
                    elif self.scor == 18 and self.high_sc > self.prev_high_sc:
                        pygame.mixer.music.load("audio/victory_sound.mp3")
                        pygame.mixer.music.play()
                        g.GameWin_win()
                

        if self.c % 2 != 0 and self.c > 1:
            g = windows()
            self.high_sc = self.timer[2]+self.timer[6]+self.timer[7]
            f = open("C:\\Users\\MY\\Desktop\\my python projects\\pic flip card game\\score\\score.txt",'r+')
            self.prev_high_sc = f.read()
            f.close()
            
            if (images[self.I[1]][self.J[1]] != images[self.I[0]][self.J[0]]):
                btn[self.I[1]][self.J[1]].place_forget()
                btn[self.I[0]][self.J[0]].place_forget()
                self.turn[1] += 1
                
            if self.scor < 18 and self.timer == " 02 : 30 ":
                pygame.mixer.music.load("audio/mixkit-fairytale-game-over-1945.wav")
                pygame.mixer.music.play()
                g.GameOver_win()

            self.I[0] = self.I[2]
            self.J[0] = self.J[2]

        if self.sc==1:
            self.timmer_()
    

list_of_imgs = ["images/bike.png","images/books.png","images/bulb.png","images/cake.png","images/car.png","images/cloud.png","images/controler.png","images/crown.png","images/diamond.png","images/football.png","images/fruits.png","images/heart.png","images/hut.png","images/leaf.png","images/lion.png","images/sword.png","images/person.png","images/sun.png"]

RandomList1 = []
while len(RandomList1) != len(list_of_imgs):
    element = random.choice(list_of_imgs)
    if element not in RandomList1:
        RandomList1.append(element)

RandomList2 = []
while len(RandomList2) != len(list_of_imgs):
    element = random.choice(list_of_imgs)
    if element not in RandomList2:
        RandomList2.append(element)

imag = []
index = 0
while len(imag) != 36:
    imag.append(RandomList1[index])
    imag.append(RandomList2[index])
    index += 1

images = [[],[],[],[],[],[]]
z = 0
for i in range(6):
    for j in range(6):
        images[i].append(imag[z-1])
        z += 1


root = CTk()

score=StringVar()
timera=StringVar()

root.title("flip the card")

p = press()
w = windows()
w.startup_win()

root.minsize(height=700,width=700)
root.maxsize(height=700,width=700)
root.geometry("700x700+330+1")

pl1 = CTkImage(Image.open("images/alarm-clock.png"), size=(150, 135))
current_time = CTkLabel(root,text="", image=pl1)
current_time.place(x=70,y=-10)

vs = CTkImage(Image.open("images/score-board.png"), size=(90, 90))
score_board = CTkLabel(root,text="", image=vs)
score_board.place(x=303,y=19)

pl2 = CTkImage(Image.open("images/high_score.png"), size=(195, 155))
player2 = CTkLabel(root,text="", image=pl2)
player2.place(x=445,y=-14)

timer_ = CTkLabel(root,textvariable=timera,font=('arial',26,"bold"),bg_color='#dff6fd',text_color="black")
timer_.place(x=100,y=42)

sc_lbl = CTkLabel(root,textvariable=score,font=("arial",30,'bold'),bg_color="white",text_color="black")
sc_lbl.place(x=331,y=36)

score_for_player2 = CTkLabel(root,text=" 00 : 00  ",font=('arial',27,"bold"),bg_color='#6cf5c2',text_color="black")
score_for_player2.place(x=510,y=47)

btn1 = CTkButton(root, text='', height=75, width=75, command=lambda i=0, j=0, x_=60, y_=110: p.click(i, j, x_, y_))
btn1.place(x=60, y=110)
btn2 = CTkButton(root, text='', height=75, width=75, command=lambda i=0, j=1, x_=160, y_=110: p.click(i, j, x_, y_))
btn2.place(x=160, y=110)
btn3 = CTkButton(root, text='', height=75, width=75, command=lambda i=0, j=2, x_=260, y_=110: p.click(i, j, x_, y_))
btn3.place(x=260, y=110)
btn4 = CTkButton(root, text='', height=75, width=75, command=lambda i=0, j=3, x_=360, y_=110: p.click(i, j, x_, y_))
btn4.place(x=360, y=110)
btn5 = CTkButton(root, text='', height=75, width=75, command=lambda i=0, j=4, x_=460, y_=110: p.click(i, j, x_, y_))
btn5.place(x=460, y=110)
btn6 = CTkButton(root, text='', height=75, width=75, command=lambda i=0, j=5, x_=560, y_=110: p.click(i, j, x_, y_))
btn6.place(x=560, y=110)

btn7 = CTkButton(root, text='', height=75, width=75, command=lambda i=1, j=0, x_=60, y_=210: p.click(i, j, x_, y_))
btn7.place(x=60, y=210)
btn8 = CTkButton(root, text='', height=75, width=75, command=lambda i=1, j=1, x_=160, y_=210: p.click(i, j, x_, y_))
btn8.place(x=160, y=210)
btn9 = CTkButton(root, text='', height=75, width=75, command=lambda i=1, j=2, x_=260, y_=210: p.click(i, j, x_, y_))
btn9.place(x=260, y=210)
btn10 = CTkButton(root, text='', height=75, width=75, command=lambda i=1, j=3, x_=360, y_=210: p.click(i, j, x_, y_))
btn10.place(x=360, y=210)
btn11 = CTkButton(root, text='', height=75, width=75, command=lambda i=1, j=4, x_=460, y_=210: p.click(i, j, x_, y_))
btn11.place(x=460, y=210)
btn12 = CTkButton(root, text='', height=75, width=75, command=lambda i=1, j=5, x_=560, y_=210: p.click(i, j, x_, y_))
btn12.place(x=560, y=210)

btn13 = CTkButton(root, text='', height=75, width=75, command=lambda i=2, j=0, x_=60, y_=310: p.click(i, j, x_, y_))
btn13.place(x=60, y=310)
btn14 = CTkButton(root, text='', height=75, width=75, command=lambda i=2, j=1, x_=160, y_=310: p.click(i, j, x_, y_))
btn14.place(x=160, y=310)
btn15 = CTkButton(root, text='', height=75, width=75, command=lambda i=2, j=2, x_=260, y_=310: p.click(i, j, x_, y_))
btn15.place(x=260, y=310)
btn16 = CTkButton(root, text='', height=75, width=75, command=lambda i=2, j=3, x_=360, y_=310: p.click(i, j, x_, y_))
btn16.place(x=360, y=310)
btn17 = CTkButton(root, text='', height=75, width=75, command=lambda i=2, j=4, x_=460, y_=310: p.click(i, j, x_, y_))
btn17.place(x=460, y=310)
btn18 = CTkButton(root, text='', height=75, width=75, command=lambda i=2, j=5, x_=560, y_=310: p.click(i, j, x_, y_))
btn18.place(x=560, y=310)

btn19 = CTkButton(root, text='', height=75, width=75, command=lambda i=3, j=0, x_=60, y_=410: p.click(i, j, x_, y_))
btn19.place(x=60, y=410)
btn20 = CTkButton(root, text='', height=75, width=75, command=lambda i=3, j=1, x_=160, y_=410: p.click(i, j, x_, y_))
btn20.place(x=160, y=410)
btn21 = CTkButton(root, text='', height=75, width=75, command=lambda i=3, j=2, x_=260, y_=410: p.click(i, j, x_, y_))
btn21.place(x=260, y=410)
btn22 = CTkButton(root, text='', height=75, width=75, command=lambda i=3, j=3, x_=360, y_=410: p.click(i, j, x_, y_))
btn22.place(x=360, y=410)
btn23 = CTkButton(root, text='', height=75, width=75, command=lambda i=3, j=4, x_=460, y_=410: p.click(i, j, x_, y_))
btn23.place(x=460, y=410)
btn24 = CTkButton(root, text='', height=75, width=75, command=lambda i=3, j=5, x_=560, y_=410: p.click(i, j, x_, y_))
btn24.place(x=560, y=410)

btn25 = CTkButton(root, text='', height=75, width=75, command=lambda i=4, j=0, x_=60, y_=510: p.click(i, j, x_, y_))
btn25.place(x=60, y=510)
btn26 = CTkButton(root, text='', height=75, width=75, command=lambda i=4, j=1, x_=160, y_=510: p.click(i, j, x_, y_))
btn26.place(x=160, y=510)
btn27 = CTkButton(root, text='', height=75, width=75, command=lambda i=4, j=2, x_=260, y_=510: p.click(i, j, x_, y_))
btn27.place(x=260, y=510)
btn28 = CTkButton(root, text='', height=75, width=75, command=lambda i=4, j=3, x_=360, y_=510: p.click(i, j, x_, y_))
btn28.place(x=360, y=510)
btn29 = CTkButton(root, text='', height=75, width=75, command=lambda i=4, j=4, x_=460, y_=510: p.click(i, j, x_, y_))
btn29.place(x=460, y=510)
btn30 = CTkButton(root, text='', height=75, width=75, command=lambda i=4, j=5, x_=560, y_=510: p.click(i, j, x_, y_))
btn30.place(x=560, y=510)

btn31 = CTkButton(root, text='', height=75, width=75, command=lambda i=5, j=0, x_=60, y_=610: p.click(i, j, x_, y_))
btn31.place(x=60, y=610)
btn32 = CTkButton(root, text='', height=75, width=75, command=lambda i=5, j=1, x_=160, y_=610: p.click(i, j, x_, y_))
btn32.place(x=160, y=610)
btn33 = CTkButton(root, text='', height=75, width=75, command=lambda i=5, j=2, x_=260, y_=610: p.click(i, j, x_, y_))
btn33.place(x=260, y=610)
btn34 = CTkButton(root, text='', height=75, width=75, command=lambda i=5, j=3, x_=360, y_=610: p.click(i, j, x_, y_))
btn34.place(x=360, y=610)
btn35 = CTkButton(root, text='', height=75, width=75, command=lambda i=5, j=4, x_=460, y_=610: p.click(i, j, x_, y_))
btn35.place(x=460, y=610)
btn36 = CTkButton(root, text='', height=75, width=75, command=lambda i=5, j=5, x_=560, y_=610: p.click(i, j, x_, y_))
btn36.place(x=560, y=610)

btn = [[btn1,btn2,btn3,btn4,btn5,btn6],[btn7,btn8,btn9,btn10,btn11,btn12],[btn13,btn14,btn15,btn16,btn17,btn18],[btn19,btn20,btn21,btn22,btn23,btn24],[btn25,btn26,btn27,btn28,btn29,btn30],[btn31,btn32,btn33,btn34,btn35,btn36]]
p.ShowHighSc()

root.mainloop()
