import time

def count_paint_ways(n, colors):
    if n == 0:
        return 0
    if n == 1:
        return colors
    dp = [0] * (n + 1)
    dp[1] = colors
    dp[2] = colors * (colors - 1)

    for i in range(3, n + 1):
        dp[i] = (colors - 1) * (dp[i - 1] + dp[i - 2])

    return dp[n]

chairs = 10
colors = 3

start_time = time.time()
ways = count_paint_ways(chairs, colors)
end_time = time.time()

print(f"Number of ways to paint {chairs} chairs with {colors} colors: {ways}")
print(f"Execution time: {end_time - start_time:.6f} sec")
