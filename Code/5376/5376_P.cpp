#include <iostream>
#include <string>
#include <cmath>
using namespace std;

long long N;
string n;

long long gcd(long long a, long long b){
    long long r;
    while (a && b){
        r = a % b;
        if (!r) return b;
        a = b;
        b = r;
    }
    return 0;
}

pair<long long, long long> toFrac(pair<string, string> parsed){
    long long nonRot = stol(parsed.first.length() ? parsed.first : "0");
    long long rot = stol(parsed.second.length() ? parsed.second : "0");
    long long num = (nonRot * pow(10, parsed.second.length()) + rot);
    num -=  (parsed.second.length())? nonRot : 0;
    long long denom = parsed.second.length() ? 0 : 1;

    for (long long i = 0; i < parsed.second.length(); i++){
        denom *= 10;
        denom += 9;
    }
    for (long long i = 0; i < parsed.first.length(); i++){
        denom *= 10;
    }
    long long g = gcd(num, denom);
    return {num / g , denom/g};
}

pair<string, string> parse(string n){
    string rot, nonRot;    
    bool rotFlag = false, nonRotFlag = false;
    for (long long i = 0; i < n.length(); i++){
        if (n[i] == '.'){
            nonRotFlag = true;
        }
        else if (n[i] == '('){
            nonRotFlag = false;
            rotFlag = true;
        }
        else if (n[i] == ')'){
            rotFlag = false;
        }
        else if (nonRotFlag){
            nonRot += n[i];
        }
        else if (rotFlag){
            rot += n[i];
        }
    }
    return {nonRot, rot};
}

int main(){
    cin >> N;
    for (long long i = 0; i < N; i++){
        cin >> n;
        pair<long long, long long> frac = toFrac(parse(n));
        cout << frac.first << "/" << frac.second << endl;
    }    
}
