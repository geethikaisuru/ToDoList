'''
Halving

**Time limit:** 2500 ms
**Memory limit:** 64 MB

Alice and Bob are playing a secret communication game. Initially, Alice writes down on a piece of paper a permutation A of size 2 * N (each number from 1 to 2 * N appears in A exactly once). Then Bob chooses a binary array R of size N which he calls "the ruleset".

Alice uses A and R to create another array B of size N, which she communicates to Bob. The rules for building B are the following:

* If Rᵢ = 0, then Bᵢ = min(A₂ᵢ₋₁, A₂ᵢ).
* If Rᵢ = 1, then Bᵢ = max(A₂ᵢ₋₁, A₂ᵢ).

For each i, 1 ≤ i ≤ N.

Unfortunately, Alice has spilled some water on the piece of paper containing A, and now some of the numbers are impossible to read. You are given an array C of size 2 * N, where:

* Cᵢ = Aᵢ if the i-th number from A is still readable.
* Cᵢ = -1 otherwise.

You also know the ruleset array R and Bob's array B. Calculate the total number of possible initial arrays A. Output the result modulo 998244353.

**Standard Input**
The first line contains a single integer N.
The second line contains 2 * N integers C₁, C₂, ..., C₂ₙ.
The third line contains N integers R₁, R₂, ..., Rₙ.
The fourth line contains N integers B₁, B₂, ..., Bₙ.

**Standard Output**
Output a single integer — the number of permutations A consistent with the given data, modulo 998244353.

**Constraints and Notes**
1 ≤ N ≤ 300
Cᵢ = -1 or 1 ≤ Cᵢ ≤ 2 * N
the positive elements of C are pairwise distinct
Rᵢ ∈ {0, 1}
1 ≤ Bᵢ ≤ 2 * N
the elements of B are pairwise distinct

'''
MOD = 998244353

def count_possible_permutations(N, C, R, B):
    # Step 1: Identify known values and missing values in C
    known = {i: C[i] for i in range(2 * N) if C[i] != -1}
    missing_values = set(range(1, 2 * N + 1)) - set(known.values())
    
    # Edge case: if there are no missing values, directly validate with known values.
    if not missing_values:
        if validate_configuration(N, C, R, B, known):
            return 1
        else:
            return 0

    # Step 2: Create pairs based on R and B constraints
    pairs = []
    for i in range(N):
        a, b = 2 * i, 2 * i + 1
        if R[i] == 0:
            pairs.append((a, b, "min", B[i]))
        else:
            pairs.append((a, b, "max", B[i]))

    # Step 3: Count all valid permutations using backtracking
    def backtrack(index, assignment):
        # If all missing values are assigned, validate this configuration
        if index == len(missing_indices):
            return 1 if validate_configuration(N, C, R, B, {**known, **assignment}) else 0

        pos = missing_indices[index]
        total_count = 0
        
        # Attempt to assign each remaining missing value
        for val in missing_values:
            if val not in assignment.values():
                assignment[pos] = val
                # Early return if configuration is invalid
                if validate_partial_configuration(pos, assignment):
                    total_count += backtrack(index + 1, assignment)
                total_count %= MOD  # Apply modulo here only once
                del assignment[pos]  # Backtrack

        return total_count

    # Collect indices of missing positions
    missing_indices = [i for i in range(2 * N) if i not in known]
    return backtrack(0, {})

def validate_configuration(N, C, R, B, combined):
    for i in range(N):
        a, b = 2 * i, 2 * i + 1
        val_a = combined.get(a)
        val_b = combined.get(b)
        if val_a is None or val_b is None:
            continue  # Skip pairs with unknown values
        if R[i] == 0 and min(val_a, val_b) != B[i]:
            return False
        if R[i] == 1 and max(val_a, val_b) != B[i]:
            return False
    return True

def validate_partial_configuration(pos, assignment):
    """ Helper function to check only necessary constraints on partial assignments. """
    # Implement specific checks for early termination based on assignment so far.
    # This can be customized to check the current "pos" and values in assignment.

    return True  # Return True if partial assignment is still valid

# Input parsing and function call
try:
    N = int(input().strip())
    C = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    print(count_possible_permutations(N, C, R, B))
except Exception as e:
    print(f"Error: {e}")



    =====


    MOD = 998244353

def cPossible(N, C, R, B):
    known = {i: C[i] for i in range(2 * N) if C[i] != -1}
    missig = set(range(1, 2 * N + 1)) - set(known.values())
    
    if not missig:
        if val_config(N, C, R, B, known):
            return 1
        else:
            return 0
            
            
            '''except Exception as e:
    print(f"Error: {e}")'''

    pairs = []
    for i in range(N):
        a, b = 2 * i, 2 * i + 1
        if R[i] == 0:
            pairs.append((a, b, "min", B[i]))
        else:
            pairs.append((a, b, "max", B[i]))
            

    def backtrack(index, assignment):
        if index == len(missing_indices):
            return 1 if val_config(N, C, R, B, {**known, **assignment}) else 0

        pos = missing_indices[index]
        total_count = 0
        
        for val in missig:
            if val not in assignment.values():
                assignment[pos] = val
                if validate_partial_configuration(pos, assignment):
                    total_count += backtrack(index + 1, assignment)
                total_count %= MOD 
                del assignment[pos] 

        return total_count

    missing_indices = [i for i in range(2 * N) if i not in known]
    return backtrack(0, {})

def val_config(N, C, R, B, combined):
    for i in range(N):
        a, b = 2 * i, 2 * i + 1
        val_a = combined.get(a)
        val_b = combined.get(b)
        if val_a is None or val_b is None:
            continue  
        if R[i] == 0 and min(val_a, val_b) != B[i]:
            return False
        if R[i] == 1 and max(val_a, val_b) != B[i]:
            return False
    return True

def validate_partial_configuration(pos, assignment):
    return True  



try:
    N = int(input().strip())
    C = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))
    
    
    B = list(map(int, input().strip().split()))

    print(cPossible(N, C, R, B))

    
except Exception as e:
    print(f"Error: {e}")