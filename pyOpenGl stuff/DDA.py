# DDA line drawing Algorithm ((5,1) and(10, 3).


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def drawLineDDA(x1, y1, x2, y2): # DDA Line Drawing Algorithm
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    xIncrement = dx / steps 
    yIncrement = dy / steps

    x = x1
    y = y1

    print("Coordinates:")
    print(f"({x}, {y})")  # Print the starting point

    for _ in range(steps):
        plot(round(x), round(y))
        x += xIncrement 
        y += yIncrement

        print(f"({round(x)}, {round(y)})")  # Print each calculated point

def display():
    glClear(GL_COLOR_BUFFER_BIT) # Clear display window
    # Set thickness of point size to 4 pixels
    glPointSize(4.0)
   
    
    glColor3f(0.0, 0.0, 0.0)  # Set color to white
    # increase the line width
    glLineWidth(3.0) 

    drawLineDDA(5, 1, 10, 3) # Draw line from (5, 1) to (10, 3)

    glFlush()

def init():
    # Set background color to black
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 20.0, 0.0, 4.0) # Define the cartesian coordinate system

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # Set display mode
    glutInitWindowSize(500, 250) # Set display window width and height
    glutCreateWindow(b"DDA Line Drawing Algorithm") # this Creates display window with a title

    glutDisplayFunc(display) # Send graphics to display window
    init()
    glutMainLoop() # Display everything and wait

if __name__ == "__main__":  
    main()





# Output:

"""
Coordinates:
(5, 1)
(6, 1)
(7, 2)
(8, 2)
(9, 3)
(10, 3)
"""