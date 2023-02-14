import sys
sys.stdin = open("input.txt", "r", encoding="UTF-8")
# import sys 안해서 runtime error 4번 뜸
import sys
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a1, a2 = map(int, sys.stdin.readline().split())    
b1, b2 = map(int, sys.stdin.readline().split())

Greatest_Common_Dicisor = gcd(a1*b2 + a2*b1, a2*b2)
print((a1*b2 + a2*b1) //Greatest_Common_Dicisor, a2*b2//Greatest_Common_Dicisor)