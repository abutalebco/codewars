def rental_car_cost(d):
    for _ in range(d):
        if d >= 7:
            return 40 * d - 50
        elif d >= 3:
            return 40 * d - 20
        else:
            return 40 * d