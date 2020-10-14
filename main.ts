basic.forever(function () {
    for (let Y = 0; Y <= 4; Y++) {
        for (let X = 0; X <= 4; X++) {
            if (Y == 1) {
                break;
            }
            led.plot(X, Y)
            basic.pause(200)
        }
    }
})
