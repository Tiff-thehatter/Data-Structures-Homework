import unittest
from solution import *
"""
    Write your main code for each question in the specified functions
    as they will be used for unit testing. You can define other functions
    to modularize your code but remember that the following functions are the
    ones that are called by our tester.

    ** Do not change the name of the file to anything else.
"""

def question3(matrix1, matrix2):

    """
        You are given two matrices where each is of format: list of list: For example,
            A 2x4 matrix:
                        [[1,2,3,4],
                         [4,1,0,12]]
            A 3x3 matrix:
                        [[1,2,-3],
                         [4,1,0],
                         [-1,11,5]]

        Given a matrix in above form, you can figure out the dimensions using the len().
        You are required to return the sum of the two matrices as a list of list in the same format.
        Moreover, it is guaranteed that the both matrices have the same dimensions.
        #cij = aij + bij
    """
    matrix0 = []


    while len(matrix1) == len(matrix2):
        for i in range(len(matrix1)):
            row =[]

            for j in range(len(matrix1[0])):
                a = matrix1[i][j]
                b = matrix2[i][j]
                c = a + b
                row.append(c)
            matrix0.append(row)
        return matrix0











def question4(n, tower1, tower2, tower3):
    """
        n: denotes number of disks

        Return the instructions for moving the disks as a list of string instead of printing:
        return ["Disk 1 moved from A to C",
                "Disk 2 moved from A to B",
                .... ]
    """



    if n == 1:
        return [f"Disk 1 moved from {tower1} to {tower2}"]


    steps = []
    steps += question4(n - 1, tower1, tower3, tower2)

    # Move the nth disk from tower1 to tower2
    steps.append(f"Disk {n} moved from {tower1} to {tower2}")

    # Move n-1 disks from tower3 to tower2 using tower1 as auxiliary
    steps += question4(n - 1, tower3, tower2, tower1)

    return steps

#or

    list = []

    if n == 1:
        list.append("Disk 1 moved from {tower1} to {tower2}")
    else:
        question4(n - 1, tower1, tower3, tower2)
        list.append(f"Disk {n} moved from {tower1} to {tower2}")
        question4(n -1, {tower3}, {tower2}, {tower1})

    question4(n, tower1, tower2, tower3)    
    return list





def question5(numbers, start, end, target):
    """
        You are given a list of numbers and a target number to search for.
        start and end indices are the indices of the start and end of list. They have been provided so you can implement the recursive function

        Return the index of the target if it exists, otherwise, return -1
    """

    if start > end:
        return -1

    mid = (start + end) // 2
    if numbers[mid] < target:
        return question5(numbers, mid + 1, end, target)
    elif numbers[mid] > target:
        return question5(numbers, start, mid - 1, target)
    return mid


def ec(nums1, nums2):
    """
        You are given two lists of numbers.
        Return the intersection of those as a list of numbers
    """
    return []

matrix1 = [[22, 19, 49, 69, 71, 47, 93],
               [41, 23, 16, 74, 71, 67, -5],
               [28, 5, 70, -9, 66, 38, 49]]

matrix2= [[-9, 34, 56, 43, 29, 71, 31],
               [19, 76, 7, 21, 39, 24, 45],
               [94, -8, 88, 75, 92, 83, 55]]
question3(matrix1,matrix2)


#question5(numbers, start, end, target)


class TestClass(unittest.TestCase):
    def test_1_q3(self):
        m11 = [[22, 19, 49, 69, 71, 47, 93],
               [41, 23, 16, 74, 71, 67, -5],
               [28, 5, 70, -9, 66, 38, 49]]

        m12 = [[-9, 34, 56, 43, 29, 71, 31],
               [19, 76, 7, 21, 39, 24, 45],
               [94, -8, 88, 75, 92, 83, 55]]

        s1 = [[13, 53, 105, 112, 100, 118, 124],
              [60, 99, 23, 95, 110, 91, 40],
              [122, -3, 158, 66, 158, 121, 104]]

        if question3(m11, m12) != s1:
            print("Q3 Failed / Test 1")
            return

        m21 = [[36], [0], [-7]]
        m22 = [[89], [83], [53]]
        s2 = [[125], [83], [46]]

        if question3(m21, m22) != s2:
            print("Q3 Failed / Test 2")
            return

        m31 = [[-3, -8, 89, -1, 23],
               [20, 80, 15, 89, 25],
               [85, 35, 72, 78, 30],
               [45, 28, 1, 10, -10],
               [28, 34, 55, 19, 83],
               [42, 48, 86, 57, -3],
               [12, 76, 49, -5, 96]]


        m32 = [[14, 17, 87, 29, 36],
               [15, 59, 92, 33, 53],
               [9, 25, 38, 43, 81],
               [9, 3, 48, 15, 85],
               [-9, 64, 84, 44, 69],
               [21, 41, 83, 51, 48],
               [84, 85, 36, 33, 49]]

        s3 = [[11, 9, 176, 28, 59],
              [35, 139, 107, 122, 78],
              [94, 60, 110, 121, 111],
              [54, 31, 49, 25, 75],
              [19, 98, 139, 63, 152],
              [63, 89, 169, 108, 45],
              [96, 161, 85, 28, 145]]

        if question3(m31, m32) != s3:
            print("Q3 Failed / Test 3")
            return

        print("Q3 Passed")


    def test_2_q4(self):
        script = ['Disk 1 moved from A to B',
                  'Disk 2 moved from A to C',
                  'Disk 1 moved from B to C',
                  'Disk 3 moved from A to B',
                  'Disk 1 moved from C to A',
                  'Disk 2 moved from C to B',
                  'Disk 1 moved from A to B']

        if question4(3, 'A', 'B', 'C') != script:
            print("Q4 Failed")
            return

        print("Q4 Passed")


    def test_3_q5(self):
        testcases = [ ([-5, 4, 5, 8, 23, 24, 45, 55, 69, 72, 81, 91, 92, 96, 99], 23 ,4),
                      ([-7, 9, 13, 26, 27, 48, 51, 52, 71, 74, 75, 83, 84, 91, 94], 91, 13),
                      ([-10, -1, 2, 17, 22, 31, 35, 42, 45, 54, 57, 79, 82, 88, 96], 178, -1)]

        for t in testcases:
            if question5(t[0], 0, len(t[0]) - 1, t[1]) != t[2]:
                print("Q5 Failed")
                return
        print("Q5 Passed")


    def test_4_ec(self):
        testcases = [([1,2, 2, 1], [2,2], [2,2]),
                     ([9,4,9,8,4], [4,9,5], [4,9]),
                     ([2], [0], [])]

        for t in testcases:
            if sorted(ec(t[0], t[1])) != sorted(t[2]):
                print("EC Failed")
                return
        print("EC Passed")


if __name__=='__main__':
    unittest.main(verbosity=0)
