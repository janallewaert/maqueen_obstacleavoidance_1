distance = False
basic.show_icon(IconNames.HEART)
maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)

def on_forever():
    global distance
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 20 and maqueen.ultrasonic(PingUnit.CENTIMETERS) != 0:
        distance = Math.random_boolean()
        if distance == True:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 101)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            basic.pause(1000)
        if distance == False:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 101)
            basic.pause(1000)
    else:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 101)
basic.forever(on_forever)
