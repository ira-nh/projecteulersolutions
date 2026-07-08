# Multiples of 3 or 5

## Find the sum of all numbers below 1000 that are multiples of 3 or 5

## Brute force method:

I looped through every number from 0 to 1000.
For each number:
- Check if divisible by 3 or 5.
- Add it to total if it is.
- Subtract common numbers (i.e. multiples of 15).

## Mathematical approach:

Multiples form an arithmetic sequence.
The sum of an arithmetic sequence is:
S = ((no. of terms) * (first_term + last_term)) / 2
OR
S = n(a+l)/2

For multiples of 3:
n = 999/3 = 333
S = 333(3 + 999)/2

For multiples of 5:
n = 1000/5 = 200
S = 200(5+1000)/2 

Since multiples of 15 would be counted twice, they need to be subtracted.

So the final formula would be sum(3s) + sum(5s) - sum(15s)

Unlike the brute force method, the mathematical solution doesn't require checking every number.