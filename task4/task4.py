def min_steps(filepath):
    nums = []
    with open(filepath, 'r') as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            nums.append(int(line[0]))
    nums.sort()
    lenght = len(nums)
    if lenght % 2:
        median = nums[lenght // 2 + lenght % 2]
    else:
        median = nums[lenght // 2]
    steps = 0
    for number in nums:
        steps += abs(median - number)
    return steps


if __name__ == '__main__':
    filepath = input()
    steps = min_steps(filepath)
    print(steps, end='\n')
