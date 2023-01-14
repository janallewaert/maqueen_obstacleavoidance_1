let distance = false
basic.showIcon(IconNames.Heart)
maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
basic.forever(function () {
    if (maqueen.Ultrasonic(PingUnit.Centimeters) < 20 && maqueen.Ultrasonic(PingUnit.Centimeters) != 0) {
        distance = Math.randomBoolean()
        if (distance == true) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 101)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            basic.pause(1000)
        }
        if (distance == false) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 101)
            basic.pause(1000)
        }
    } else {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 101)
    }
})
