def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def arrays_with_prime_sum(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j + 1]
            if prime(sum(subarray)):
                res.append(subarray)
    return res


arr1 = [1, 2, 3, 4, 5]
result = arrays_with_prime_sum(arr1)
print(result)

arr2 = [25, 37, 14, 17, 34, 8, 79]
result = arrays_with_prime_sum(arr2)
print(result)
