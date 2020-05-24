"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Section: Algorithms
Subsection: Searching
Type: Linear Search
Problem: Maximum Sum

Description:
    You are given an array of integers A, you need to find the maximum sum that can be obtained by picking some
    non-empty subset of the array. If there are many such non-empty subsets, choose the one with the maximum number of
    elements. Print the maximum sum and the number of elements in the chosen subset.

Input:
    The first line contains an integer N, denoting the number of elements of the array. Next line contains N
    space-separated integers, denoting the elements of the array.

Output:
    Print 2 space-separated integers, the maximum sum that can be obtained by choosing some subset and the maximum
    number of elements among all such subsets which have the same maximum sum.

Constraints:
    1 <= N <= 10^5
    -10^9 <= A_i <= 10^9

Sample input:
5
1 2 -4 -2 3

Sample output:
6 3

Explanation:
The chosen subset is {1, 2, 3}

My thoughts:
for number in array:
    if negative:
        add to negative num set.
    if non-negative:
        add to non-negative num set.
if non-negative set is not empty:
    add all nums in non-negative set
    return sum and num nums
else if negative set not empty:
    add all nums in negative set
    return sum and num nums
else
return default 0, 0

Apparently this problem is worded incorrectly. Subset by definition does not have repeated elements but this
problem expects "subsets" to have repeated elements, therefore it is required to use lists instead of sets.
"""
import os

num_input_lines = 2


def calculate(n: int, nums: list) -> (int, int):
    """
    Calculate the maximum sum obtainable by any subset of the given list.
    Also calculate the number of elements in the chosen subset.
    :param n: The length of the given list.
    :param nums: The given list.
    :return (int, int): (max sum, num elements in subset).

    >>> calculate(5, [1, 2, -4, -2, 3])
    (6, 3)
    """
    neg_set = list()
    non_neg_set = list()
    for num in nums:
        if num < 0:
            neg_set.append(num)
        else:
            non_neg_set.append(num)
    set_sum = 0
    num_elements = 0
    if len(non_neg_set) > 0:
        for element in non_neg_set:
            set_sum += element
            num_elements += 1
    elif len(neg_set) > 0:
        set_sum = max(neg_set)
        num_elements = 1
    return set_sum, num_elements


def parse_input(lines: list) -> (int, list):
    """
    Parse two user lines.
    Line one: The number of nums.
    Line two: The nums.
    :param lines: The lines to parse.
    :return (int, list): (n, nums).
    """
    n = int(lines[0])
    line_two = lines[1].split(" ")
    nums = [int(x) for x in line_two]
    return n, nums


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
    lines = get_input(num_input_lines)
    # lines = list()
    # with open(os.path.dirname(__file__) + "/input1.txt", "r") as test_input:
    #     for line in test_input.readlines():
    #         lines.append(line)
    args = parse_input(lines)
    list_sum, element_num = calculate(*args)
    print(list_sum, element_num)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
