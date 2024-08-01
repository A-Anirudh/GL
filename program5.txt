#include <GL/glut.h>
#include <stdio.h>

float lightPos[] = {2, 2, 2};
float ambient[] = {0, 1, 1, 1};

void align()
{
    glRotated(50, 0, 1, 0);
    glRotated(10, -1, 0, 0);
    glRotated(11, 0, 0, -1);
}

void myInit()
{
    glClearColor(0, 0, 0, 0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

void obj(float sx, float sy, float sz, float tx, float ty, float tz)
{
    align();
    glTranslated(tx, ty, tz);
    glScaled(sx, sy, sz);
    glutSolidCube(1);
    glLoadIdentity();
}

void display()
{
    obj(0.02, 1, 1, -0.5, 0, 0);
    obj(1, 1, 0.02, 0, 0, 0.5);
    obj(1, 0.02, 1, 0, -0.5, 0);

    obj(0.02, 0.25, 0.02, 0, -0.4, 0);
    obj(0.02, 0.30, 0.02, 0, -0.39, -0.4);
    obj(0.02, 0.30, 0.02, 0.4, -0.39, -0.4);
    obj(0.02, 0.30, 0.02, 0.4, -0.39, 0);

    obj(0.7, 0.02, 0.7, 0.4, -0.2, -0.4);

    align();
    glTranslated(0.4, -0.1, -0.4);
    glutSolidTeapot(0.1);

    glFlush();
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(600, 600);
    glutCreateWindow("1CR21CS015");

    myInit();
    glutDisplayFunc(display);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos);
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient);
    glEnable(GL_DEPTH_TEST);
    glutMainLoop();

    return 0;
}
