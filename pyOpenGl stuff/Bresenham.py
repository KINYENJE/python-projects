# Bresenham’s Line-Drawing Algorithm (−4,7) and (2,3).

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def drawLineBresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / dx

    if slope > 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    x = x1
    y = y1

    p = 2 * dy - dx

    print("Coordinates:")
    print(f"({x}, {y})")  # Print the starting point

    for x in range(x1, x2 + 1):
        plot(x, y)
        if p >= 0:
            y = y + 1
            p = p - 2 * dx
        p = p + 2 * dy

        print(f"({x}, {y})")  # Print each calculated point

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Set color to BLACK

    glPointSize(4.0)

    drawLineBresenham(-4, 7, 2, 3) # Draw line from (-4, 7) to (2, 3)

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) # Set background color to WHITe  
    gluOrtho2D(-5.0, 5.0, 0.0, 15.0) # Define the cartesian coordinate system


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 250) 
    glutCreateWindow(b"Bresenham's Line Drawing Algorithm")

    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()



# Output:
""""
Coordinates:
(-4, 7)
(-4, 8)
(-3, 8)
(-2, 9)
(-1, 10)
(0, 10)
(1, 11)
(2, 12)
"""