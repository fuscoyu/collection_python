def binary_search(array, target): # 二分查找
    if not array:
       return -1
    beg, end = 0, len(array)
    while beg < end:
        mid = beg + (end - beg) // 2
        if array[mid] == target:
           return mid
        elif array[mid] > target:
           end = mid
        else:
           beg = mid + 1
    return -1

# 要求: array list 是顺序的

def test():
   """
   如何设计测试用例：
   - 正常值功能测试
   - 边界值（比如最大最小，最左最右值）
   - 异常值（比如None，空置， 非法值）
   """
   # 正常值功能测试 包含有无两种结果
   assert binary_search([0,1,2,3,4,5], 1) == 1
   assert binary_search([0,1,2,3,4,5], 6) == -1
   assert binary_search([0,1,2,3,4,5], -1) == -1
   
   # 边界值
   assert binary_search([0,1,2,3,4,5], 0) == 0
   assert binary_search([0,1,2,3,4,5], 5) == 5
   assert binary_search([0], 0) == 0

   # 异常值
   assert binary_search([], 1) == -1


