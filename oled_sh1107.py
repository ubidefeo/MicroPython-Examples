from machine import I2C, Pin
import sh1107
import gc
from random import randint
from time import sleep_ms

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 128
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coords(coords):
        return
old_coords = Point(64, 64)
new_coords = Point(64, 64)

# old_coords = ["x": 0, "y":0]
# new_coords = ["x": 0, "y": 0]
i2cbus = I2C(id = 0, scl = Pin(13), sda = Pin(12), freq = 200000)
print(i2cbus)

oled = sh1107.SH1107_I2C(128, 128, i2cbus)

oled.fill(0)
oled.show()

oled.text('Arduino', 40, 40)
oled.text('vs', 60, 54)
oled.text('MicroPython', 23, 68)
oled.show()

def new_random_point():
    new_x = randint(0, DISPLAY_WIDTH)
    new_y = randint(0, DISPLAY_HEIGHT)
    new_coords.x = new_x
    new_coords.y = new_y
    oled.line(old_coords.x, old_coords.y, new_coords.x, new_coords.y, 1)
    oled.show()
    old_coords.x = new_x
    old_coords.y = new_y
    return

def new_random_offset():
    new_x_offset = randint(-5, 5)
    new_y_offset = randint(-5, 5)
    new_coords.x += new_x_offset
    new_coords.y += new_y_offset
    if(new_coords.x > DISPLAY_WIDTH):
        new_coords.x = DISPLAY_WIDTH
    if(new_coords.x < 0):
        new_coords.x = 0
    if(new_coords.y > DISPLAY_HEIGHT):
        new_coords.y = DISPLAY_HEIGHT
    if(new_coords.y < 0):
        new_coords.Y = 0
    oled.line(old_coords.x, old_coords.y, new_coords.x, new_coords.y, 1)
    oled.show()
    old_coords.x = new_coords.x
    old_coords.y = new_coords.y

def reset_all():
    gc.collect()
    oled.fill(0)
    oled.show()
    
    
while(1):
    new_random_offset()
    sleep_ms(10)
