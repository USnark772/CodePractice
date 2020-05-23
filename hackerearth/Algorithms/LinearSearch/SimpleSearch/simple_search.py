"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Problem: Simple Search

Description:
    Given a list of distinct N numbers a_1,a_2,a_3........a_n. Find the position of number K in the given list.

Input Format:
    First line takes input value of N.
    Second line takes input N space separated integer value.
    Third line takes input value of K.

Output Format:
Position of K in the given list

Constraints
0 < N < 100001
0 < a_i < 1010
0 < K < 1010

NOTE:
Array Indexing Starts From 0

Sample input:
5
1 2 3 4 5
4

Sample output:
3
"""


def calculate(n: int, nums: list, k: int) -> int:
    """
    Calculate the index of the given value in the list of numbers.
    :param n: The number of numbers in the list.
    :param nums: The list of numbers.
    :param k: The value to search for.
    :return int: The index of the value in the list.

    >>> calculate(5, [1, 2, 3, 4, 5], 4)
    3
    """
    # Could just return nums.indexOf(k) but that would be just way to simple.
    for i in range(n):
        if nums[i] == k:
            return i
    return -1


def parse_input(lines: list) -> (int, list, int):
    """
    Parse three lines from user into usable format.
    Line one: integer.
    Line two: list of integers.
    Line three: integer.
    :param lines: The lines to parse.
    :return (int, list, int): (n, nums, k).
    """
    n = int(lines[0])
    line_two = lines[1].split(" ")
    nums = [int(x) for x in line_two]
    k = int(lines[2])
    return n, nums, k


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
    lines = get_input(3)
    # lines = list()
    # with open(os.path.dirname(__file__) + "/input17.txt", "r") as test_input:
    #     for line in test_input.readlines():
    #         lines.append(line)
    args = parse_input(lines)
    res = calculate(*args)
    print(res)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
