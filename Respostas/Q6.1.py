import time

def knapsack(capacity, weights, values, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

items = [(2, 3), (3, 4), (4, 5), (5, 8)]
weights, values = zip(*items)
capacity = 7

start_time = time.time()
max_value = knapsack(capacity, weights, values, len(items))
end_time = time.time()

print(f"Maximum value: {max_value}")
print(f"Execution time: {end_time - start_time:.6f} sec")
