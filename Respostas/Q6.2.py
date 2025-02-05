import time

def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    return dp[m][n]

str1 = "AGGTAB"
str2 = "GXTXAYB"

start_time = time.time()
lcs_result = lcs(str1, str2)
end_time = time.time()

print(f"Longest Common Subsequence: {lcs_result}")
print(f"Length: {len(lcs_result)}")
print(f"Execution time: {end_time - start_time:.6f} sec")
