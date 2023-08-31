from tkinter import *
from PIL import Image,ImageTk
from random import *

#main window
root=Tk()
root.title("ROCK PAPER AND SCISSOR ")
root.configure(background="#9b59b6")
root.geometry("600x160")



#picture
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.png"))
sciccor_img=ImageTk.PhotoImage(Image.open("scissor.png"))




#insert picture

user_label=Label(root,image=sciccor_img,bg="#9b59b6")
comp_label=Label(root,image=sciccor_img,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


#scores

playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)


#Indicator
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#Message

msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)
#update msg
def updateMsg(x):
    msg['text']=x
    
    
def updateUserScore():
    score=int(playerscore['text'])
    score+=1
    playerscore['text']=str(score)
    
def updateCompScore():
    score=int(computerscore['text'])
    score+=1
    computerscore['text']=str(score)


def checkWinner(player,computer):
    if player == computer:
        updateMsg("It's a Draw !!!")
    elif player == "rock":
        if computer =="paper":
            updateMsg("You Loose :( .")
            updateCompScore()
        else:
            updateMsg("You Win :) .")
            updateUserScore()
            
    elif player == "paper":
        if computer =="scissor":
            updateMsg("You Loose :( .")
            updateCompScore()
        else:
            updateMsg("You Win :) .")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateMsg("You Loose :( .")
            updateCompScore()
        else:
            updateMsg("You Win :) .")
            updateUserScore()
    else:
        pass        
            
choices=["rock","paper","scissor"]

#upadte choice
def updatechoice(x):
    #for computer
    
    compchoice=choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=sciccor_img)
    
    
    
    #for ueser
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sciccor_img)
    checkWinner(x,compchoice) 
        
#Buttons

rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updatechoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=3)



root.mainloop()