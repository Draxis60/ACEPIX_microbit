input.onPinPressed(TouchPin.P0, function () {
    led.plotBrightness(X, Y, 255)
})
input.onButtonPressed(Button.A, function () {
    if (X == 0) {
        X = 1
    } else if (X == 1) {
        X = 2
    } else if (X == 2) {
        X = 3
    } else if (X == 3) {
        X = 4
    } else if (X == 4) {
        X = 0
    }
})
input.onPinPressed(TouchPin.P2, function () {
    led.plotBrightness(X, Y, 50)
})
input.onButtonPressed(Button.AB, function () {
    if (input.logoIsPressed()) {
        basic.showLeds(`
            . # # # .
            # . # . #
            # # # # #
            . # # # .
            . # # # .
            `)
        basic.pause(500)
        basic.showLeds(`
            . . . . .
            # . # . #
            # # # # #
            . # # # .
            . # # # .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            . # # # .
            . # # # .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            . # # # .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    if (Y == 0) {
        Y = 1
    } else if (Y == 1) {
        Y = 2
    } else if (Y == 2) {
        Y = 3
    } else if (Y == 3) {
        Y = 4
    } else if (Y == 4) {
        Y = 0
    }
})
input.onPinPressed(TouchPin.P1, function () {
    led.plotBrightness(X, Y, 150)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (led.pointBrightness(X, Y) == 0) {
        led.plot(X, Y)
    } else {
        led.unplot(X, Y)
    }
})
let Y = 0
let X = 0
X = 0
Y = 0
basic.showString("ACEPIX")
basic.showLeds(`
    . . . . .
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . # . . .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . # # . .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . # . . .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
