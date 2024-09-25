
"""
Group 36
Tiffany Whitsett U90321785
Micaela Arlo-Gil
"""

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
    nums1.sort()
    nums2.sort()
    x,y = 0,0
    intersect = []
    while x < len(nums1) and y < len(nums2):
        if nums1[x] == nums2[y]:
            intersect.append(nums1[x])
            x += 1
            y += 1
        elif nums1[x] < nums2[y]:
            x += 1
        else:
            y += 1
    return intersect


matrix1 = [[22, 19, 49, 69, 71, 47, 93],
               [41, 23, 16, 74, 71, 67, -5],
               [28, 5, 70, -9, 66, 38, 49]]

matrix2= [[-9, 34, 56, 43, 29, 71, 31],
               [19, 76, 7, 21, 39, 24, 45],
               [94, -8, 88, 75, 92, 83, 55]]


#question4(3, 'A', 'B', 'C')
#print(question5([-5, 4, 5, 8, 23, 24, 45, 55, 69, 72, 81, 91, 92, 96, 99], 0, 23 ,4))
#print(ec([1,2, 2, 1], [2,2]))

