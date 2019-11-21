def make_song(count=99,beverage='soda'):
    i = count
    while True:
        try:
            if i==0:
                yield "No more {} left".format(beverage)
                #break
            elif i == 1:
                yield "Only 1 bottle of {} left".format(beverage)
                i=i-1
                #continue
            else:
                yield "{} bottles of {} on the wall".format(i,beverage)
                i = i-1
        except StopIteration:
            break
        
kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))
print(next(kombucha_song))