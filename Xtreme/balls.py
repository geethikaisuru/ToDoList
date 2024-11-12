'''
Balls

**Time limit:** 2500 ms
**Memory limit:** 256 MB

Josh has N tiles arranged in a row and he has numbered them from 1 to N. He also has K balls, and for each of the balls he knows a special property called elasticity. Josh denotes the elasticity of the i-th ball by Eᵢ. When he throws a ball of elasticity Eᵢ, it will hit the Eᵢ-th tile, 2 * Eᵢ-th tile, 3 * Eᵢ-th tile, and so on. 

Josh decides to throw all the K balls at once. How many tiles will he hit at least once?

**Standard input**
The first line contains two integers N and K.
The second line contains K integers, the elasticities of the balls.

**Standard output**
Print one integer representing the number of tiles that will be hit at least once.

**Constraints and notes**
1 ≤ N ≤ 10¹⁴
1 ≤ K ≤ 100
1 ≤ Eᵢ ≤ 1000
The greatest common divisor of any two elasticities is 1 (also expressed as gcd(Eᵢ, Eⱼ) = 1 for all i ≠ j)

----
Example 0 
Input 0
17 3
2 3 7

Output 0
12

Explanation 0
The first ball will hit the tiles 2, 4, 6, 8, 10, 12, 14, 16.
The second ball will hit the tiles 3, 6, 9, 12, 15.
The third ball will hit the tiles 7, 14.
In total there are 12 tiles hit by at least one ball: 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16. 
----
''''

import math
from itertools import combinations

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def c_titlesh(N, elasticities):
    num_tiles = 0
    K = len(elasticities)
    
    for i in range(1, K + 1):
        for subset in combinations(elasticities, i):
            # Calculate LCM of the current subset
            lcm_value = subset[0]
            for elasticity in subset[1:]:
                lcm_value = lcm(lcm_value, elasticity)
                if lcm_value > N:
                    break
            
            if lcm_value <= N:
                hit_count = N // lcm_value
                num_tiles += hit_count if i % 2 == 1 else -hit_count
    
    return num_tiles

N, K = map(int, input().split())
elasticities = list(map(int, input().split()))

print(c_titlesh(N, elasticities))
