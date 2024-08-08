# example 1:
# [1,3,5,7,8]  target = 10
# output [3,7]

# example 2:
# [2,4,5,7] target = 3
# output "無解"

# eample 3:
#[3,3] traget = 6
# output [3,3]


def solution(nums:list, target: int):
    len = nums.__len__()
    for i in range(len):
        x = target - nums[i] # 要的數字
        for j in range(i+1,len):
            if nums[j] == x:
                return [nums[i],x]

    return "無解"
    



sol=solution([1,7,3,5,8,7],15)

print(sol)