#include <iostream>
using namespace std;

int n, k, c, T;

pair<pair<int, int>, int> extendedGCD(int a, int b){
    int dividend = a, divisor = b;
    int q, r;
    int s_prev = 1, s_cur = 0, s_next;
    int t_prev = 0, t_cur = 1, t_next;    

    while (a && b){
        q = dividend / divisor;
        r = dividend % divisor;
        if (!r) return {{s_cur, t_cur}, divisor};
        s_next = s_prev - q * s_cur;
        t_next = t_prev - q * t_cur;
        s_prev = s_cur, s_cur = s_next;
        t_prev = t_cur, t_cur = t_next;
        dividend = divisor;
        divisor = r;
    }
    return {{-1, -1}, -1};
}

int main(){
    scanf("%d", &T);
    while (T--){
        scanf("%d%d", &k, &c);
        pair<pair<int, int>, int> extdGCD = extendedGCD(k, c);
        if (extdGCD.second != 1) printf("IMPOSSIBLE\n");
        else {
            int x = extdGCD.first.first;
            int y = extdGCD.first.second;
            while (!(x < 0 && y > 0)){
                x -= c;
                y += k;
            }
            while ((x < 0 && y > 0) && !(y <= 1000000000)){
                x += c;
                y -= k;
            }
            if (!(x < 0 && y > 0 && y <= 1000000000)) printf("IMPOSSIBLE\n"); 
            else printf("%d\n", y);
        }
    }
}
