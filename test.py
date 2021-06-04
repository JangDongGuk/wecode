def test(nums):
    result=[]
    for nums in range(51):
        if nums % 2 == 0:
           result.append(nums)
           
    return result

a = test(range(51))

print(a)

   
    