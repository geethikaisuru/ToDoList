'''
Think through the given problem and take note of the given example inputs, output and answer in python. Think and reason to understand the question first. Then reason through an algorithm to solve the problem. Them give the answer.


**Time limit:** 1250 ms
**Memory limit:** 64 MB

Given a sequence t₁, t₂, ..., tₖ, we are interested in grouping the elements into ⌈k/2⌉ groups — each group will contain exactly 2 elements, and if k is odd there will be exactly one group with just one element. For each group we compute the sum of its elements. We'll call the maximum of these sums the matching cost.
Out of all the possible ways of grouping the elements, we are interested in the one that has the smallest matching cost. We will call this value the optimal cost.

For example, the optimal cost for (5, 1, 3, 4) is 7, and we can get it by grouping the elements in {{5,1}, {3,4}}. Any other grouping has a larger matching cost.

You are given a sorted array A and you have to answer Q queries:

Each query consists of a single integer x.
For each subarray of A that has an optimal cost ≤ x, add the difference between the rightmost and the leftmost elements of the subarray. Formally, calculate ∑₁≤l≤r≤N, optimal cost(Aₗ, ..., Aᵣ) ≤ x (Aᵣ - Aₗ).

**Standard input**
The first line contains the integers N and Q, the number of elements in the sequence and the number of queries.
The second line contains the sequence of integers A₁, A₂, ..., Aₙ separated by spaces.
The next Q lines, the integer xᵢ, the value of x for the i-th query, is found.

**Standard output**
For each query, return the value of the indicated summation.

**Constraints and Notes**
1 ≤ N ≤ 10⁵
1 ≤ Q ≤ 100
0 ≤ Aᵢ ≤ 10⁹ for 1 ≤ i ≤ N
0 ≤ xᵢ ≤ 2 × 10⁹ for 1 ≤ i ≤ Q



----
Example 0
Input 0
10 5
4 4 5 5 10 10 10 10 14 14
4
24
9
5
12

Output 0
0
200
4
0
15

----

Example 1
Input 1
10 4
0 0 0 6 18 18 18 20 20 20
40
19
1
26

Output 1
456
126
0
264
----

Please don't give example usage. Accommodate for user input. Think through the given problem and take note of the given example inputs, output, think and reason before answering.
'''

