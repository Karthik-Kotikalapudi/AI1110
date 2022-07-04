void uniform(char *str, int len);
void gaussian(char *str, int len);
void V(char *str, int len);
double mean(char *str);
double var(char *str);
void triangular(char *str, int len);

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

void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
for (i = 0; i < len; i++)
{
	temp = 0;
	for (j = 0; j < 12; j++)
	{
	temp += (double)rand()/RAND_MAX;
	}
	temp-=6;
	fprintf(fp,"%lf\n",temp);
}
fclose(fp);
}

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

void triangular(char *str, int len)
{
double sum;
FILE *fp;

fp = fopen(str,"w");
for (int i = 0; i < len; i++)
{
	sum = 0;
	for (int j = 0; j < 2; j++)
	{
	sum += (double)rand()/RAND_MAX;
	}
	fprintf(fp,"%lf\n",sum);
}
fclose(fp);
}

double mean(char *str)
{
int i=0;
FILE *fp;
double x,req_mean, sum=0.0;

fp = fopen(str,"r");
while(fscanf(fp,"%lf",&x)!=EOF)
{
i=i+1;
sum = sum+x;
}
req_mean = sum/(i-1);
fclose(fp);
return req_mean;

}

double var(char *str)
{
int i=0;
FILE *fp;
double x,c,variance, sum=0.0;

fp = fopen(str,"r");

c = mean(str);
while(fscanf(fp,"%lf",&x)!=EOF)
{
i=i+1;
sum = sum+pow(x-c,2);
}
fclose(fp);
variance = sum/(i-1);
return variance;
}



