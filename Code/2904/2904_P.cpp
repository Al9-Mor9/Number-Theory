/*
  코드가 매우 매우 매우 더러움에 
*/
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

int N, num[100];
int gcd = 1, cnt = 0;

vector<int> primes;
map<int, vector<int>> factor;

void factorize(int a){
    for (int prime : primes){
        int n = 0;
        while (!(a % prime)){
            n++;
            a /= prime;
        }    
        factor[prime].push_back(n);
    } 
}

void getPrime(){
    bool isPrime[1000001] = {false, };
    for (int i = 2; i < 1000001; i++) isPrime[i] = true;
    for (int i = 2; i < 1000001; i++){
        if (!isPrime[i]) continue;
        primes.push_back(i);        
        for (int j = 2 * i; j < 1000001; j += i){
            isPrime[j] = false;
        }
    }
}

int main(){
    getPrime();
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%d", &num[i]);
        factorize(num[i]);
    }

    for (pair<int, vector<int>> m : factor){
        int sum = 0;
        sort(m.second.begin(), m.second.end(), greater<>());
        priority_queue<int> pq;
        for (int i = 0; i < m.second.size(); i++){
            sum += m.second[i];
        } 
        if (sum >= N) {
            gcd *= pow(m.first, sum / N);
            for (int i = 0; i < m.second.size(); i++){
                if (m.second[i] >= sum / N){
                    pq.push(m.second[i] - (sum / N));
                }
                else if (m.second[i] == sum / N) continue;
                else {
                    while (m.second[i] < sum / N){
                        int top = pq.top();
                        pq.pop();
                        int amt = sum / N - m.second[i]; 
                        amt = top < amt ? top : amt;
                        cnt += amt;
                        top -= amt;
                        m.second[i] += amt;
                        if (top) pq.push(top);
                    }
                }
            }            
        }
    }

    printf("%d %d", gcd, cnt);


}
