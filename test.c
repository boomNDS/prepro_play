#include <stdio.h>
int main(){
    int a = 600;
    double b = 1.5;
    int result1 = (a*6000/b+4*1000+786*0)*1000;
    double result2 = (a*6000/b+4*1000+786*0)*1000;
    printf("int result = %d\n", result1);
    printf("float result = %lf\n", result2);
    return 0;
}