#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void V(char *str, int len)
{
double x,i=0;
FILE *fin, *fout;

fout = fopen(str,"w");
fin = fopen("../Uniform_Random_Variables/uni.dat","r");
while(fscanf(fin,"%lf",&x)!=EOF)
{
	fprintf(fout,"%lf\n",-2*log(1-x));
}
fclose(fin);
fclose(fout);
}


int  main(void)
{

V("v.dat", 1000000);

return 0;
}

