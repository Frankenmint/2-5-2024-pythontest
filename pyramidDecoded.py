#!/usr/env python3

import math

def decode(file):
    def read_file_into_dictionary(filename):
        result = {}
        with open(filename, 'r') as file:
            for line in file:
                # Split each line by space
                parts = line.strip().split()
                result[parts[0]] = parts[1]
        return result
    def triangular_number(n):
        return (n * (n + 1)) // 2

    def rows_in_pyramid(X):
        n = (-1 + math.sqrt(1 + 8*X)) / 2
        return int(n)

    rawData = read_file_into_dictionary("./strings.txt")
    rows = rows_in_pyramid(len(rawData))
    last_number_in_row = triangular_number(rows)
    # print(f"Number of rows: {rows}")
    # print(f"Last number in row: {last_number_in_row}")
    # print(rawData)

    for i in range(rows):
        if i == 0:
            continue
        print(rawData[str(triangular_number(i))], end=" ")

decode("./strings.txt")