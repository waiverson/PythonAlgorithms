# encoding:utf-8



class Sorting():

    def __init__(self):
        pass

    # sorts a sequence in ascending order using the bubble sort algorithm 冒泡
    @staticmethod
    def bubble_sort(the_seq):
        n = len(the_seq)
        # perform n-1 bubble operations on the sequence
        for i in range(n-1):
            # bubble the largest item to the end
            for j in range(n - 1 - i):
                if the_seq[j] > the_seq[j+1]:
                    tmp = the_seq[j]
                    the_seq[j] = the_seq[j+1]
                    the_seq[j+1] = tmp

        print the_seq

    """
    # sorts a sequence in ascending order using the selection sort algorithm 选择排序
    The process starts by finding the smallest value in the sequence and swaps it with
    the value in the first position of the sequence. The second smallest value is then
    found and swapped with the value in the second position. This process continues positioning
    each successive value by selecting them from those not yet sorted and swapping with the values
    in the respective positions.
    """

    @staticmethod
    def selection_sort(the_seq):
        n = len(the_seq)
        for i in range(n-1):
            # assume the ith element is the smallest
            smallNdx = i
            # determine if any other element contains a smaller value
            for j in range(i+1, n):
                if the_seq[j] < the_seq[smallNdx]:
                    smallNdx = j

            # swap the ith value and smallNdx value only if the smallest value is
            # not already in its proper position. some implementations omit testing
            # the condition and always swap the two values

            if smallNdx != i:
                tmp = the_seq[i]
                the_seq[i] = the_seq[smallNdx]
                the_seq[smallNdx] = tmp
        print the_seq

    # 插入排序
    # sorts a sequence in ascendig order using the insertion sort algorithm
    @staticmethod
    def insertion_sort(the_seq):
        n = len(the_seq)
        # starts with the first item as the only sorted entry
        for i in range(1, n):
            # save the value to be positioned
            value = the_seq[i]
            # find the position where value fits in the ordered part of the list
            pos = i
            while pos > 0 and value < the_seq[pos - 1]:
                # shift the items to the right during the search
                # 循环和前一个进行比较，直到找到自己的位置
                the_seq[pos] = the_seq[pos - 1]
                pos -= 1

            # put the saved value into the open slot
            the_seq[pos] = value
        print the_seq


    # merges two sorted lists to create and return a new sorted list
    @staticmethod
    def merge_sorted_lists(listA, listB):
        # create the new list and init the list markers
        new_list = list()
        a = 0
        b = 0

        # merge the two lists together until one is empty
        while a < len(listA) and b < len(listB):
            if listA[a] < listB[b]:
                new_list.append(listA[a])
                a += 1
            else:
                new_list.append(listB[b])
                b += 1

        # if listA contains more items, append them to newlist
        while a < len(listA):
            new_list.append(listA[a])
            a += 1

        # or if listb contains more items, append them to newlist
        while b < len(listB):
            new_list.append(listB[b])
            b += 1

        return new_list







if __name__ == "__main__":

    Sorting.bubble_sort([1,2,7,10,3,9,3,4,2,1,4,5,3,6,3])
    Sorting.selection_sort([1,2,7,10,3,9,3,4,2,1,4,5,3,6,3])
    Sorting.insertion_sort([1,2,7,10,3,9,3,4,2,1,4,5,3,6,3])
