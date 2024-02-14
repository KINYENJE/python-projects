# Midpoint Algorithm (- 4, 3) and (5, - 2).

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def drawLineMidpoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    slope = dy / dx

    if slope > 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    x = x1
    y = y1

    p = dy - dx / 2

    print("Coordinates:")
    print(f"({x}, {y})")  # Print the starting point

    for x in range(x1, x2 + 1):
        plot(x, y)
        if p < 0:
            p = p + dy
        else:
            y = y - 1
            p = p + dy - dx

        print(f"({x}, {y})")  # Print each calculated point

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glPointSize(4.0)

    drawLineMidpoint(-4, 3, 5, -2) # Draw line from (-4, 3) to (5, -2)

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) # Set background color to white
    gluOrtho2D(-5.0, 6.0, 1.0, 4.0) # Define the cartesian coordinate system

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Midpoint Line Drawing")

    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()




"""
Coordinates:
(-4, 3)
(-4, 3)
(-3, 3)
(-2, 3)
(-1, 3)
(0, 3)
(1, 3)
(2, 3)
(3, 3)
(4, 3)
(5, 3)

"""