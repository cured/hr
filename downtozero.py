#!/bin/python3

from dataclasses import dataclass
import os
import sys
from math import sqrt


def generate():
    limit = 1000000
    steps = [-1] * (limit + 1)

    steps[0], steps[1], steps[2], steps[3] = 0, 1, 2, 3

    for i in range(limit):
        if steps[i] == -1 or steps[i] > steps[i - 1] + 1:
            steps[i] = steps[i - 1] + 1

        for j in range(2, i+1):
            if i * j > limit:
                break
            if steps[i * j] == -1 or steps[i * j] > steps[i] + 1:
                steps[i * j] = steps[i] + 1

    return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = generate()
    q = int(input())

    for q_itr in range(q):
        n = int(input())
        result = steps[n]
        fptr.write(str(result) + '\n')

    fptr.close()
