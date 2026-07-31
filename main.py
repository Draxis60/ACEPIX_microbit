"""

different brightness values

"""
"""

paints the selected pixel

"""
"""

clears the screen

"""

def on_pin_pressed_p0():
    if led.point_brightness(X, Y) == 0:
        led.plot_brightness(X, Y, 201)
    else:
        led.unplot(X, Y)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

"""

makes it so that it lights up for a short amount of time

"""
def LIGHTFORSHORT():
    if led.point_brightness(X, Y) == 0:
        led.plot(X, Y)
        basic.pause(100)
        led.unplot(X, Y)
    else:
        led.unplot(X, Y)
        basic.pause(100)
        led.plot(X, Y)
"""

moves the "cursor" on the x and y axis (yes i know the microturtle could acomplish this more easily)

"""

def on_button_pressed_a():
    global X
    if X == 0:
        X = 1
        LIGHTFORSHORT()
    elif X == 1:
        X = 2
        LIGHTFORSHORT()
    elif X == 2:
        X = 3
        LIGHTFORSHORT()
    elif X == 3:
        X = 4
        LIGHTFORSHORT()
    elif X == 4:
        X = 0
        LIGHTFORSHORT()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    if led.point_brightness(X, Y) == 0:
        led.plot_brightness(X, Y, 50)
    else:
        led.unplot(X, Y)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    if input.logo_is_pressed():
        basic.show_leds("""
            . # # # .
            # . # . #
            # # # # #
            . # # # .
            . # # # .
            """)
        basic.pause(500)
        basic.show_leds("""
            . . . . .
            # . # . #
            # # # # #
            . # # # .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            . # # # .
            . # # # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # .
            """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Y
    if Y == 0:
        Y = 1
        LIGHTFORSHORT()
    elif Y == 1:
        Y = 2
        LIGHTFORSHORT()
    elif Y == 2:
        Y = 3
        LIGHTFORSHORT()
    elif Y == 3:
        Y = 4
        LIGHTFORSHORT()
    elif Y == 4:
        Y = 0
        LIGHTFORSHORT()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    if led.point_brightness(X, Y) == 0:
        led.plot_brightness(X, Y, 122)
    else:
        led.unplot(X, Y)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_logo_pressed():
    if led.point_brightness(X, Y) == 0:
        led.plot(X, Y)
    else:
        led.unplot(X, Y)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

"""

sets variables and does the startup animation

"""
Y = 0
X = 0
X = 0
Y = 0
basic.show_string("ACEPIX")
basic.show_leds("""
    . . . . .
    . # . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . # . . .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . # # . .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . .
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    . # . . .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)