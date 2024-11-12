Think through the given problem and take note of the given example inputs, output and answer in python. Think and reason to understand the question first. Then reason through an algorithm to solve the problem. Them give the answer.


Time limit: 2500 ms
Memory limit: 256 MB

Alice and Bob play the following game:

Each of them has some initial amounts of red stones and blue stones (they know each other's amounts).
The game is played in turns. A turn consists of several steps, as described below. In a turn, Alice and Bob will take on two roles, A and B.
At the first turn, Alice will take on the role of A and Bob will take on the role of B. For the next turns, they will start alternating the roles. So at the second turn, Alice will take on the role of B and Bob on the role of A.
A turn consists of the following steps:
Player A chooses a color (red or blue), writes it down on a piece of paper, and puts it on the table in a way that player B can't see what's written.
Player B then tries to guess the color written down. Let's call the guessed color X.
If B guesses correctly, player A loses one stone of color X; otherwise, player B loses one stone of color X.
The game ends when one player loses their last stone of any color, as they lose immediately.
Your task is to calculate the probability of Alice winning the game if both players are trying to maximize their probability of winning regardless of their opponent's moves.

Standard input
The first line contains two integers, R₁ and B₁, representing the number of red and blue stones for Alice, followed by another two integers, R₂ and B₂, representing the number of red and blue stones for Bob.

Standard output
Output one number - the probability of Alice winning the game, represented as a real number. Your answer will be accepted if the relative or absolute error is less or equal to 10⁻⁶.

Constraints and notes
1 ≤ R₁, R₂, B₁, B₂ ≤ 40

----
Example 0 
Input  0
1 1 1 1

Output 0
0.5

----
Example 1
Input 1
1 2 3 4

Output 1
0.071428571
----

Please don't give example usage. Accommodate for user input. Think through the given problem and take note of the given example inputs, output, think and reason before answering.
