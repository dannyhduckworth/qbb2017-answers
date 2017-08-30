#!/usr/bin/env python

#Convert linear search into a binary search

nums = range(0,100,10)
print nums

        
key = 10
lo = 0
hi = len(nums)

while lo < hi:
    mid_inx = (lo+hi) / 2
    mid = nums[mid_inx] #??
    
 
    if (mid == key):
        print "Found at %d==%d at %d" % (key, mid, mid_inx)
        break
    elif (key > mid):
        lo = mid_inx + 1
    else:
        hi = mid_inx
   
   

   

    