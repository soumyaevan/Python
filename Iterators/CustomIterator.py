''' def yes_or_no():
    answer = 'yes'
    while True:
        yield answer
        answer = 'no' if answer=='yes' else 'yes' 
answer = yes_or_no()
print(next(answer))
print(next(answer))
print(next(answer))
print(next(answer)) '''

def current_beat():
    i = 1
    while True:
        yield i
        if i < 4:
            i = i+1
        else:
            i = 1
beat = current_beat()
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))    