# Xiaolin Wu's line algorithm ((9,6) and(14, 3).

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plot(x, y, intensity):
    glBegin(GL_POINTS)
    glColor3f(intensity, intensity, intensity)
    glVertex2f(x, y)
    glEnd()

def drawLineWu(x1, y1, x2, y2):
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
        intensity = 1.0 - (x - int(x))  # Calculate intensity based on fractional part of x
        plot(int(x), int(y), intensity)
        plot(int(x), int(y) + 1, 1 - intensity)

        x += xIncrement
        y += yIncrement

        print(f"({int(x)}, {int(y)})")  # Print each calculated point

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glPointSize(4.0)

    drawLineWu(9, 6, 14, 3)

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 20.0, 0.0, 10.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 250)
    glutCreateWindow(b"Wu's Antialiased Line Drawing")

    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()


# Output:
"""
Coordinates:
(9, 6)
(10, 5)
(11, 4)
(12, 4)
(13, 3)
(14, 3)
"""