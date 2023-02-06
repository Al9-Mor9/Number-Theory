#include <iostream>
using namespace std;

int N;
int v[1000001];
int tree[20000001];

int gcd(int a, int b){
    int q, r;
    while (a && b){
        q = a / b;
        r = a % b;
        if (!r) return b;
        a = b;
        b = r;
    }
    return a + b;
}

int make_GCD_tree(int from, int to, int node){
    if (from == to) return tree[node] = v[from];
    int mid = (from + to) / 2;
    int a = make_GCD_tree(from, mid, node * 2), b = make_GCD_tree(mid + 1, to, node * 2 + 1);
    return tree[node] = gcd(a, b);
}


int get_gcd(int node, int start, int end, int left, int right){
    if (left > end || right < start) return 0;
    else if (left <= start && end <= right) return tree[node];
    else return gcd(get_gcd(2 * node, start, (start + end)/2, left, right), get_gcd(2 * node + 1, (start + end) / 2 + 1, end, left, right));
}

int main(){
    scanf("%d", &N);
    for (int i = 1; i <= N; i++){
        scanf("%d", &v[i]);
    }
    make_GCD_tree(1, N, 1);  

    int maxIdx = -1, maxGCD = tree[0], g = 1;
    for (int i = 1; i <= N; i++){
        int l = get_gcd(1, 1, N, 1  , i-1);
        int r = get_gcd(1, 1, N, i+1, N);
        g = gcd(r, l);
        if (g > maxGCD && (v[i] % g)) {
            maxGCD = g;
            maxIdx = i;
        }
    }    

    if (maxIdx < 0 ) printf("-1");
    else printf("%d %d", maxGCD, v[maxIdx]);    
    
}
