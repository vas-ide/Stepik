#n, k = map(int, input().split())
def c_n_k(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c_n_k(n - 1, k) + c_n_k(n - 1, k - 1)

print(c_n_k(10, 5))