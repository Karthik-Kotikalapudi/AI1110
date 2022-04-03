#include<stdio.h>
#include<math.h>

int main(){
    double r,h,V1,V2,V3,V;
    r = 7;
    h = 4;
    V1 = 2*M_PI*pow(r,3)/3;
    V2 = M_PI*pow(r,2)*h;
    V3 = M_PI*pow(r,2)*h/3;
    //Total Volume
    V = V1 + V2 + V3;
    printf("%f   %f", 490*M_PI, V);
    return 0;
}