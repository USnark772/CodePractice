"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Section: Algorithms
Subsection: Searching
Type: Linear Search
Problem: Easy Sum Set Problem

Description:
    In this problem, we define "set" is a collection of distinct numbers. For two sets A and B, we define their sum set
    is a set S(A,B) = {a+b|a e A,b e B). In other word, set S(A,B) contains all elements which can be represented as
    sum of an element in A and an element in B. Given two sets A,C, your task is to find set B of positive integers
    less than or equals 100 with maximum size such that S(A,B) = C. It is guaranteed that there is unique such set.

Input Format:
    The first line contains N denoting the number of elements in set A, the following line contains N space-separated
    integers a_i denoting the elements of set A.

    The third line contains M denoting the number of elements in set C, the following line contains M space-separated
    integers c_i denoting the elements of set C.

Output Format:
    Print all elements of B in increasing order in a single line, separated by space.

Constraints:
    1 <= N, M <= 100
    1 <= a_i, c_i <= 100

Sample input:
    2
    1 2
    3
    3 4 5

Sample output:
    2 3

Explanation:
    If e is an element of set B, then e + 2 is an element of set C, so we must have e <= 3. Clearly, e cannot be 1
    because 1 + 1 = 2 is not an element of set C. Therefore, B = {2,3}.
"""
import os

doc_testing = False
use_file = False


def calculate(n: int, m: int, a: list, c: list) -> list:
    """
    Calculate the set B from the sets A and C.
    First find range of set B using largest and smallest values in A and C.
    Second test each number in range to see if valid value for B.
    :param n: The number of elements in a.
    :param m: The number of elements in c.
    :param a: The set A.
    :param c: The set C.
    :return list: The sorted set B.

    >>> calculate(2, 3, [1, 2], [3, 4, 5])
    {2, 3}
    """
    ret = set()
    biggest = abs(max(a) - max(c))
    smallest = abs(min(a) - min(c))
    ret.add(smallest)
    ret.add(biggest)
    for i in range(smallest + 1, biggest):
        passes = True
        for e in a:
            if not i + e in c:
                passes = False
        if passes:
            ret.add(i)
    return sorted(ret)


def parse_input(lines: list) -> (int, int, list, list):
    """
    Parse input with respect to this problem.
    :param lines: The user input to parse.
    :return (int, int, list, list): (N, M, a, c)
    """
    N = int(lines[0])
    a_str = lines[1].split(" ")
    a = [int(x) for x in a_str]
    M = int(lines[2])
    c_str = lines[3].split(" ")
    c = [int(y) for y in c_str]
    return N, M, a, c


def get_input(num_lines: int) -> list:
    """
    Get lines of user input equal to num_lines.
    :param num_lines: The number of lines to get from the user.
    :return list: A list of user input lines.
    """
    lines = []
    for i in range(num_lines):
        lines.append(input())
    return lines


def main():
    """
    Get user input, calculate result, print result.
    """
    if use_file:
        lines = list()
        with open(os.path.dirname(__file__) + "/input2.txt", "r") as test_input:
            for line in test_input.readlines():
                lines.append(line)
    else:
        lines = get_input(4)
    args = parse_input(lines)
    res = calculate(*args)
    to_print = ""
    for e in res:
        to_print += str(e) + " "
    to_print = to_print[:len(to_print) - 1]
    print(to_print)


if __name__ == '__main__':
    if doc_testing:
        import doctest
        doctest.testmod()
    else:
        main()
