from typing import List, Tuple

def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1 


def count_primes(n: int) -> int:
    if n < 2:
        return 0
    isPrime = [True] * (n + 1)
    isPrime[0], isPrime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if isPrime[i] else 0)
    return prime_count[n]




def find_closest_pair(pair: Tuple[int, int], bycicle: List[Tuple[int, int]]) -> int:

    arr = []
    for i in bycicle:
        distance = abs(pair[0] - i[0]) + abs(pair[1] - i[1])
        arr.append(distance)
    return arr.index(min(arr))

def bycicle(student: List[Tuple[int, int]], bycicle: List[Tuple[int, int]]) -> List[int]:

    answer = []
    for i in student:
        index = find_closest_pair(i, bycicle)
        answer.append(index)
        bycicle.pop(index)
    return answer

print(bycicle([(0, 0), (1, 1)], [(0, 1), (4, 3), (2, 1)]))

