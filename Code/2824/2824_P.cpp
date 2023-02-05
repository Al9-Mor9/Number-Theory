#include <iostream>
#include <vector>
#define INF 1000000000
using namespace std;

vector<int> A, B;
long long ans = 1;
int d;

int gcd(int a, int b){
    int dividend = a;
    int divisor = b;
    int quotient;
    int remainder;

    while (a && b){
        quotient = dividend / divisor;
        remainder = dividend % divisor;
        if (remainder == 0) return divisor;
        dividend = divisor;
        divisor = remainder;        
    }
    return -1;
}

int main(){
    int N, M, a, b;
    bool isTooBig = false;
    scanf("%d", &N);

    for (int i = 0; i < N; i++){
        scanf("%d", &a);
        A.push_back(a);
    }
    
    scanf("%d", &M);
    for (int i = 0; i < M; i++){
        scanf("%d", &b);        
        B.push_back(b);
    }

    if (A.size() < B.size()) swap(A, B);

    for (int i = 0; i < A.size(); i++){
        for (int j = 0; j < B.size(); j++){
            d = gcd(A[i], B[j]);
            A[i] /= d;
            B[j] /= d;
            ans *= d;
            if (ans >= INF) {
                ans %= INF;
                isTooBig = true;
            }

        }
    }

    if (!isTooBig) printf("%lld", ans);
    else {
        printf("%09lld", ans);
    }   
}
