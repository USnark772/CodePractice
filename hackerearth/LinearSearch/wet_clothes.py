"""
Author: Phillip Riskin
Date: 2020
Project: hackerearth.com practice.
Problem: Wet Clothes

Description:
    We have m completely wet clothes out under sunshine waiting to become dry. we are now at second t_1 and it's
    raining. It's going to rain again on seconds t_2...t_n and after each rain clothes will be completely wet again.
    Cloth number i needs a_i seconds to become dry. We can go out and collect all dry clothes at any moment but can't
    do this more than g times. What is the maximum number of clothes we can collect until second t_n? Note that the
    duration of each rain is almost zero, so we can ignore it. Also collecting clothes does not take any time from us.

Input format:
    First line of input contains three integers n, m, g (2<=n<=100, 1<=m,g<=100) respectively. In the second line will
    be n increasing numbers denoting t_1...t_n (0 <= t_1 < ... < t_n <= 10^4). In the Last line will have m numbers
    denoting a_1...a_n (1 <= a_i <= 10000).

Output format:
    In a single line print maximum number of clothes we can collect.

Sample input:
3 3 2
3 5 8
4 1 3
Sample output:
2

Explanation:
    In the sample, first we go outside at time 5(exactly before rain) and take second piece of clothes.
    Then for the second time, at second 8, we go and take the third piece.


My thoughts:
t_k is a point in time at which it will rain.
a_k is the time it will take garment k to dry.
n is the number of times it will rain.
m is the number of garments on the line.
g is the number of attempts we have to get dry garments from the line.
"""


def calculate(num_rains: int, num_garments: int, num_tries: int, rain_times: list, dry_times: list) -> int:
    """
    Calculate the number of dry garments retrievable from the line given the parameters.
    First calculate the time each break in rain is.
    Second remove each garment that we can from longest break to shortest break.
    :param num_rains: The number of times it will rain.
    :param num_garments: The number of garments on the line.
    :param num_tries: The number of tries to get dry garments.
    :param rain_times: A list of times at which it will rain.
    :param dry_times: A list of times it takes each garment to dry.
    :return int: The number of dry garments we can retrieve from the line.
    """
    retrieved = 0
    tried = 0
    rain_breaks = list()
    for i in range(1, num_rains):
        rain_breaks.append(rain_times[i] - rain_times[i - 1])
    for i in range(len(rain_breaks)):
        longest_break = max(rain_breaks)
        if longest_break < 0:
            break
        if tried == num_tries:
            break
        rain_breaks[rain_breaks.index(longest_break)] = -1
        to_remove = list()
        for b in range(len(dry_times)):
            if dry_times[b] < longest_break:
                to_remove.append(i)
        retrieved += len(to_remove)
        for a in to_remove:
            del dry_times[a]
    return retrieved


def parse_input(lines: list) -> (int, int, int, list, list):
    """
    Parse list of user input lines into integers specific to this problem. Assume there are three lines.
    Line one has three space separated numbers.
    Line two has a variable number of space separated numbers.
    Line three has a variable number of space separated numbers.
    :param lines: The list of user input lines assumed to be strings.
    :return (int, int, int, list, list): (n, m, g, t, a)
    """
    line_one = lines[0]
    line_two = lines[1]
    line_three = lines[2]
    n, m, g = line_one.split(" ")
    n, m, g = int(n), int(m), int(g)
    t_strings = line_two.split(" ")
    t = [int(x) for x in t_strings]
    a_strings = line_three.split(" ")
    a = [int(y) for y in a_strings]
    return n, m, g, t, a


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
    # lines = get_input(3)
    lines = ["3 3 2", "3 5 8", "4 1 3"]
    args = parse_input(lines)
    res = calculate(*args)
    print(res)


if __name__ == '__main__':
    main()
