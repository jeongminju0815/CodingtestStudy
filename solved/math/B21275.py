from string import ascii_lowercase
from collections import defaultdict

alphabet = defaultdict(int)
start = 10
for s in list(ascii_lowercase):
    alphabet[s] = start
    start+=1


def gcd(x,y):
    print(x,y)
    x, y = int(x), int(y)
    while(y):
        x, y = y, x%y
    return x


print(gcd(str(alphabet["e"])+str(alphabet["p"]), str(alphabet["j"])+str(alphabet["h"])))