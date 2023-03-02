#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;


long long n;
vector<long long> primes;
unordered_set<long long> factors;

void getPrimes(){
	bool isPrime[1000001];
	for (int i = 0; i < 1000001; i++) isPrime[i] = true;	
	for (int i = 2; i < 1000001; i++){
		if (!isPrime[i]) continue;
		primes.push_back(i);
		for (int j = 2 * i; j < 1000001; j += i){
			isPrime[j] = false;
		}
	}	
}

void factorize(long long n){
	int i = 0;
	while (i < primes.size()){
		if (n % primes[i] == 0) {
			n /= primes[i];
			factors.insert(primes[i]);
		}
		else i++;
	}
	if (n != 1) factors.insert(n);
}


int main(){
	getPrimes();
	
	scanf("%lld", &n);

	factorize(n);

	for (long long f : factors){
		n /= f;
		n *= (f-1);
	}	

	printf("%lld", n);

}
