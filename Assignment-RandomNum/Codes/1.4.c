#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double mean(char *str)
{
int i=0;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;

}

double var(char *str)
{
int i=0;
FILE *fp;
double x,c, temp=0.0;

fp = fopen(str,"r");

c = mean(str);
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+pow(x-c,2);
}
fclose(fp);
temp = temp/(i-1);
return temp;
}


int  main(void)
{

printf("mean:%lf	variance:%lf\n",mean("uni.dat"),var("uni.dat"));

return 0;
}

