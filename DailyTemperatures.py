from typing import List, Dict, Tuple, Optional


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """ Given an array of daily temperatures, for each day i find the number of days
    you need to wait to get the next higher tempature than temperatures[i]"""
    answers  = [0]*len(temperatures)
    stack = []
    for i,tmp in enumerate(temperatures):
        while stack and stack[-1][0] < tmp:
            # find next higher tmp for top element in stack
            tmp_curr, j = stack.pop()
            answers[j] = i - j
        stack.append((tmp, i))
    return answers





