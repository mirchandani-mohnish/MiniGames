'''
To the reader/coder of this code:
This project consists of 7 different functions and a variety of sub-functions.
These functions are each called upon the button press of the main window.
Each of the sub-functions are only restricted to the functions that define them.

The variables that were required to be defined globally are available at the start respectively.
The code is as developed as it can be from a beginner programmer's point of view.

ALL CODE HAS BEEN COMPILED AND RUN IN PYTHON 3.8 ALONG WITH PYCHARM/IDLE.
PLEASE BEAR WITH US IF IT PERFORMS DIFFERENTLY IN YOUR IDE.

A special thanks to our professor
Prof. Jaideepsinh Raulji
for his tremendous encouragement and support. 


The Developers
Jatin Parmar:AU2040118
Omikumar Makadia:AU2040103
Mohnish Mirchandani:AU2040110

'''



from tkinter import *
import random
import time
import turtle
from tkinter import messagebox

temp_win = Tk()
temp_win.geometry("10x10")

#~~~~~~global Variables~~~~~
num = 0
ans = "1234"
attempt = 10
var = StringVar(temp_win)
text = StringVar(temp_win)
text1 = StringVar(temp_win)


press = False
B1posxl = 1
B1posx2 = 101
points = 0
B1posy = 400
o7 = 0
endline = 420

score = 0
attempts = 10

cnt = 0
player = 1
bx1 = "1"
bx2 = "2"
bx3 = " "
bx4 = " "
bx5 = " "
bx6 = " "
bx7 = " "
bx8 = " "
bx9 = " "
side = 0

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "jaideepsinh",
    "mexico",
    "dubai",
    "dhoni",
    "paris",
    "china",
    "corona",
    "hacker",
]

words = [
    "\" nptoyh \"",
    "\" avja \"",
    "\" wfsit \"",
    "\" cdanaa \"",
    "\" aidin \"",
    "\" aiearcm \"",
    "\" odnlon \"",
    "\" adeepsijhn \"",
    "\" ximeco \"",
    "\" budai \"",
    "\" onidh \"",
    "\" rispa \"",
    "\" hicna \"",
    "\" naroco \"",
    "\" ackerh \"",
]

#~~~~~~~~functions~~~~~~~
'''

    Message For Reader/Developer/User/Respected Sir:

    1) All the glitches have been fixed by the developer using python v3.9.0 (64-bit).

    2) We genuinly apologize for any glitch that occurs during the game Play.

    3) After Select Name Of Game From Main Menu Try To Click On Game Window Anywhere.

    4) For Neat & Smooth Experience Only Copy Code Of Particular Game And Run In New Window.

'''

#~~Playball game: Jatin Parmar
def playball():
        class Ball:

            def __init__(self, canvas, paddle, color):

                self.canvas = canvas

                self.paddle = paddle

                self.id = canvas.create_oval(0,0,20,20,fill=color)

                self.canvas.move(self.id,245,100)

                starts = [-3, -2, -1, 1, 2, 3]

                random.shuffle(starts)

                self.x = starts[0]

                self.y = -3

                self.canvas_height = self.canvas.winfo_height()

                self.canvas_width = self.canvas.winfo_width()

                self.hit_bottom = False



            def hit_paddle(self, pos) :

                paddle_pos = self.canvas.coords(self.paddle.id)

                if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:

                    if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                        return True

                return False

            # Speed Control Of Ball After Hit The Ball

            def draw(self) :

                self.canvas.move(self.id,self.x,self.y)

                pos =self.canvas.coords(self.id)

                if pos[1] <= 0:

                    self.y = 6

                if pos[3] >= self.canvas_height:

                    self.hit_bottom == False
                    top = Tk()

                    top.title()

                    top.geometry("0x0")

                    # Messagebox At End Of Game

                    def helloCallBack():

                        msg = messagebox.showinfo("Notice", "       ~~GAME IS OVER~~\n\n +++GAME DEVELOPER+++   \n        ** JATIN PARMAR **     ")
                        msg.destroy()
                        exit(0)

                    B = Button(top, text="Start", command=helloCallBack())

                    B.place(x=0, y=0)

                    top.mainloop

                # Speed Control Of Ball After Hit The Ball

                if self.hit_paddle(pos) == True:

                    self.y = -6

                if pos[0] <= 0:

                    self.x = 2

                if pos[2] >= self.canvas_width:

                    self.x = -2

        # Paddler Height,Width Of Rectangle And Length

        class Paddle:

            def __init__(self, canvas, color):

                self.canvas = canvas

                self.id = canvas.create_rectangle(0,0,100,10,fill=color)

                self.canvas.move(self.id,250,548)

                self.x = 0

                self.canvas_width = self.canvas.winfo_width()

                self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

                self.canvas.bind_all('<KeyPress-Right>', self.turn_right)



            def draw (self):

                self.canvas.move (self.id, self.x,0)

                pos = self.canvas.coords(self.id)

                if pos[0] <=0:

                    self.x = 0

                elif pos [2] >= self.canvas_width:

                    self.x = 0

            # Peddler Movement Speed

            def turn_left(self,evt):

                    self.x = -6

            def turn_right(self,evt):

                    self.x = 6



        tk = Tk()

        tk.title("Bouncing Ball Game By JATIN PARMAR")

        tk.resizable(50,50)

        tk.wm_attributes("-topmost",1)

        canvas = Canvas(tk, width=560, height =580, bd=0, highlightthickness=0)

        canvas.pack()

        tk.update()



        paddle = Paddle(canvas, 'blue')

        ball = Ball(canvas, paddle, 'red')



        while 1:

            if ball.hit_bottom == False:

                ball.draw()

                paddle.draw()

            tk.update_idletasks()

            tk.update()

            time.sleep(0.01)

        root.main()




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Weird Rainfall: Mohnish Mirchandani
def rainfall():
    '''
    Message for reader/user:
    1) All the glitches have been fixed by the developer using python v3.8.6
    2) We genuinly apologize for any glitch that occurs during the game
    3) Do not press the Stop button first as then the game does not work
    4) If the game does not work please press the play button twice
    '''


    main = Tk()
    main.geometry("652x480")
    main.resizable(height = False,width = False)
    main.title("Rainfall by Mohnish Mirchandani")
    ########Global Variables######
    press = False
    B1posxl = 1
    B1posx2 = 101
    points = 0
    B1posy = 400
    o7 = 0
    endline = 420
    global var
    var = StringVar()

    ########functions#######
    #For the box to move left
    def ButtonPressL():  # for the left button movement
        gamwin.move(B1,-30,0)
    #For the box to move right
    def ButtonPressR():  # for the right button movement
        gamwin.move(B1,30,0)

    #For the game to stop execution via the stop button
    def stop():         
        print("stop pressed")
        global press
        press = True

    # For the creation of new rain drops 
    def create(egg):    # to generate the ovals 
        
        global o1
        global o2
        global o3
        global o4
        global o5
        global o6
        global o7
        if(egg == o7):
            o1 = gamwin.create_oval(20,80,30,90,fill = "#034AEC")
            o2 = gamwin.create_oval(400,80,410,90,fill = "#034AEC")
            o3 = gamwin.create_oval(120,180,130,190,fill = "#034AEC")
            o4 = gamwin.create_oval(220,180,230,190,fill = "#034AEC")
            o5 = gamwin.create_oval(320,280,330,290,fill = "#034AEC")
            o6 = gamwin.create_oval(420,280,430,290,fill = "#034AEC")
        if(egg == o1):
            o1 = gamwin.create_oval(20,80,30,90,fill = "#034AEC")
        if(egg == o2):
            o2 = gamwin.create_oval(400,80,410,90,fill = "#034AEC")
        if(egg == o3):
            o3 = gamwin.create_oval(120,180,130,190,fill = "#034AEC")
        if(egg == o4):
            o4 = gamwin.create_oval(220,180,230,190,fill = "#034AEC")
        if(egg == o5):
            o5 = gamwin.create_oval(320,280,330,290,fill = "#034AEC")
        if(egg == o6):
            o6 = gamwin.create_oval(420,280,430,290,fill = "#034AEC")
       
     # updates the co-ordinates of every drop
    def update_coords():   
        global o1_coords
        global o2_coords
        global o3_coords
        global o4_coords
        global o5_coords
        global o6_coords
        global B1_coords
        o1_coords = gamwin.coords(o1)
        o2_coords = gamwin.coords(o2)
        o3_coords = gamwin.coords(o3)
        o4_coords = gamwin.coords(o4)
        o5_coords = gamwin.coords(o5)
        o6_coords = gamwin.coords(o6)
        B1_coords = gamwin.coords(B1)
        
        return

     # checks the coordinates of the eggs and the boxes   
    def check():         
        global points
        if(o1_coords[1] >= endline):
            points = points - 1
            gamwin.delete(o1)
            create(o1)
        if(o2_coords[1] >= endline):
            points = points - 1
            gamwin.delete(o2)
            create(o2)
        if(o3_coords[1] >= endline):
            points = points - 1
            gamwin.delete(o3)
            create(o3)
        if(o4_coords[1] >= endline):
            points = points - 1
            gamwin.delete(o4)
            create(o4)
        if(o5_coords[1] >= endline):
            points = points - 1
            gamwin.delete(o5)
            create(o5)
        if(o6_coords[1] >= endline):
            points = points - 1
            gamwin.delete(o6)
            create(o6)
            
        if(o1_coords[0]>B1_coords[0] and o1_coords[0]<B1_coords[2] and o1_coords[1] == B1posy):
            points = points+1
            gamwin.delete(o1)
            create(o1)
        if(o2_coords[0]>B1_coords[0] and o2_coords[0]<B1_coords[2] and o2_coords[1] == B1posy):
            points = points+1
            gamwin.delete(o2)
            create(o2)
        if(o3_coords[0]>B1_coords[0] and o3_coords[0]<B1_coords[2] and o3_coords[1] == B1posy):
            points = points+1
            gamwin.delete(o3)
            create(o3)
        if(o4_coords[0]>B1_coords[0] and o4_coords[0]<B1_coords[2] and o4_coords[1] == B1posy):
            points = points+1
            gamwin.delete(o4)
            create(o4)
        if(o5_coords[0]>B1_coords[0] and o5_coords[0]<B1_coords[2] and o5_coords[1] == B1posy):
            points = points+1
            gamwin.delete(o5)
            create(o5)
        if(o6_coords[0]>B1_coords[0] and o6_coords[0]<B1_coords[2] and o6_coords[1] == B1posy):
            points = points+1
            gamwin.delete(o6)
            create(o6)
        print(points)
        global var
        var.set(points)
        return
            
    # the function controls the movement of the eggs and
    #also binds all other funtions and loops until the stop button is pressed
    # the main function of the game
    def play():     
        
        global press
        eggno = random.randrange(1,7)
        if(eggno == 1):
            gamwin.move(o1,0,10)
        elif(eggno == 2):
            gamwin.move(o2,0,10)
        elif(eggno == 3):
            gamwin.move(o3,0,10)
        elif(eggno == 4):
            gamwin.move(o4,0,10)
        elif(eggno == 5):
            gamwin.move(o5,0,10)
        elif(eggno == 6):
            gamwin.move(o6,0,10)
        update_coords()
        check()
        if(press == True):
            press = False
            return
        else:
            gamwin.after(25,play)
    ##########

    ##########Panels - frames that define the main window
    TopPanel = Frame(main,borderwidth=6,bg="#fadadd",relief = "sunken")
    LeftPanel = Frame(main,borderwidth = 4,bg = "#fadadd",relief = "sunken")
    RightPanel = Frame(main,borderwidth = 4,bg = "#fadadd",relief = "sunken")
    TopPanel.pack(side = "top",anchor = "n",fill = "x")
    LeftPanel.pack(side = "left",anchor = "w",fill = "y")
    RightPanel.pack(side = "right",anchor = "e",fill = "y")
    #########


    #########canvas window - the window that draws all the shapes
    gamwin = Canvas(main,height = 440,width = 652,bg = "#87CEEB",relief = "sunken")
    create(o7)
    
    ## displays the points - updates itself after every movement
    point_label = Label(TopPanel, textvariable = var, relief = "raised")
    point_label.pack(side = "right")

    bottoml = gamwin.create_line(0,420,652,420,width = 6,fill = "#964B00")
    B1 = gamwin.create_rectangle(B1posxl,400,B1posx2,410,fill = "black")


    gamwin.pack(side = "top",anchor = "center")
    ##########


    ##########buttons

    BPlay = Button(TopPanel,bg = "#71c7ec",fg = "Black",text = "Play",command = play)# play button
    Bstop = Button(TopPanel,bg = "#71c7ec",fg = "Black",text = "stop",command = stop)
    Bleft  = Button(LeftPanel,bg = "#71c7ec",fg = "black",text = "Left",command = ButtonPressL)
    BRight = Button(RightPanel,bg = "#71c7ec",fg = "black",text = "Right",command = ButtonPressR)

    BPlay.pack(side = "left")
    Bstop.pack(side = "left")
    BRight.pack(side = "left", anchor = "center")
    Bleft.pack(side = "right", anchor = "center")
    ##########
     

    main.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Guessing Game: Omikumar Makadia
def guess():
    global text
    global attempts
    attempts = 10

    answer = random.randint(1,99)

    def check_answer():
        global attempts
        global text

        attempts -= 1


        guess=int(entry_window.get())

        if answer == guess:
            text.set("You win! Congrats !!")
            btn_check.pack_forget()

        elif attempts ==0:
            text.set("You are out of attempts!")
            btn_check.pack_forget()

        elif guess < answer:
            text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Go Higher!!")
        elif guess > answer:
            text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Go Lower!!")
        
        return

        
    root = Tk()

    root.title("Guess The Number By Omikumar Makadia")

    root.geometry("500x150")

    label = Label(root, text="Guess the number between 1 & 99")

    label.pack()

    entry_window = Entry(root, width=40, borderwidth=4)
    entry_window.pack()

    btn_check = Button(root, text="Check", command=check_answer)
    btn_check.pack()

    btn_quit = Button(root, text="Quit", command=root.destroy)
    btn_quit.pack()

    text = StringVar()
    text.set("You have 10 attempts remaining! Good Luck!")

    guess_attempts = Label(root, textvariable=text)
    guess_attempts.pack()

    root.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Snake: Omikumar Makadia
def snake():
    delay = 0.1

    #Score
    score = 0
    high_score = 0


    # Set up the screen 
    wn = turtle.Screen()
    wn.title("Snake Game by Omikumar Makadia: use W,A,S,D")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)


    #Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")

    head.color("red")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"


    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("green")
    food.penup()
    food.goto(0,100)

    segments=[]


    #Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"
        
    def go_down():
        if head.direction != "up":
            head.direction = "down"
        
    def go_left():
        if head.direction != "right":
            head.direction = "left"
        
    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
            
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
            

    #Keyborard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down,"s")
    wn.onkeypress(go_left,"a")
    wn.onkeypress(go_right,"d")

            
    #Main game loop
    while True:
        wn.update()
        
        #Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            
            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
                
            #Clear the segments list
            segments.clear()
            
            #Reset the score
            score = 0
            
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        
        #Check for a collision with the food 
        if head.distance(food) < 20:
            #Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            
            #Add a segment
            new_segment =turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)
            
            #Shorten the delay
            delay -= 0.001
            
            #Increase the score
            score += 10
            
            if score > high_score:
                high_score = score
                
                pen.clear()
                pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
        #Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
            
            
        #Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
        
        move()
        
        #Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                
                 #Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
                
                #Clear the segments list
                segments.clear()
                
                #Reset the score
                score = 0
                
                #Reset  the delay
                delay = 0.1
            
                #Update the score display
                pen.clear()
                pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        time.sleep(delay)
        
    wn.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



#Tic Tac Toe: Omikumar Makadia
def tic_tac_toe():
    global cnt
    global player
    cnt = 0
    bx1 = "1"
    bx2 = "2"
    bx3 = "3"
    bx4 = "4"
    bx5 = "5"
    bx6 = "6"
    bx7 = "7"
    bx8 = "8"
    bx9 = "9"
    root= Tk()
    root.geometry("290x258")
    root.title("Tic-Tac-Toe By Omikumar Makadia")
    button1 = Button(root, text = "  ",command = lambda: activate(1))
    button1.grid(row='0',column="0",ipadx="40",ipady="30")
    button2 = Button(root, text = "  ",command = lambda: activate(2))
    button2.grid(row='0',column="1",ipadx="40",ipady="30")
    button3 = Button(root, text = "  ",command = lambda: activate(3))
    button3.grid(row='0',column="2",ipadx="40",ipady="30")
    button4 = Button(root, text = "  ",command = lambda: activate(4))
    button4.grid(row='1',column="0",ipadx="40",ipady="30")
    button5 = Button(root, text = "  ",command = lambda: activate(5))
    button5.grid(row='1',column="1",ipadx="40",ipady="30")
    button6 = Button(root, text = "  ",command = lambda: activate(6))
    button6.grid(row='1',column="2",ipadx="40",ipady="30")
    button7 = Button(root, text = "  ",command = lambda: activate(7))
    button7.grid(row='2',column="0",ipadx="40",ipady="30")
    button8 = Button(root, text = "  ",command = lambda: activate(8))
    button8.grid(row='2',column="1",ipadx="40",ipady="30")
    button9 = Button(root, text = "  ",command = lambda: activate(9))
    button9.grid(row='2',column="2",ipadx="40",ipady="30")
    player = 1
    def activate(box):
        global player
        global cnt
        global bx1
        global bx2
        global bx3
        global bx4
        global bx5
        global bx6
        global bx7
        global bx8
        global bx9
        cnt =cnt +1
        if box == 1 and player == 1:
            button1.config(text="O")
            player = 2
            bx1="O"
        elif box == 1 and player == 2:
            button1.config(text="X")
            player =1
            bx1="X"
        elif box == 2 and player == 1:
            button2.config(text="O")
            player = 2
            bx2="O"
        elif box == 2 and player == 2:
            button2.config(text="X")
            player =1
            bx2="X"
        elif box == 3 and player == 1:
            button3.config(text="O")
            player = 2
            bx3="O"
        elif box == 3 and player == 2:
            button3.config(text="X")
            player =1
            bx3="X"
        elif box == 4 and player == 1:
            button4.config(text="O")
            player = 2
            bx4="O"
        elif box == 4 and player == 2:
            button4.config(text="X")
            player =1
            bx4="X"
        elif box == 5 and player == 1:
            button5.config(text="O")
            player = 2
            bx5="O"
        elif box == 5 and player == 2:
            button5.config(text="X")
            player =1
            bx5="X"
        elif box == 6 and player == 1:
            button6.config(text="O")
            player = 2
            bx6="O"
        elif box == 6 and player == 2:
            button6.config(text="X")
            player =1
            bx6="X"
        elif box == 7 and player == 1:
            button7.config(text="O")
            player = 2
            bx7="O"
        elif box == 7 and player == 2:
            button7.config(text="X")
            player =1
            bx7="X"
        elif box == 8 and player == 1:
            button8.config(text="O")
            player = 2
            bx8="O"
        elif box == 8 and player == 2:
            button8.config(text="X")
            player =1
            bx8="X"
        elif box == 9 and player == 1:
            button9.config(text="O")
            player = 2
            bx9="O"
        elif box == 9 and player == 2:
            button9.config(text="X")
            player =1
            bx9="X"

        if bx1 == bx2 == bx3 =="O" or bx4 == bx5 == bx6 =="O" or bx7 == bx8 == bx9 =="O":
            player = "O"
            m1 = messagebox._show("Game end", "player: " + player + " wins")
            m1.destroy()    
            exit(0)
        elif bx1 == bx2 == bx3 =="X" or bx4 == bx5 == bx6 =="X" or bx7 == bx8 == bx9 =="X":
            player = "X"
            m1 = messagebox._show("Game end", "player: " + player + " wins")
            m1.destroy()    
            exit(0)
        elif bx1 == bx4 == bx7 =="O" or bx2 == bx5 == bx8 =="O" or bx3 == bx6 == bx9 =="O":
            player = "O"
            m1 = messagebox._show("Game end", "player: " + player + " wins")
            m1.destroy()    
            exit(0)
        elif bx1 == bx4 == bx7 =="X" or bx2 == bx5 == bx8 =="X" or bx3 == bx6 == bx9 =="X":
            player = "X"
            m1 = messagebox._show("Game end", "player: " + player + " wins")
            m1.destroy()    
            exit(0)
        elif bx1 == bx5 == bx9 =="O" or bx3 == bx5 == bx7 =="O":
            player = "O"
            m1 = messagebox._show("Game end", "player: " + player + " wins")
            m1.destroy()    
            exit(0)
        elif bx1 == bx5 == bx9 =="X" or bx3 == bx5 == bx7 =="X":
            player = "X"
            m1 = messagebox._show("Game end", "player: " + player + " wins")
            m1.destroy()    
            exit(0)
        elif cnt == 9:
            m1 = messagebox._show("Game end", "Draw")
            m1.destroy()
            exit(0)
    root.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#Simple Dice: Mohnish Mirchandani
def dice():
    global side
    side = 0

    #Function chooses the side to display
    def randomside():
        global side
        
        
        side = random.randrange(1,7,1)
        print("button pressed")
        drawball()

    main = Tk()
    main.geometry("852x480")
    main.resizable(height = False,width = False)
    main.title("A Simple Dice by Mohnish Mirchandani")

    Toppanel = Frame(main,bg = "blue",relief = "sunken",height = 70,borderwidth = 2)
    play = Button(Toppanel,bg = "green",fg = "yellow",text = "play",command = randomside)

    play.pack(side = "top",anchor = "center")

    Toppanel.pack(side = "top",anchor = "n",fill = "x")
    mainwin = Canvas(main,height = 450,width = 852,bg = "#b5cfff")
    side1 = mainwin.create_rectangle(226,40,626,440,fill = "blue")

    #Function clears the canvas 
    def clearcanvas():
        mainwin.delete('dots')

    #Function draws the side that is to be displayed
    def drawball():
        clearcanvas()
        print(side)
        if(side == 1):
            mainwin.create_oval(416,230,426,240,fill = "yellow",tags = 'dots')
        elif(side == 2):
            mainwin.create_oval(349,230,359,240,fill = "yellow",tags = 'dots')
            mainwin.create_oval(472,230,482,240,fill = "yellow",tags = 'dots')
        elif(side == 3):
             mainwin.create_oval(326,230,336,240,fill = "yellow",tags = 'dots')
             mainwin.create_oval(416,230,426,240,fill = "yellow",tags = 'dots')
             mainwin.create_oval(516,230,526,240,fill = "yellow",tags = 'dots')
        elif(side == 4):
             mainwin.create_oval(326,230,336,240,fill = "yellow",tags = 'dots')
             mainwin.create_oval(516,230,526,240,fill = "yellow",tags = 'dots')
             mainwin.create_oval(416,130,426,140,fill = "yellow",tags = 'dots')
             mainwin.create_oval(416,330,426,340,fill = "yellow",tags = 'dots')
        elif(side == 5):
            mainwin.create_oval(416,230,426,240,fill = "yellow",tags = 'dots')
            mainwin.create_oval(326,230,336,240,fill = "yellow",tags = 'dots')
            mainwin.create_oval(516,230,526,240,fill = "yellow",tags = 'dots')
            mainwin.create_oval(416,130,426,140,fill = "yellow",tags = 'dots')
            mainwin.create_oval(416,330,426,340,fill = "yellow",tags = 'dots')
        elif(side == 6):
            mainwin.create_oval(326,130,336,140,fill = "yellow",tags = 'dots')
            mainwin.create_oval(416,130,426,140,fill = "yellow",tags = 'dots')
            mainwin.create_oval(516,130,526,140,fill = "yellow",tags = 'dots')
            mainwin.create_oval(326,330,336,340,fill = "yellow",tags = 'dots')
            mainwin.create_oval(416,330,426,340,fill = "yellow",tags = 'dots')
            mainwin.create_oval(516,330,526,340,fill = "yellow",tags = 'dots')
        


    mainwin.pack(side = "left",anchor = "s")



    main.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Surce Code Access by Omikumar Makadia
import sys
def source():

    def command1(event):
        if entry1.get() == 'Omi' and entry2.get() == '1234' or entry1.get() == 'Jatin' and entry2.get() == '1234' or entry1.get() == 'Mohnish' and entry2.get() == '1234':
            print("https://drive.google.com/file/d/15m5Bpxa1ig8CwlDb7AbNpvQe4BHx2Vje/view?usp=sharing")
            root.deiconify()
            top.destroy()

    def command2():
        top.destroy()
        root.destroy()
        sys.exit()

    root = Tk()
    top = Toplevel()

    top.geometry('300x200')
    top.title('Login Screen By Omikumar Makadia')
    top.configure(background='white')
    lbl1 = Label(top, text='Username', font=('Helvetica', 10))
    entry1 = Entry(top)
    lbl2 = Label(top, text='Password', font=('Helvetica', 10))
    entry2 = Entry(top, show="*")
    lbl_hint = Label(top, text='Username:(Omi) \nPassword:(1234)', font=('Helvetica', 10))
    button2 = Button(top, text='Cancel', command=lambda: command2())

    entry2.bind('<Return>', command1)

    lbl1.pack()
    entry1.pack()
    lbl2.pack()

    entry2.pack()
    button2.pack()
    lbl_hint.pack()

    root.title('Source Code')
    root.configure(background='white')
    root.geometry('400x50')
    lbl_hint2 = Label(root, text='Please find link in console', font=('Helvetica', 10))
    lbl_hint2.pack()

    #https://drive.google.com/file/d/15m5Bpxa1ig8CwlDb7AbNpvQe4BHx2Vje/view?usp=sharing
    root.withdraw()
    root.mainloop()


#~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Jumble your mind by Jatin Parmar
def jumble():
        global num
        global words
        num =  random.randrange(0, len(words), 1)
        
        global answers
        
        def default():
            global words,answers,num
            lbl.config(text = words[num])

        def res():
            global words,answers,num
            num = random.randrange(0, len(words), 1)
            lbl.config(text = words[num])
            e1.delete(0, END)
        # Ans Checking Control
        def checkans():
            global words,answers,num
            var = e1.get()
            if var == answers[num]:
                messagebox.showinfo("Success", "      WOW! Excellent\nYour Answer Is Correct")
                res()
            else:
                messagebox.showerror("Error", "      WORST! Very Bad\nYour Answer Is Incorrect")
                e1.delete(0, END)



        # Geometry Control
        root = Tk()
        root.geometry("350x400+400+300")
        root.title("Jumbling by JATIN PARMAR")
        root.configure(background = "#000000")

        def end():
            root.destroy()

            
        lbl = Label(
            root,
            text = "Your here",
            font = ("Verdana", 18),  # Verdana Is Font Type
            bg = "#000000",
            fg = "#FFFFFF",
        )
        lbl.pack(pady = 30,ipady=10,ipadx=10)


        ans1 = StringVar()
        e1 = Entry(
            root,
            font = ("Verdana", 16),  # Verdana Is Font Type
            textvariable = ans1,
        )
        e1.pack(ipady=5,ipadx=5)

        btncheck = Button(
            root,
            text = "Check",
            font = ("Comic sans ms", 16),  # Comic Sans ms Font Type
            width = 16,
            bg = "#4c4b4b",
            fg = "#ff8330",
            relief = GROOVE,
            command = checkans,
        )
        btncheck.pack(pady = 10)

        btnReset = Button(
            root,
            text = "Reset",
            font = ("Comic sans ms", 16),
            width = 16,
            bg = "#4c4b4b",
            fg = "#ffffff",
            relief = GROOVE,
            command = res,
        )
        btnReset.pack(pady = 15)
        btnExit = Button(
            root,
            text = "Exit",
            font = ("Comic sans ms", 16),
            width = 16,
            bg = "#4c4b4b",
            fg = "#03ff20",
            relief = GROOVE,
            command = end,
        )
        btnExit.pack(pady = 10)
        btnExit.pack()

        default()
        root.mainloop()





#Contributions
    
def credits():
    crwin = Tk()
    crwin.geometry("660x450")
    crwin.resizable(height = False,width = False)
    crwin.title("Credits")

    
    win = Frame(crwin,relief = "sunken",bg = "#080100",height = 652,width = 550)
    intro1 = Label(win,font ="none 24 bold",bg = "#080100",fg = "#27e8d2",text = "Welcome! Mini Games")
    text1 = "\n The project was the product of the collective hardwork and efforts of \n \
            all its team members\
            \n ~~~~ Omikumar Makadia~~~~\n >Tic-Tac-Toe< \n>Guess the Number< \n >The Legendary snake< \n           >Source Code Access< \
            \n ~~~~ Mohnish Mirchandani~~~~\n >Weird Rainfall< \n >A Simple Dice< \n >Main Window<\n\t  >Debugging<         \
            \n ~~~~ JATIN PARMAR~~~~\n >Bouncing Ball< \n >Jumble Your Mind< \n >Complete Overview< \n >Gui Optimization & Credit Screen<\n\
            Special Thanks to our Professor\t\n Prof. Jaideepsinh Raulji\n \
    For supporting us throughout the project and for teaching us all\n\
        that was required.\n\
     A very big Thank You to anyone who has helped us for the project\n"

    cont = Label(win,font = 16,bg = "#080100",fg = "#ffffff",text = text1)
    
    
        
    intro1.pack(side = "top",anchor = "center")
    cont.pack(side = "top",anchor = "center")
    
    win.pack(side = "top",anchor = "center",fill = "both")
    crwin.mainloop()

#########main window##########
mainwindow = Tk()
mainwindow.geometry("652x570")
mainwindow.resizable(height = False,width = False)
mainwindow.title("Mini Games")

toppanel = Frame(mainwindow,borderwidth = 6,relief = "sunken",bg = "#080100",height = 100)
midpanel = Frame(mainwindow,borderwidth = 6,relief = "sunken",bg = "#080100",height = 380)
bottompanel = Frame(mainwindow,borderwidth = 6,relief = "sunken",bg = "#c4a39d",height = 400)
intro = Label(toppanel,font = 32,bg = "#080100",fg = "#27e8d2",text = "Welcome! Mini Games")

gam1 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#5e2921",fg = "#ffffff",text = "Weird Rainfall",command = rainfall)
gam2 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#783e35",fg = "#ffffff",text = "Bouncing Ball",command = playball)
gam3 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#915f57",fg = "#ffffff",text = "Guess The Number",command = guess)
gam4 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#a87e77",fg = "#ffffff",text = "The Legendary Snake",command = snake)
gam5 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#c4a39d",fg = "#542a23",text = "Tic Tac Toe",command = tic_tac_toe)
gam6 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#dbc9c5",fg = "#471f19",text = "A Simple Dice",command = dice)
gam7 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#f0eae9",fg = "#000000",text = "Jumble your brain",command = jumble)
gam8 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#f0eae9",fg = "#000000",text = "Source Code Access",command = source)
gam9 = Button(midpanel,font = 16,height = 2,width = 200,borderwidth = 6,relief = "sunken",bg = "#f0eae9",fg = "#000000",text = "Credits",command = credits)


toppanel.pack(side = "top",anchor = "center",fill = "x")
midpanel.pack(side = "top",anchor = "center",fill = "both")
bottompanel.pack(side = "bottom",fill = "x")
intro.pack(side = "top",anchor = "center")
gam1.pack(side = "top")
gam2.pack(side = "top")
gam3.pack(side = "top")
gam4.pack(side = "top")
gam5.pack(side = "top")
gam6.pack(side = "top")
gam7.pack(side = "top")
gam8.pack(side = "top")
gam9.pack(side = "top")
'''
add jatin ka game and omi ka game
remove space bottom panel/
try to add a window for about button
color correction
'''

mainwindow.mainloop()

temp_win.mainloop()
