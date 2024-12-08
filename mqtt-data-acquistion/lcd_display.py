import time
import fcntl
import struct
import bmp180sensor
from ctypes import c_short

# I2C settings
DEVICE = 0x27  # Default I2C address for the LCD
I2C_SLAVE = 0x0703  # I2C_SLAVE operation

# Open the I2C device
i2c_file = open('/dev/i2c-1', 'rb+', buffering=0)
fcntl.ioctl(i2c_file, I2C_SLAVE, DEVICE)

# LCD Backlight bit (0x08) for I2C control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

def write_byte(data):
    """Write a single byte to the LCD via I2C."""
    i2c_file.write(bytearray([data]))
    time.sleep(0.0001)

def write_byte_data(register, value):
    """Write byte data to the I2C LCD."""
    i2c_file.write(bytearray([register, value]))
    time.sleep(0.0001)

def lcd_strobe(data):
    """Pulse the enable pin to latch the data."""
    write_byte(data | 0b00000100)  # Enable high
    write_byte(data & ~0b00000100)  # Enable low

def lcd_write_four_bits(data):
    """Write the lower 4 bits of the data to the LCD."""
    write_byte(data)
    lcd_strobe(data)

def lcd_write(cmd, mode=0, backlight=LCD_BACKLIGHT):
    """Write a command to the LCD."""
    # Ensure backlight is turned on by combining it with the command
    lcd_write_four_bits(mode | (cmd & 0xF0) | backlight)  # High nibble
    lcd_write_four_bits(mode | ((cmd << 4) & 0xF0) | backlight)  # Low nibble

def lcd_clear():
    """Clear the LCD screen."""
    lcd_write(0x01)  # Clear display command
    time.sleep(0.002)

def lcd_init():
    """Initialize the LCD."""
    time.sleep(0.05)
    lcd_write(0x03)
    lcd_write(0x03)
    lcd_write(0x03)
    lcd_write(0x02)  # Set to 4-bit mode
    lcd_write(0x28)  # 2-line mode, 5x8 font
    lcd_write(0x0C)  # Display ON, cursor OFF
    lcd_write(0x06)  # Entry mode set (increment cursor)
    lcd_clear()

def display_string(string, line=1):
    """Display a string on a specific line (1-4)."""
    if line == 1:
        lcd_write(0x80)
    elif line == 2:
        lcd_write(0xC0)
    elif line == 3:
        lcd_write(0x94)
    elif line == 4:
        lcd_write(0xD4)

    for char in string:
        lcd_write(ord(char), 0x01, backlight=LCD_BACKLIGHT)  # RS = 1 (data), with backlight

# Initialize LCD
lcd_init()

# Display the message  on the first line
#message = "Hello from Shweta"

# Infinite loop to continuously display the message on the first line
while True:
    try:
        # Display the message "Hello from Shweta" on the first line
        #display_string(message, line=1)
        temp, pressure, altitude = bmp180sensor.readBmp180()

        # Displaying in two lines
        line1 = f"T:{temp:.1f}C P:{pressure//1000}kPa"
        line2 = f"Alt:{altitude:.2f}m"

        # Display data on LCD
        display_string(line1, line=1)
        display_string(line2, line=2)
        
        time.sleep(2)  # Wait for 2 second before refreshing

    except KeyboardInterrupt:
        # Exit loop on keyboard interrupt
        lcd_clear()
        break
