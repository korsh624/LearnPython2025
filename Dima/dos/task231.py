def ways(start, finish, forbidden=None):
    dp = [0] * (finish + 1)
    dp[start] = 1

    for n in range(start + 1, finish + 1):
        if n == forbidden:
            dp[n] = 0
            continue

        dp[n] += dp[n - 1]
        if n - 3 >= start:
            dp[n] += dp[n - 3]
        if n % 2 == 0 and n // 2 >= start:
            dp[n] += dp[n // 2]

    return dp[finish]

print(ways(2, 15, 7) * ways(15, 25))
# 10935