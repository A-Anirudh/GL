#include <GL/glut.h>
#include <math.h>
#include <stdio.h>

void myInit()
{
	glClearColor(1, 1, 1, 0);
	gluOrtho2D(0, 600, 0, 600);
}

void display_point(int x, int y)
{
	glBegin(GL_POINTS);
	glVertex2d(x, y);
	glEnd();
}

void bresenhem_algo(int x1, int y1, int x2, int y2)
{

	int dely = abs(y2 - y1);
	int delx = abs(x2 - x1);
	double m = dely / delx;

	display_point(x1, y1);
	
	int incrX = 1, incrY = 1;
	if (x1 > x2)
		incrX = -1;
	if (y1 > y2)
		incrY = -1;
	
	int p0;
		if (m <= 1)
			p0 = 2 * dely - delx;
		else 
			p0 = 2 * delx - dely;
			
		while (x1 != x2 || y1 != y2)
		{
			if (p0 < 0)
			{
				if (abs(m) < 1) {
					p0 = p0 + 2 * dely;
					x1 += incrX;
				}
				else if (abs(m) == 1) {
					p0 = p0 + 2 * delx;
					y1 += incrY;	
				}
				else if (abs(m) > 1) {
					p0 = p0 + 2 * delx;
					y1 += incrY;
				}
			}
			else
			{
				if (abs(m) < 1)
					p0 = p0 + (2 * dely - 2 * delx);
				else if (abs(m) == 1)
					p0 = p0 + (2 * delx - 2 * dely);
				else 
					p0 = p0 + (2 * delx - 2 * dely);
				x1 += incrX;
				y1 += incrY;
			}
			display_point(x1, y1);
			printf("%d, %d\n", x1, y1);
		}
	
}

void displayMe()
{
	int x1, x2, y1, y2;
	printf("Enter x1 and y1: ");
	scanf("%d %d", &x1, &y1);

	printf("Enter x2 and y2: ");
	scanf("%d %d", &x2, &y2);

	glClear(GL_COLOR_BUFFER_BIT);
	glColor3d(0, 0, 0);
	bresenhem_algo(x1, y1, x2, y2);

	glFlush();
}

int main(int argc, char **argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE);
	glutInitWindowSize(600, 600);
	glutCreateWindow("Program-1");

	myInit();
	glutDisplayFunc(displayMe);
	glutMainLoop();

	return 0;
}
