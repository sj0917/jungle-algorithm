import sys
input = sys.stdin.readline

c, r = map(int, input().split())

_r = [0, r]
_c = [0, c]
for _ in range(int(input())):
    n, k = map(int, input().split())
    if n: _c.append(k)
    else: _r.append(k)

_r.sort()
_c.sort()
r_mx = 0
c_mx = 0
for i in range(len(_r)-1):
    r_mx = max(r_mx, _r[i+1] - _r[i])
for i in range(len(_c)-1):
    c_mx = max(c_mx, _c[i+1] - _c[i])
print(r_mx * c_mx)