#include <iostream>
using namespace std;

int gcd(int a, int b){
    int r;
    while (a && b){
        r = a % b;
        if (!r) return b;
        a = b;
        b = r;
    }
    return 0;
}

int main(){
    int a, b, c, d;
    int num, denom, g;
    scanf("%d%d%d%d", &a, &b, &c, &d);
    num = (a * d + b * c);
    denom = (b * d);
    g = gcd(num, denom);
    printf("%d %d", num/g, denom/g);
}
