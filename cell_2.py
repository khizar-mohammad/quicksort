#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def quicksort(lst):
    # Quicksort algorithm without recursion
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in range(1, len(lst)):
            if lst[i] < pivot:
                left.append(lst[i])
            else:
                right.append(lst[i])
            print(left)
            print(right)
        return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([67423,123,777,893,9,2,1,1,0]))

