import kmNet
import time
import random

class KMBoxMouse:
    def __init__(self):
        # Initialize the kmbox connection
        kmNet.init('192.168.2.188', 'port', 'UUID') #maybe add a config for this so user can fill in on their own.
        # Enable keyboard and mouse monitoring function
        kmNet.monitor(10000)

    def random_delay(self, min_delay=0.1, max_delay=0.2):
        """Generate a random delay to humanize interactions."""
        time.sleep(random.uniform(min_delay, max_delay))

    def click(self):
        kmNet.left(1)  # Press the left mouse button
        self.random_delay()
        kmNet.left(0)  # Release the left mouse button

    def press(self):
        kmNet.left(1)  # Press the left mouse button

    def release(self):
        kmNet.left(0)  # Release the left mouse button

    def move(self, x, y):
        kmNet.move(x, y)  # Move the mouse relatively (x, y) pixel (it not absolute but relative)

    def close(self):
        kmNet.reboot()  # Reboot the device to ensure clean disconnection

    def __del__(self):
        self.close()

kmbox_mouse = KMBoxMouse()

""" The following are kmNet modules
first import this  import kmNet  be sure it in the same folder.
# Connect to the kmbox device
kmNet.init('192.168.2.188', 'port', 'UUID') #must be call first
kmNet.monitor(10000)  # must be call first to start monitor, enable keyboard and mouse monitoring function
kmNet.isdown_left(1) is the mouse left is pressed.
kmNet.isdown_keyboard(arg0: int) check for a key if it is pressed or not
kmNet.isdown_right() the value is 0 or 1 is the mouse right is pressed.
kmNet.isdown_middle() the value is 0 or 1 is the mouse middle is pressed.
kmNet.isdown_side1() the value is 0 or 1 is the mouse side1 is pressed.
kmNet.isdown_side2() the value is 0 or 1 is the mouse side2 is pressed.
kmNet.keydown(a) is press the key has code a. where a is the number from 4 is A, 5 is B, 6 is C, ... so on.
kmNet.keyup(a)    is release the key has code a,
kmNet.lcd_color(arg0: int) for set lcd color
kmNetlcd_picture(arg0: int)
kmNet.left(1) press the left mouse button.
kmNet.left(0) release the left mouse button.
kmNet.right(1) press the right mouse button.
kmNet.right(0) release the right mouse button.
kmNet.mask_keyboard(...) block the keyboard key.
kmNet.mask_left(...) 1 or 0 to block or unblock the left mouse button.
kmNet.mask_right(...) 1 or 0 to block or unblock the right mouse button.
kmNet.mask_middle(...) 1 or 0 to block or unblock the middle mouse button.
kmNet.mask_side1(...) 1 or 0 to block or unblock the side1 mouse button.
kmNet.mask_side2(...) 1 or 0 to block or unblock the side2 mouse button.
kmNet.mask_wheel(...) 1 or 0 to block or unblock the wheel mouse.
kmNet.mask_x(...) 1 or 0 to block or unblock the x axis mouse movement.
kmNet.mask_y(...) 1 or 0 to block or unblock the y axis mouse movement.
kmNet.middle(...) 1 or 0 to press or release the middle mouse button.
kmNet.mouse(a,b,c,d) control the mouse where a is the button code. b is the dx and c is the dy and d is the wheel.
kmNet.move(arg0: int, arg1 : int) move the mouse input x, y
kmNet.move_auto(arg0: int, arg1 : int, arg2 : int) relatively mouse the mouse input x, y, the arg2 is time_ms
kmNet.move_beizer(arg0: int, arg1 : int, arg2 : int, arg3 : int, arg4 : int, arg5 : int, arg6 : int)  x, y, time_ms, piont1_x, point1_y, point2_x, point2_y
kmNet.reboot() reboot the device.
kmNet.reboot kmbox net.
kmNet.setip_port(arg0: str, arg1 : int) -> int set box ip and port.
kmNet.unmask_all() unblock all.
kmNet.unmask_keyboard(arg0: int) unmask keyboard key.
kmNet.wheel(arg0: int) control mouse wheel.input > 0 down, < 0 up
"""
