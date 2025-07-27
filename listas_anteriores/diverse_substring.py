from collections import Counter


def verify_str(str):
    distinct_characters = len(set(str))
    diverse = list(filter(lambda d: Counter(str)[d] <= distinct_characters, Counter(str)))
    return len(diverse)


t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    if(len(s)<=n): print(verify_str(s))

