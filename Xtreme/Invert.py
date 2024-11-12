Think through the given problem and take note of the given example inputs, output and answer in python. Think and reason to understand the question first. Then reason through an algorithm to solve the problem. Them give the answer.


Invertible Pairs

**Time limit:** 750 ms
**Memory limit:** 512 MB

Given an integer array A (1-indexed) with even length n. You can do the following operation as many times as you want:

* Choose a pair of positions 2k-1 and 2k and multiply both A₂ₖ₋₁ and A₂ₖ by -1.

After finishing your operations, you must compute the maximum subarray sum of the resulting array. Maximize this value.

**Standard input**
The first line contains an integer T, the number of test cases.
The following lines describe t test cases. The first line of each test case contains an even integer Nᵢ, the length of the array. The second line contains Nᵢ integers Aⱼ, the j-th integer is the j-th element of the array.

**Standard output**
Print t lines, the i-th line must contain the answer to the i-th test case.

**Constraints and notes**
1 ≤ T ≤ 10⁵
1 ≤ ∑ᵢ₌₁ᵀ Nᵢ ≤ 4 * 10⁵
2 ≤ Nᵢ ≤ 2 * 10⁵ for every i = 1, ..., T
Nᵢ is even for every i = 1, ..., T
|Aⱼ| ≤ 10⁴ for every valid j



----
Example 0
Input 0
3
4
5 -10 7 -2
2
7 -8
2
5 4

Output 0
17
8
9

Explanation 0
For the first test case, it's possible to apply the operation on position 2, which gives the array (−5,10,7,−2) and its maximum subarray sum is 10+7=17.
----

Example 1
Input 1
2
6
-8 -6 9 5 -6 -10
2
-1 -8

Output 1
44
9

Explanation 1
For the second test case, it's possible to apply the operation on position 2, which gives the array (−7,8) and its maximum subarray sum is 8.
----

Example 2
Input 2
2
6
9 -5 -3 8 0 -6
2
-8 0

Output 2
16
8

Explanation 2
For the third test case, there is no need to apply the operation since all the values are positive, so the maximum subarray sum is 5+4=9

----


Please don't give example usage. Accommodate for user input. Think through the given problem and take note of the given example inputs, output, think and reason before answering.
