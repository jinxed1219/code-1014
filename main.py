def on_forever():
    for Y in range(5):
        for X in range(5):
            led.plot(X, Y)
            basic.pause(200)
    for Y2 in range(5):
        for X2 in range(5):
            led.unplot(X2, Y2)
            basic.pause(200)
basic.forever(on_forever)
