# 10.014 CTD 1D Project: Projectile-Motion-Game

SC07, Team 7J <br/>  
1006927 Wong Jun Ming, Ivan  <br/>
1006934 Ho Atsadet  <br/>
1006983 Tan Jie Ping  <br/>
1007136 Ooi Zher Xian  <br/>
1007208 Issac Anand Rajaram  <br/>

 
## Objective: <br/>
This game is aimed to help prospective physics students by exposing them to the physics concept of projectile motions. This game will allow students to visualise projectile motions with different initial velocities and angles. Students can therefore try to apply the physics concepts learnt in this game and get them more interested in studying physics. 

## Description: <br/>
This game starts with the system telling the user the distance between the cannon and the target. From there, it prompts the user to input the velocity and angle required to fire the cannon to the target. Thereafter, stars are awarded to the user depending on how close the cannon ball's trajectory is to the target. The closer the trajectory path of the cannonball, the more stars are awarded. 

 

## Documentation: <br/>
It is required for this game to use the Turtle, random and math library. <br/>

 ### welcome_text(): <br/>
This function displays the message “Welcome! Would you like to play?”, and then prompts user if they want to play. <br/>

__draw_grid(x, y, grid_size):__ <br/>
This function takes in x, y and grid_size. X is the width, y is the height of the screen respectively, and grid_size is the spacing between all lines. Using the for loop, it draws multiple horizontal and vertical lines that form a grid on the screen.  <br/>

__relative_coordinates(ini_xy_coords):__ <br/>
This function takes in ini_xy_coords, which is the tuple returning the initial coordinates of the cannon.  It calculates the distance between the cannon’s initial coordinates and its instantaneous coordinate. <br/>

__create_cannon():__ <br/>
This function creates a cannon object and sets random coordinates for the object within the range of the screen. <br/>

__create_target():__ <br/>
This function creates a target object and sets random coordinates for the target object within the range of the screen. <br/>

__text_box(x_distance, y_distance, u, u_angle):__ <br/>
This function takes in 4 parameters. x_distance and y_distance are the differences between the x and y coordinates of the target and on respectively. u is the user input for initial velocity in m/s, and u_angle is the angle to be launched relative to the ground in degrees. This function will then display the following message: <br/>

The horizontal distance is (x_distance)m. <br/>
The vertical distance is (y_distance)m. <br/>
Initial velocity: (u)m/s <br/>
Launch angle: (u_angle)degrees. <br/>

__req_for_inputs(x_distance, y_distance, u, u_angle):__ <br/>
This function asks for 2 user inputs via pop-up dialogue windows. The first is for launch velocity, u, and the second popup asks for launch angle,  u_angle.  It will call the text_box(x_distance, y_distance, u, u_angle) function to display the above message with the user’s inputs and return the tuple u, u_angle. <br/>

__calc_traj(ux, uy, cannon_initial_pos):__ <br/>
This function takes in ux, uy, and cannon_initial_pos. ux and uy are the horizontal and vertical components of the velocity respectively, and cannon_initial_pos takes in values in create_cannon().  <br/>

The path of trajectory is calculated using the following equations,  <br/>

sx = uxt + cannoninitialpos[0] <br/>
sy = uyt − g2t2 + cannoninitialpos[1] <br/>
 
where sx is the horizontal distance and sy is the vertical distance.  

__traj_tracker():__ <br/>
This function is called to draw the path of the trajectory using dotted lines. The distance between each point on the line of trajectory and the target is calculated and added to the list, distance.<br/>

__min():__ <br/>
This function is used to find the closest distance. <br/>

__cal_traj(ux, uy, cannon_initial_pos):__ <br/>
This function will return the closest distance based on the output from min(). <br/>

__traj_tracer(k, sx, sy):__ <br/>
This function takes in 3 parameters, k, sx, and sy. k is a variable that allows the line to be dotted, and parameters sx and sy are the values calculated in the calc_traj(ux, uy, cannon_initial_pos) function. This function moves the cannon object to the next instantaneous coordinates, drawing a dotted trajectory line along the way. <br/>
 
__how_many_stars(dist):__ <br/>
This function takes in variable dist, which is the values returned by calc_traj(). It will use the input dist to determine how many stars to display using the draw_stars(n) function. 

__star_shape():__ <br/>
This function draws the shape of the star using the turtle library when executed. The inside of the star will be filled with color as well. 

__draw_stars(n):__ <br/>
This function takes in n, the value returned from how_many_stars().  It will display a certain number of stars depending on the value of n. If the trajectory is too far away from the target, no stars will be given. Instead, it will display: <br/>

You Suck! <br/>
LOL <br/>
WHAT A PROJECTILE MOTION NUBBB <br/>

__end_screen_text():__ <br/>
This function displays the message “Thanks for playing! Would you still like to play?”, at the end of the game, and prompts users if they wish to continue the game or quit. <br/>

__play_game():__ <br/>
This function will run the game accordingly when the user inputs “y” for their welcome_text() and end_screen_text(). Otherwise, the game will end.  <br/>

 

__run_game():__ <br/>
This function runs the game. The pseudocode is as follows: <br/>

1. Set screen animation to null and draw the grid background. <br/>

2. Update the screen and set the tracer to 1.  <br/>

3. Generate cannon and target. <br/>

4. Calculate horizontal and vertical distance between cannon and target <br/>

5. Request for velocity and angle inputs.  <br/>

6. Animate and draw projectile motion. <br/>

7. Draw stars based on the displacement of the cannon from the target. <br/>

8. The user is then asked if they wish to play the game again.  <br/>

9. If yes, the game will restart. If no, the game will stop and close. <br/>
