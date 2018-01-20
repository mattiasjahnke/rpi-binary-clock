from neopixel import *
import time

# LED strip configuration:
LED_COUNT = 18      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # Invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


def render(number, pixel_offset, strip):
    for index, char in enumerate("{0:b}".format(number).rjust(6, "0")[::-1]):
        color = Color(0, 0, 50) if char == '1' else 0
        strip.setPixelColor(pixel_offset + index, color)


if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
        LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()
    print('Press Ctrl-C to quit.')
    while True:
        t = time.localtime()
        render(t.tm_sec, 0, strip)
        render(t.tm_min, 6, strip)
        render(t.tm_hour, 12, strip)
        strip.show()
        time.sleep(500/1000.0)
