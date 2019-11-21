def eat(food,isHealthy):
    endingHealthy = ", because my body is a temple"
    endingUnhealthy = ", because YOLO!"
    if isHealthy:
        return f"I'm eating {food}{endingHealthy}"
    return f"I'm eating {food}{endingUnhealthy}"
def nap(num_hours):
    if not isinstance(num_hours, int):
        raise ValueError
    if num_hours > 1:
        return f"Ugh!!! I overslept. {num_hours} hours are too much."
    return f"I am feeling refreshed after my {num_hours} hour nap."