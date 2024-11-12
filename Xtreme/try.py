def alice_wins_probability(R1, B1, R2, B2):
    dp = [[[[[0.0 for _ in range(2)] for _ in range(41)] for _ in range(41)] for _ in range(41)] for _ in range(41)]
    
    # Base cases
    for r1 in range(41):
        for b1 in range(41):
            for r2 in range(41):
                for b2 in range(41):
                    if r1 == 0 or b1 == 0:
                        dp[r1][b1][r2][b2][0] = 0.0
                        dp[r1][b1][r2][b2][1] = 0.0
                    elif r2 == 0 or b2 == 0:
                        dp[r1][b1][r2][b2][0] = 1.0
                        dp[r1][b1][r2][b2][1] = 1.0
    
    for r1 in range(40, -1, -1):
        for b1 in range(40, -1, -1):
            for r2 in range(40, -1, -1):
                for b2 in range(40, -1, -1):
                    for turn in range(2):
                        if r1 == 0 or b1 == 0 or r2 == 0 or b2 == 0:
                            continue
                        if turn == 0:
                            lose_red = (r2 / (r2 + b2)) * dp[r1 - 1][b1][r2][b2][1] if r1 > 0 else 0
                            lose_blue = (b2 / (r2 + b2)) * dp[r1][b1 - 1][r2][b2][1] if b1 > 0 else 0
                        else:
                            lose_red = (r1 / (r1 + b1)) * dp[r1][b1][r2 - 1][b2][0] if r2 > 0 else 0
                            lose_blue = (b1 / (r1 + b1)) * dp[r1][b1][r2][b2 - 1][0] if b2 > 0 else 0
                        
                        dp[r1][b1][r2][b2][turn] = lose_red + lose_blue
    
    return dp[R1][B1][R2][B2][0]

# Read input values
R1, B1, R2, B2 = map(int, input().split())
# Calculate and print the probability of Alice winning
print(alice_wins_probability(R1, B1, R2, B2))
