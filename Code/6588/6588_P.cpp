#include <iostream>
using namespace std;

int N;
bool isNotPrime[10000001];

void getPrime(){
    for (int i = 2; i < 10000001; i++){
        if (isNotPrime[i]) continue;
        for (int j = 2 * i; j < 10000001; j += i){
            isNotPrime[j] = true;
        }
    }    
}

int main(){
    getPrime();
    while (true){
    scanf("%d", &N);
        if (N == 0) return 0;
        for (int i = 3 ; i < N; i++){
            if (!isNotPrime[i] && !isNotPrime[N - i]) {
                printf("%d = %d + %d\n", N, i, N - i);
                break;
            }
        }
    }
}
