#include <stdio.h>
#include <stdlib.h>

void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

return 0;
}
