# Any or All

x, N = int(input()), list(map(int, input().strip().split()))
print(all(n > 0 for n in N) and any(n < 10 or n % 11 == 0 for n in N))
