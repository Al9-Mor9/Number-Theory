#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int main(){
	char N[100001];
	bool haveZero = false;
	int digitSum = 0;

	scanf("%s", N);
	for (int i = 0; N[i]; i++){
		if (N[i] == '0') haveZero = true;
		digitSum += N[i] - '0';
	}

	if (!haveZero || (digitSum % 3)) printf("-1");
	else {
		sort(N, N + strlen(N), greater<>());
		printf("%s", N);
	}
}
