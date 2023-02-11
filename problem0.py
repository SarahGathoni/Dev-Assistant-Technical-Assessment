def getValue_x(n, isTooSweet):
    lower-value = n
    higher-value = n*2

    while higher-value - lower-value > 1:
        mid-value = (lower-value + higher-value)

        if isTooSweet(mid):
            higher-value = mid-value
        else:
            lower-value = mid-value
    return mid-value = x
