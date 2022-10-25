// C program to read a BMP Image and
// write the same into a PGM Image file
#include <stdio.h>

void main()
{
	int i, j, temp = 0;
	int width = 13, height = 13;

	// Suppose the 2D Array to be converted to Image is as given below
	int image[13][13] = {
	{ 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 },
	{ 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31},
	{ 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47},
	{ 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63},
	{ 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79},
	{ 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95 },
	{ 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111, 111},
	{ 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127, 127},
	{ 143, 143, 143, 143, 143, 143, 143, 143, 143, 143, 143, 143, 143},
	{ 159, 159, 159, 159, 159, 159, 159, 159, 159, 159, 159, 159, 159},
	{ 175, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175, 175},
	{ 191, 191, 191, 191, 191, 191, 191, 191, 191, 191, 191, 191, 191},
	{ 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207}
	};

	FILE* pgmimg;
	pgmimg = fopen("pgmimg.pgm", "wb");

	// Writing Magic Number to the File
	fprintf(pgmimg, "P2\n");

	// Writing Width and Height
	fprintf(pgmimg, "%d %d\n", width, height);

	// Writing the maximum gray value
	fprintf(pgmimg, "255\n");
	int count = 0;
	for (i = 0; i < height; i++) {
		for (j = 0; j < width; j++) {
			temp = image[i][j];

			// Writing the gray values in the 2D array to the file
			fprintf(pgmimg, "%d ", temp);
		}
		fprintf(pgmimg, "\n");
	}
	fclose(pgmimg);
}
