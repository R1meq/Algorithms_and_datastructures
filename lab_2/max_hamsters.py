def max_hamsters(daily_supply, hamsters_on_sale, hamsters):
    LENGTH = len(hamsters)
    AUXILIARY = [None] * LENGTH
    GREED = 1
    FOOD_FOR_ONE = 0
    MAX_INDEX = LENGTH - 1

    def calculate_sum(neighbors):
        total = 0
        len_subarray = neighbors + 1

        for index in range(0, LENGTH):
            sum = (hamsters[index][GREED] * neighbors) + hamsters[index][FOOD_FOR_ONE]
            AUXILIARY[index] = sum

        AUXILIARY.sort()

        for index in range(0, len_subarray):
            sum = AUXILIARY[index]
            total += sum

        return total

    step = LENGTH
    hi = MAX_INDEX
    lo = 0

    total = calculate_sum(MAX_INDEX)
    if total <= daily_supply:
        return LENGTH
    else:
        while step != 0:
            mid = (lo + hi) // 2
            total = calculate_sum(mid)

            if daily_supply < total:
                hi = mid
                step //= 2
            elif total < daily_supply:
                lo = mid
                step //= 2
            else:
                return hi
    return hi