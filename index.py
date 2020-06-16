from tkinter import *
import random
from tkinter import messagebox

############################# FUNCTION ##############################
def timer():
    global timeleft,score,miss
    if timeleft > 0:
        timeleft-=1
        label5.configure(text=timeleft)
        label5.after(1000,timer)
    else:
        output.configure(text='hit = {} | miss = {} | total score = {}'.format(score,miss,score-miss))
        msgbx=messagebox.askretrycancel('notification','wanna play again? HIT RETRY BUTTON!')
        if msgbx == True:
            score = 0
            timeleft = 60
            miss = 0
            label5.configure(text=timeleft)
            label2.configure(text=countwords[0])
            label4.configure(text=score)

def playgame(event):
    global score,miss
    if timeleft == 60:
      timer()
    output.configure(text='')
    if(entry1.get()==label2['text']):
        score+=1
        label4.configure(text=score)
        #print('sc:',score)
    else:
        miss+=1
        #print('mi:',miss)
    random.shuffle(countwords)
    label2.configure(text=countwords[0])
    entry1.delete(0,END)




##############################   ROOT METHOD  ############################3
root = Tk()
root.geometry('800x500+400+100')
root.configure(bg='black')
root.title('typing speed game')

##################################### VARIABLE ###########################
score= 0
timeleft = 60
countwords = ['Mango','freelancer','independent','industries','illustrating','programming',
              'designate','cognitive','committed','necessarily','professional',
              'temporary','employment','participation','contractor',
              'highlighting','professions']
miss = 0

#############################  LABEL METHOD  #################################
random.shuffle(countwords)
label1 = Label(root , text = "WELCOME TO THE GAME!" ,bg = "black",fg='white', font = ('ariel' , 25 ))
label1.place(x=10,y=10)
label2 = Label(root , text = countwords[0],bg = "black",fg='white',font = ('ariel' , 30 ))
label2.place(x=300 ,y=200)
#############################  SCORE TEXT  #####################################
label3 = Label(root , text = "Your score : " ,bg = "black",fg='yellow', font = ('ariel' , 25 ))
label3.place(x= 30 , y=50)
#############################  SCORE COUNT  #########################################
label4 = Label(root , text = score ,bg = "black",fg='yellow', font = ('ariel' , 25 ))
label4.place(x= 80 , y=100)
#############################  TIMER TEXT  #########################################
label5 = Label(root , text = "Time left : " ,bg = "black",fg='yellow', font = ('ariel' , 25 ))
label5.place(x= 600 , y=50)
#############################  TIMER COUNT  #########################################
label5 = Label(root , text = timeleft ,bg = "black",fg='yellow', font = ('ariel' , 25 ))
label5.place(x= 650 , y=100)
############################# FINAL OUTPUT  #########################################
output = Label(root, text = "hit enter " ,bg = "black",fg='yellow', font = ('ariel' , 30 ))
output.place(x= 80 , y=450)


##############################  ENTRY BOX   ##################################
entry1= Entry(root,font = ('ariel', 20), bd= 10,justify='center')
entry1.place(x=240,y=300)
entry1.focus_set()
################################################################################
root.bind('<Return>',playgame)
root.mainloop()


