#a fuction that returns the maximum distance between a feld and a towe
def get_distance(fields, towers):

    a = len(fields)
    b = len(towers)

    i, j = 0, 0

    distance = 0

    while i < a and j < b:

        distance = max(distance, abs(fields[i] - towers[j]))

        if fields[i] < towers[j]:

            i += 1

        else:

            j += 1

    return distance
