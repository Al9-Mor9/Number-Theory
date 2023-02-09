#include <iostream>
using namespace std;

int C, N, n;
int cnt[1001];

int gcd(int a, int b){
    int r;
    while (a && b){
        r = a % b;
        if (r == 0) return b;
        a = b;
        b = r;
    }
    if (a + b == 1) return 1;
    return -1;
}

int main(){
    cnt[1] = 1;
    for (int i = 1; i < 1001; i++){
        for (int j = 0; j < i; j++) {
            if (gcd(i, j) == 1) cnt[i] += 2;
        }
        cnt[i] += cnt[i-1];
    }
    scanf("%d", &C);
    for (int i = 0; i < C; i++){
        scanf("%d", &N);
        printf("%d\n",cnt[N]);
    }
}
