n = [int(x) for x in input().strip("[]").split(",")]

# l = [1, 2, 1, 3, 5, 8, 1, 7, 5]

def shaker(arr, ans):
    if arr == []:
        return ans
    firstEl = arr[0]
    ans.append(firstEl)
    arr = list(filter(lambda x: x != firstEl, arr))
    return shaker(arr, ans)

def isEnlish(c):
    return c in 'qwertyuiopasdfghjklxcvbnmzQWERTYUIOPASDFGHJKLXCVBNMZ'

cleanedInput = list(filter(lambda x: isEnlish(chr(x)), shaker(n, [])))

decrypted = list(map(lambda x: chr(x), cleanedInput))

print(decrypted)
