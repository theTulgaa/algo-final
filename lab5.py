def pound(goods: list[int], pound: int) -> list[int]:
    """
    Return a sorted list of integers in goods that can sum up to the given pound.
    If no combination is found, return an empty list.
    If multiple combinations are found, return the one with the least length.
    """
    '''lab5'''
    dp = {0: []}

    for good in goods:
        if good <= pound:
            current_keys = list(dp.keys())
            for current_sum in reversed(current_keys):
                new_sum = current_sum + good
                if new_sum <= pound:
                    new_combination = dp[current_sum] + [good]
                    if new_sum not in dp or len(new_combination) < len(dp[new_sum]):
                        dp[new_sum] = new_combination

    return sorted(dp[pound]) if pound in dp else []



def optimal_bst(keys: list[int], freq: list[int], n: int) -> int:
    """
    Function to calculate minimum cost of an Optimal Binary Search Tree (OBST)
    
    :param keys: List of keys in sorted order
    :param freq: List of frequencies corresponding to keys
    :param n: Number of keys
    :return: Minimum cost of the Optimal BST
    """
    '''Lab6'''
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            total_freq = sum(freq[i:j + 1])
            for r in range(i, j + 1):
                left_cost = cost[i][r - 1] if r > i else 0
                right_cost = cost[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + total_freq
                if total_cost < cost[i][j]:
                    cost[i][j] = total_cost
    return cost[0][n - 1]


def fractional_knapsack(goods: list[list[int]], pound: int) -> float:
    """
    Return the maximum value achievable with a fractional knapsack approach.
    
    Args:
    goods: A list of lists where each sublist contains [weight, value].
    pound: The maximum weight capacity of the knapsack.
    
    Returns:
    The maximum value achievable. lab7
    """
    # Sort goods by value-to-weight ratio (highest first)
    goods.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    current_weight = 0
    
    for item in goods:
        weight = item[0]
        value = item[1]
        
        if current_weight + weight <= pound:
            total_value += value
            current_weight += weight
        else:
            remaining_weight = pound - current_weight
            total_value += value * (remaining_weight / weight)
            break
    
    return total_value



