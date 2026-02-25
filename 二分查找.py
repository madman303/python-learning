#二分查找经典例题

def binary_search(arr,target):
    """
    在有序数组arr中查找target
    :param arr:有序数组（升序）
    :param target:序列中的目标值
    :return:目标值的索引，查找失败就返回-1
    """
    left = 0  #左边界指针，指向数组中第一个元素
    right = len(arr) - 1   #右边界指针，指向数组最后一个位置
    step = 0  #记录查找步长

    print(f"开始查找目标值：{target}")
    print("=" * 40)

    #当左边界 <= 右边界时，说明查找区间不为空
    while left <= right:
        step += 1
        #计算中间位置，防止left + right导致整数太大而溢出
        mid = left + (right - left)//2
        guess = arr[mid]

        print(f"第{step}步查找中间值：{guess},区间：[{left},{right}]")

        #判断guess数字所在区间
        if guess == target:
            print("找到目标数字target")
            return mid
        elif guess > target:
            print("猜大了，目标值在左半部分")
            right = mid - 1
        else:
            print("猜小了，目标值在右半部分")
            left = mid + 1

    print("没找到目标值:{target},共查找{step}步")
    return -1


#---测试代码---
if __name__ =="__main__":
    #测试数组
    nums = [1,3,5,7,9,11,13,15]
    target = 7

    #调用函数
    result = binary_search(nums,target)

    #最终结果
    print("=" * 40)
    if result != -1:
        print(f"结果：目标值{target}在数组中的索引是{result}")
    else:
        print(f"结果：数组中没有目标值{target}")