from curses.ascii import SP
from tkinter import *
import random
from tkinter import font
from xxlimited import foo

from numpy import square, true_divide

GAME_WIDTH=1200
GAME_HEIGHT = 700
SPEED=100
SPACE_SIZE = 50
BODY_PARTS= 2
SNAKE_COLOR = "#0000FF"
FOOD_COLOR="#FFFF00"
BACKGROUND_COLOR = "#000000"




class Snake:
    
    def __init__(self):
        # nbre de partie ( carre ) du serpent
        self.body_size = BODY_PARTS
        #liste des coordonnes
        self.coordinates = []
        #liste de graphique carre
        self.squares = []

        # cree liste des coor
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0, 0])
        # liste de liste pour crer des rectangles qui seront le serpent
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x+ SPACE_SIZE, y+ SPACE_SIZE, fill=SNAKE_COLOR,tag="snake")
            # ajouter le recttangle dans la liste des graphoque carre
            self.squares.append(square)


class Food:
    
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)* SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1)* SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")
        


#pour faire tourner le serpent
def next_turn(snake,food):

    x,y = snake.coordinates[0]
    if direction =="up":
        y -= SPACE_SIZE

    elif direction =="down":
        y += SPACE_SIZE

    elif direction =="left":
        x -= SPACE_SIZE

    elif direction =="right":
        x += SPACE_SIZE


    snake.coordinates.insert(0,(x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR,tag="snake")

    snake.squares.insert(0, square)

    #la condition pour que le serpent puisse manger l'alimment
    #si les deux coordonnes sont les memes
    #l'aliment sera supprime ( genre comme si le serpent l'avait mangé )
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        #supprimer les coordonnes negatives et le dernier 
        #supprimer la derniere partie du corps
    
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
            window.after(SPEED, next_turn, snake, food)
   
#------------------------  pour faire changer de direction le serpent soit gauche, droite , haut,bas
def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
             direction = new_direction
    
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    

def check_collisions(snake):
    
    x , y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME_OVER")
        return True
    elif y <0 or y >= GAME_HEIGHT:
        print("GAME_OVER")
        return True

    # si le serpent touche son corps et une autre partie 
    # game over
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME_OVER")
            return True



def game_over():
    #tout supprime
    canvas.delete(ALL)
    #ecrire game over au milieu
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas",70),text="GAME OVER",fill="red",tag="gameover")


window= Tk()

window.title("Snake game")
window.resizable(False,False)



score = 0
direction= "down"

label=Label(window,text="Score:{}".format(score),font=('consolas',40))
label.pack()


canvas =Canvas(window, bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()

window_width= window.winfo_width()
window_height= window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int ( (screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#-------------------pour redirerctionner avec les touches 
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake= Snake()
food = Food()

next_turn(snake,food)

window.mainloop()

print(2)
