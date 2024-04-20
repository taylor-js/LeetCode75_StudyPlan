# https://leetcode.com/problems/combination-sum-iii/?envType=study-plan-v2&envId=leetcode-75

def find_combinations(k, n):
    def backtrack(start, remain, path):
        if remain == 0 and len(path) == k:
            result.append(path[:])
            return
        elif remain < 0 or len(path) > k:
            return
        for i in range(start, 10):
            path.append(i)
            backtrack(i+1, remain-i, path)
            path.pop()
    result = []
    backtrack(1, n, [])
    return result

if __name__ == "__main__":
    fc1 = find_combinations(3, 7)
    print(fc1)
    fc2 = find_combinations(3, 9)
    print(fc2)
    fc3 = find_combinations(4, 1)
    print(fc3)