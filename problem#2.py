#a function that returns the maximum distance between a feld and water tower
def get_distance(field , tower):
    a = len(field)
    b = len(tower)

    x = 0
    y = 0
    
    distance = 0

    while x < a and y < b:
        distance = max(distance, abs(field[x] - tower[y]))
        if field[x] < tower[y]:
            x += 1
        else;
        j += 1
    return distance
