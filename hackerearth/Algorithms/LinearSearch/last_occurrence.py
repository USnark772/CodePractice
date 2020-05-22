"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Problem: Last Occurrence (tutorial practice problem).

Description:
You have been given an array of size N consisting of integers. In addition you have been given an element M you need
 to find and print the index of the last occurrence of this element M in the array if it exists in it, otherwise print
  -1. Consider this array to be 1 indexed.

Input Format:
The first line consists of 2 integers N and M denoting the size of the array and the element to be searched for in the
 array respectively . The next line contains N space separated integers denoting the elements of of the array.

Output Format
Print a single integer denoting the index of the last occurrence of integer M in the array if it exists, otherwise
 print -1.

Constraints:
1 <= N <= 10^5
1 <= M <= 10^9
1 <= A[i] <= 10^9
"""


def calculate(length: int, target: int, nums: list) -> int:
    """
    Calculate the index of last occurrence of target in nums.
    :param length: The length of nums list.
    :param target: The target to search for in nums list.
    :param nums: The nums list.
    :return int: The index or -1 if no occurrence of target in nums list.
    """
    ret = -1
    for i in range(length):
        if nums[i] == target:
            ret = i + 1
    return ret


def parse_input(lines: list) -> (int, int, list):
    """
    Parse list of user input lines into integers specific to this problem. Assuming there are two lines
    Line one has two space separated integers.
    Line two has a variable number of space separated integers.
    :param lines: The list of user input lines assumed to be strings.
    :return (int, int, list): (length of list, target number, list of numbers).
    """
    line_one = lines[0]
    line_two = lines[1]
    n, m = line_one.split(" ")
    list_len = int(n)
    target_num = int(m)
    str_list = line_two.split(" ")
    num_list = [int(x) for x in str_list]
    return list_len, target_num, num_list


def get_input(num_lines: int) -> list:
    """
    Get lines of user input equal to num_lines.
    :param num_lines: The number of lines to get from the user.
    :return list: A list of user input lines.
    """
    lines = list()
    for i in range(num_lines):
        lines.append(input())
    return lines


def main():
    """
    Get user input, calculate result, print result.
    """
    lines = get_input(2)
    args = parse_input(lines)
    res = calculate(*args)
    print(res)


if __name__ == '__main__':
    main()
