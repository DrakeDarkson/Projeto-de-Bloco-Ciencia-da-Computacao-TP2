import time

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 5, 10, 25]
amount = 63

start_time = time.time()
result = min_coins(coins, amount)
end_time = time.time()

print(f"Minimum coins required: {result}")
print(f"Execution time: {end_time - start_time:.6f} sec")
