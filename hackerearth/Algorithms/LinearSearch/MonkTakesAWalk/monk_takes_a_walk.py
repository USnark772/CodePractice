"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Section: Algorithms
Subsection: Searching
Type: Linear Search
Problem: Monk Takes a Walk.

Description:
    Today, Monk went for a walk in a garden. There are many trees in the garden and each tree has an English alphabet
    on it. While Monk was walking, he noticed that all trees with vowels on it are not in good state. He decided to
    take care of them. So, he asked you to tell him the count of such trees in the garden.
    Note : The following letters are vowels: 'A', 'E', 'I', 'O', 'U' ,'a','e','i','o' and 'u'.

Input:
    The first line consists of an integer T denoting the number of test cases.
    Each test case consists of only one string, each character of string denoting the alphabet
    (may be lowercase or uppercase) on a tree in the garden.

Output:
For each test case, print the count in a new line.

Constraints:
1 <= T <= 10
1 <= length of string <= 10^5

Sample input:
2
nBBZLaosnm
JHkIsnZtTL

Sample output:
2
1

Explanation:
In test case 1, a and o are the only vowels. So, count=2

My Thoughts:
Each tree has one letter on it.
If letter is vowel, count.
"""

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']


def calculate(line: str) -> int:
    """
    Calculate the number of vowels in the given string.
    :param line: The given string.
    :return int: The number of vowels.

    >>> calculate("nBBZLaosnm")
    2

    >>> calculate("JHkIsnZtTL")
    1
    """
    ret = 0
    for char in line:
        if char in vowels:
            ret += 1
    return ret


def main():
    """
    Get user input, calculate result, print result.
    """
    num_tests = int(input())
    for i in range(num_tests):
        line = input()
        res = calculate(line)
        print(res)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
