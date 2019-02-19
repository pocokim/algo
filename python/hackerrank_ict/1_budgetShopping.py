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
    # Write your code here
    buyingNotes = 0
    money = 0
    gsb = []

    for i in range(len(bundleCosts)):
            gsb.append(bundleCosts[i]/bundleQuantities[i])
            print(gsb)

    i = gsb.index(min(gsb))

    while True :
        

        n -= bundleCosts[i]
        buyingNotes += bundleQuantities[i]
        print('현재까지 구매한 노트수 :',buyingNotes,'남아있는돈: ',n)
        if n < min(bundleCosts):
            break;


    return buyingNotes    



        

    while( n > min(bundleCosts)):
        

        n -= bundleCosts[i]
        buyingNotes += bundleQuantities[i]
        print('현재까지 구매한 노트수 :',buyingNotes,'남아있는돈: ',n)
    
    # return buyingNotes

    


        


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