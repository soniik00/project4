from tkinter import *
import random

window=Tk()

w=600
h=600

window.geometry(str(w)+'x'+str(h))

canvas=Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)

bg_photo=PhotoImage(file='bg_2.png')

class Knight:
    def __init__(self):
        #коордиаты центра рыцаря
        self.x=70
        self.y=h//2
        self.v=0
        self.photo=PhotoImage(file='knight.png')
    
    def up(self, event):
        self.v= -3
    
    def down(self, event):
        self.v=3
    
    def right(self, event):
        self.v=3
    
    def left(self, event):
        self.v=-3

    def stop(self, event):
        self.v=0

class Dragon:
    def __init__(self):
        self.x=random.randint(500,600 )
        self.y=random.randint(100, 500)
        self.v=random.randint(1,10)/8
        self.photo=PhotoImage(file='dragon.png')

knight=Knight()

dragons=[]
for i in range(10):
    dragons.append(Dragon())

def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y+=knight.v
    knight.x+=knight.v

    current_dragon=0
    dragon_to_kill=-1

    for dragon in dragons:
        dragon.x-=dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        
        if ((dragon.x-knight.x)**2)+ ((dragon.y-knight.y)**2)<=(96)**2:
            dragon_to_kill=current_dragon
        
        current_dragon+=1

        if dragon.x<=0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text='Ты проиграл:(', font='Ubuntu 60', fill='red')
  
    if dragon_to_kill>=0:
        del dragons[dragon_to_kill]

    if len(dragons)==0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text='Ура! Победа!!!', font='Ubuntu 60', fill='red' )
    else:
        window.after(5, game)

game()

window.bind('<Key Up>', knight.up)
window.bind('<Key Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<Key Right>', knight.right)
window.bind('<Key Left>', knight.left)

window.mainloop()

