# Gupta-Sproull algorithm (4, 3) and (12, - 5)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot(x, y, intensity):
    glBegin(GL_POINTS)
    glColor3f(intensity, intensity, intensity)
    glVertex2f(x, y)
    glEnd()

def drawLineGuptaSproull(x1, y1, x2, y2):
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
        intensity = 1.0 - (abs(x - round(x)) + abs(y - round(y))) # Calculate intensity based on fractional part of x and y
        plot(round(x), round(y), intensity) # Plot the pixel at (x, y) with calculated intensity
        x += xIncrement
        y += yIncrement

        print(f"({round(x)}, {round(y)})")  # Print each calculated point

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    glPointSize(4.0)

    drawLineGuptaSproull(4, 3, 12, -5)

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0) # Set background color to black
    gluOrtho2D(0.0, 20.0, -6.0, 4.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Gupta-Sproull Line Drawing")

    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()



# Output:
"""
Coordinates:
(4, 3)
(5, 2)
(6, 1)
(7, 0)
(8, -1)
(9, -2)
(10, -3)
(11, -4)
(12, -5)
"""