# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,0,200,scene_width,scene_height)
    draw_ground(canvas,0,0,scene_width,200)
    draw_sun(canvas,650,350,800,500)
    draw_clouds(canvas,550,400,75,90)
    draw_lake(canvas,400, 50, 750,150)
    draw_path(canvas,400,100,5,5)

    for x in range(50,800,50):
        draw_pine_tree(canvas,x,150,90)
        draw_grid(canvas,scene_width, scene_height, 50)

    #draw_sky(canvas,0,200,800,500)
   

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_grid(canvas, width, height, interval ):
    #draw vertical lines
    label_y=15
    for x in range(interval,width, interval):
        draw_line(canvas,x,0,x,height)
        draw_text(canvas,x,label_y,f"{x}")
    
    #drawing horizontal lines
    label_x=15
    for y in range(interval,height, interval):
        draw_line(canvas,0,y,width,y)
        draw_text(canvas,label_x,y,f"{y}")

def draw_clouds(canvas,limit_x, limit_y, min_diam,max_diam):
    for i in range(20):
        x = random.randint(150, limit_x)
        y = random.randint(350, limit_y)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="white", outline="")
##draw the sun using specig cordanates for x an y
def draw_sun(canvas,x_start,y_start,x_end,y_end):
    draw_oval(canvas, x_start, y_start, x_end, y_end, fill="yellow1")

## draw sky
def draw_sky(canvas, left_bottom_x,left_bottom_y ,right_top_x,right_top_y ):
    draw_rectangle(canvas,left_bottom_x, left_bottom_y,right_top_x, 
    right_top_y, fill="skyblue1")
##draw the ground giving the cordenates for two corners
def draw_ground(canvas, left_bottom_x,left_bottom_y ,right_top_x,right_top_y ):
    draw_rectangle(canvas,left_bottom_x, left_bottom_y,right_top_x, 
    right_top_y, fill="sandyBrown")

def draw_pine_tree(canvas, center_x, bottom, height):
    #draw a  trunk of pine tree
    trunk_width= height/10
    trunk_height= height/8
    left_trunk= center_x -trunk_width/2
    botton_trunk= bottom
    right_trunk=center_x+trunk_width/2
    trunk_top=bottom+ trunk_height
    draw_rectangle(canvas, left_trunk, botton_trunk, right_trunk, trunk_top, fill="tan4")

## draw the triangle of pine tree
    skirt_width=height/2
    skirt_left=center_x-skirt_width/2
    skirt_bottom=trunk_top
    peak_x=center_x
    peak_y=bottom + height
    skirt_rigth= center_x + skirt_width/2
    draw_polygon(canvas,skirt_left, skirt_bottom, peak_x,
    peak_y, skirt_rigth, skirt_bottom, fill="green")

## draw lake
def draw_lake(canvas,x_start,y_start,x_end,y_end):
    draw_oval(canvas, x_start, y_start, x_end, y_end, fill="blue1")

def draw_path(canvas,limit_x, limit_y, min_diam,max_diam):
    for i in range(1500):
        x = random.randint(50, limit_x)
        y = random.randint(80, limit_y)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="black", outline="")
# Call the main function so that
# this program will start executing.
main()