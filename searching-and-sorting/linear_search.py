__author__ = 'abear'


class LinearSearch:

    def __init__(self):
        pass

    @staticmethod
    def linear_search(the_values, target):

        n = len(the_values)
        for i in range(n):
            if the_values[i] == target:
                return True

        return False

    @staticmethod
    def sorted_linear_search(the_values, item):
        n = len(the_values)
        for i in range(n):
            # if the target is found in the ith element, return True
            if the_values[i] == item:
                return True
            # if target is larger than the ith element, it's not in the sequence
            elif the_values[i] > item:
                return False

        return False

    @staticmethod
    def find_smallest(the_values):
        n = len(the_values)
        # assume the first item is the smallest value
        smallest = the_values[0]
        # determine if any other item in the sequence is smaller
        for i in range(1, n):
            if the_values[i] < smallest:
                smallest = the_values[i]
        # return the smallest found
        return smallest

    @staticmethod
    def binary_search(the_values, target):
        # start with the entire sequence of elements
        low = 0
        high = len(the_values)-1

        # repeatedly subdivide the sequence in half until the target is found
        while low <= high:
            # find the midpoint contain the target?
            mid = (low + high)/2
            # Does the midpoint contain the target?
            if the_values[mid] == target:
                return True
            # or does the target precede the midpoint?
            elif target < the_values[mid]:
                high = mid - 1
            # or does it follow the midpoint?
            else:
                low = mid + 1

        # if the sequence cannot be subdivided further, we're done
        return False





