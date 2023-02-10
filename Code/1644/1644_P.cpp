#include <iostream>
#include <vector>
using namespace std;

bool bprime[4000001] = { 0, };
vector<int> primes;

int mkprime(int N) {
	for (int i = 2; i <= N; i++) bprime[i] = true;

	for (int i = 2; i <= N; i++) {
		if (bprime[i]) {
			primes.push_back(i);
			for (int j = 2; i*j <= N; j++) {
				bprime[i*j] = false;
			}
		}
	}
	return primes.size();
}

int main() {
	int N, start = 0, end = 0, cnt = 0, np, sum = 2;
	scanf("%d", &N);
	np = mkprime(N);

	while (start <= end && end < np) {
		if (sum < N) {
			end++;
			if (end < np) sum += primes[end];
		}
		else if (sum > N) {
			sum -= primes[start];
			start++;
		}
		else if (sum == N) {
			cnt++;
			end++;
			if (end < np) sum += primes[end];
		}
	}
	printf("%d", cnt);
}
