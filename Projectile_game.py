from turtle import Turtle, Screen, textinput, numinput, time, bye
import random
import math

# choose play area
width = 1200
height = 800

screen = Screen()
screen.title("Python 1D Game")
screen.bgcolor("black")
screen.setup(0.8, 0.9, None, 5)
screen.tracer(0)

cannon = Turtle("circle")
cannon.fillcolor("yellow")
cannon.penup()
    
target = Turtle("square")
target.fillcolor("red")
target.penup()

text = Turtle("circle")
text.penup()
text.hideturtle()
text.color("white")
text.fillcolor("white")
text.setpos(-600, 250)

stats = Turtle()
stats.penup()
stats.hideturtle()
stats.color("white")
stats.fillcolor("white")
stats.setpos(-600, 225)

font1 =("Cooper Black", 15, "italic")

line = Turtle()
line.penup()
line.hideturtle()
line.color('#222222')

feedback = Turtle()
feedback.penup()
feedback.hideturtle()
feedback.color("white")
feedback.fillcolor("white")
feedback.goto(0,100)

star = Turtle()
star.hideturtle()
star.color('yellow')



objects = [star, stats, target, cannon, feedback]


#   shape of the star
def star_shape():
    '''Draws the shape of a star'''

    star.pendown()
    star.begin_fill()
    star.setheading(-72)
    for _ in range(5):
        star.fd(20)
        star.left(72)
        star.fd(20)
        star.right(144)
    star.end_fill()
    star.penup()
    time.sleep(1)

#   positioning of stars
def draw_stars(n):
    '''Depending on input, draws 1, 2 or 3 stars at fixed positions.'''
    screen.tracer(0)
    #1 star segment
    if n == 1:
        # draw first star
        star.penup()
        star.setpos(0,120)
        star_shape()
        screen.update()

    #2 star segment
    elif n == 2:
        # draw first star
        star.penup()
        star.setpos(-30,120)
        star_shape()
        screen.update()


        # draw second star
        star.penup()
        star.setpos(30,120)
        star_shape()
        screen.update()


    #3 star segment
    elif n == 3: 
        # draw first star
        star.penup()
        star.setpos(-60,100)
        star_shape()
        screen.update()

        # draw second star
        star.penup()
        star.setpos(0,100)
        star_shape()
        screen.update()

        # draw third star
        star.penup()
        star.setpos(60,100)
        star_shape()
        screen.update()


    else:
        feedback.write(f"You Suck!\nLOL\nWHAT A PROJECTILE MOTION NUBBB", align = "center", font=font1)
    
    time.sleep(1)

#   num of stars to draw
def how_many_stars(dist):
    '''based on range of distance,
    input 0,1,2 or 3 into draw_stars()'''
    if dist < 50:
        draw_stars(3)
    elif dist < 150:
        draw_stars(2)
    elif dist < 250:
        draw_stars(1)
    else:
        draw_stars(0)

#   grid background
def draw_grid(x, y, grid_size):
    '''Draws a grid background based on x and y range and a grid size.'''
    
    #draw verticle lines
    for a in range(int(-x),int(x+1),grid_size):
        line.setpos(a,-y)
        line.pendown()
        line.setpos(a,y)
        line.penup()
    #   draw horizontal lines
    for b in range(int(-y),int(y+1),grid_size):
        line.setpos(-x,b)
        line.pendown()
        line.setpos(x,b)
        line.penup()

#   optimising projectile coordinates and print
def relative_coordinates(ini_xy_coords):
    ''''''
    x_cor = cannon.xcor() - ini_xy_coords[0]
    y_cor = cannon.ycor() - ini_xy_coords[1]
    a = ( int(x_cor), int(y_cor ))
    stats.clear()
    stats.write(f"""
    Projectile position:{a}.""",align='left', font=font1)


# #   welcome prompt
# def welcome_text():
#     prompt_1 = 'Press Ok to Play and Cancel to quit'
#     wanna_play = str.lower(textinput(title= "Welcome!",prompt = prompt_1 ))
#     if wanna_play == None:
#         bye()

#   spawn a cannon
def create_cannon():
    #   set x and y coordinates
    x_cannon = random.randint(-550,-400)
    y_cannon = random.randint(-290, 0)

    #   position turtle
    cannon.clear()
    cannon.setpos(x_cannon, y_cannon)

#   spawn a target
def create_target():
    #   set x and y coordinates
    x_target = random.randint(400,550)
    y_target = random.randint(-290, 300)

    #   position turtle
    target.setpos(x_target, y_target)

#   creating top left UI
def text_box(x_distance, y_distance, u, u_angle):
    
    message = """
    The horizontal distance is {}m.
    The vertical distance is {}m.
    Initial velocity: {} m/s.
    Launch angle: {} degrees.""".format(x_distance,y_distance,u,u_angle)

    text.clear()
    text.write( message ,font=font1)
    screen.update()

#   ask for starting velocity and angle
def req_for_inputs(x_distance,y_distance,u,u_angle):

    u = int(numinput("Launch velocity", "Velocity (m/s)\nEnter from 1 to 150"))
    text_box(x_distance,y_distance,u ,u_angle)

    u_angle = int(numinput("Launch angle relative to ground", "Angle (Degrees)" ))
    text_box(x_distance,y_distance,u ,u_angle)

    return u, u_angle

#   calculate trajectory
def calc_traj(ux,uy, cannon_initial_pos):
    #Drawing the trajectory path
    t = 0
    sx = 0
    sy = 0
    g = 9.81
    k = 0
    distance = []
    screen.tracer(3)

    #   equation of trajectory and calculation of closest distance
    while abs(sx) < 600 and -390 < sy < 500:
        sx = ux * t + cannon_initial_pos[0]
        sy = (uy * t) - ((g/2) * t**2) + cannon_initial_pos[1]
        t += 0.1
        k += 1

        #show coordinates of projectile
        relative_coordinates(cannon_initial_pos)
    #     stats.clear()
    #     stats.write(f"""
    # Projectile position:{relative_coordinates(initial)}.""",align='left', font=font1)

        # drawing of projectile path
        traj_tracer(k,sx,sy)

        #   calculate closest distance to target
        dist = cannon.distance(target.pos())
        distance.append(dist)
    print(min(distance))
    return min(distance)

#   lines for the cannon path
def traj_tracer(k,sx,sy):
        if k % 2 == 0:
            cannon.pendown()
            cannon.pencolor("white")
        # else:
        #     cannon.penup()
    
        time.sleep(0.05)
        screen.update()
        
        cannon.goto(sx, sy)
        cannon.penup()



#   main code
def run_game():
    '''Main code to run the game
    1. Set screen animation to null and draws the grid background.
    2. Update screen and set tracer to 1.
    3. Generate cannon and target.
    4. Calculate horizontal and vertical distance between cannon and target.
    5. Request for velocity and angle input.
    6. Animate and draw projectile motion.
    7. Draw stars based on displacement of cannon from target.
    8. End screen'''

    screen.tracer(0) 

    #   draw grid
    # draw_grid(width/2, height/2, 40)
    # screen.update()
    screen.tracer(1)

    create_target()
    create_cannon()
    cannon_initial_pos = cannon.pos()
    
    #screen.update()

    #   calculate distances between cannon and target
    x_distance = target.xcor() - cannon.xcor()
    y_distance = target.ycor() - cannon.ycor()
    time.sleep(2)

    #   setting of initial velocity and angle
    u = "-"
    u_angle = "-"
    text_box(x_distance,y_distance,u,u_angle)

    initial = req_for_inputs(x_distance,y_distance,u,u_angle)
    relative_coordinates(cannon_initial_pos)

    u = initial[0]
    u_angle = initial[1]

    u_angle_radian = u_angle * math.pi / 180
    ux = u * math.cos(u_angle_radian)
    uy = u * math.sin(u_angle_radian)
    time.sleep(2)

    minimum_dist = calc_traj(ux,uy, cannon_initial_pos)

    how_many_stars(minimum_dist)

    time.sleep(2)
    print('b4 end screen')
    end_screen_text()
    print('aft end screen')

#   welcome prompt
def welcome_text():
    '''Welcomes the user to the game.
    Asks if the user wants to play.'''

    prompt_1 = 'Press Ok to Play and Cancel to Quit'
    wanna_play = str.lower(textinput(title= "Welcome!",prompt = prompt_1 ))
    if wanna_play == None:
        bye()

    draw_grid(width/2, height/2, 40)
    screen.update()
    screen.tracer(1)

    
#   ending screen
def end_screen_text():
    '''Prompt asking whether to play again or quit'''

    x = 'Would you still like to play?\nOK to play, Cancel to quit'
    play_again = str.lower(textinput(title= "Thanks for playing!",prompt = x ))
    if play_again == None:
        bye()
    for i in objects:
            print(i)
            i.clear()
        
    run_game()
    
#   play_game
def play_game():
    welcome_text()
    run_game()


play_game()


