#include <GL/glut.h>
float ambient[]={1,0,0,1};
float light_pos[]={2,2,2,1};
static float theta[3] = {0,0,0};
int axis = 0;
int ch=1;
void mouse(int button, int state, int x, int y)
{
if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)


axis = 0;
if(button == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
axis = 1;
if(button == GLUT_RIGHT_BUTTON && state == GLUT_UP)
axis = 2;
}
void idle(){
theta[axis] += 2;
if(theta[axis] > 360)
theta[axis] = 0;
glutPostRedisplay();
}
void display()
{
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
glClearColor(1,1,1,1);
glLoadIdentity();
glRotatef(theta[0],1,0,0); // rotation about x
glRotatef(theta[1],0,1,0); // rotate about y
glRotatef(theta[2],0,0,1); // rotate about z
if(ch==1)
glutSolidCube(1);
if(ch==2)
glutSolidTeapot(0.5);
if(ch==3)
glutSolidCone(0.5,0.5,20,20);
glFlush();
glutSwapBuffers(); // use whenever you use double buffer
}
void menu(int id)
{
switch(id)
{
case 1:
ch=1;
break;
case 2:
ch=2;
break;
case 3:
ch=3;
break;
}
}
int main(int argc, char ** argv)
{
glutInit(&argc,argv);
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
glutInitWindowSize(500,500);

glutCreateWindow("Color Cube");
glutCreateMenu(menu);
glutAddMenuEntry("Cube",1);
glutAddMenuEntry("Teapot",2);
glutAddMenuEntry("Cone",3);
glutAttachMenu(GLUT_RIGHT_BUTTON);
glutDisplayFunc(display);
glEnable(GL_LIGHTING);
glEnable(GL_LIGHT0);
glMaterialfv(GL_FRONT,GL_AMBIENT,ambient);
glLightfv(GL_LIGHT0,GL_POSITION,light_pos);
glutMouseFunc(mouse); //change axis of rotation
glutIdleFunc(idle);
glEnable(GL_DEPTH_TEST);
glutMainLoop();
return 0;
}
