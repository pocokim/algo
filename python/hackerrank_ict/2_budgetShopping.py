#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'budgetShopping' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY bundleQuantities
#  3. INTEGER_ARRAY bundleCosts
#

def budgetShopping(n, bundleQuantities, bundleCosts):
    return explore(n,0,0,bundleQuantities,bundleCosts)

def explore(budget,curBdQ,curBdC,bundleQuantities,bundleCosts):
    for i in range(len(bundleCosts)):
        
        curValue = explore(budget,curBdQ+bundleQuantities[i],curBdC+bundleCosts[i],bundleQuantities,bundleCosts)
    


        


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    bundleQuantities_count = int(input().strip())

    bundleQuantities = []

    for _ in range(bundleQuantities_count):
        bundleQuantities_item = int(input().strip())
        bundleQuantities.append(bundleQuantities_item)

    bundleCosts_count = int(input().strip())

    bundleCosts = []

    for _ in range(bundleCosts_count):
        bundleCosts_item = int(input().strip())
        bundleCosts.append(bundleCosts_item)

    result = budgetShopping(n, bundleQuantities, bundleCosts)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()