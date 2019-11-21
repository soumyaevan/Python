def eatJunk(food):
    assert food in [
        "pizza",
        "burger",
        "ice cream",
        "fries"
    ], "food must be junk food!!!"
    return f"Yaay!!! I am having {food}"

food = input("Enter a food name: ")
print(eatJunk(food))