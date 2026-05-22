from machine import Pin, ADC, Timer, SPI, PWM
import framebuf
import time

# Motor control and encoder setup
m1a_pin = Pin(16, Pin.OUT)
m1b_pin = Pin(17, Pin.OUT)
m2a_pin = Pin(18, Pin.OUT)
m2b_pin = Pin(19, Pin.OUT)
encoder_pin = Pin(15, Pin.IN, Pin.PULL_UP)  # Using GPIO 15 for encoder DO
adc_pin = ADC(Pin(26))  # Using GPIO 26 for encoder AD (ADC0)

step_angle_deg = 1.8
step_angle_rad = step_angle_deg * (3.141592653589793 / 180)

encoder_pulses = 0
last_time = time.ticks_us()
step_sequence = [
    (1, 0, 1, 0),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (1, 0, 0, 1)
]

speed_factor = 1.0  # Initial speed factor

# Touch button setup
increase_speed_pin = Pin(6, Pin.IN, Pin.PULL_UP)
decrease_speed_pin = Pin(7, Pin.IN, Pin.PULL_UP)

def encoder_isr(pin):
    global encoder_pulses
    encoder_pulses += 1

encoder_pin.irq(trigger=Pin.IRQ_RISING, handler=encoder_isr)

def set_coils(coil_states):
    m1a_pin.value(coil_states[0])
    m1b_pin.value(coil_states[1])
    m2a_pin.value(coil_states[2])
    m2b_pin.value(coil_states[3])

def step_motor(steps, direction):
    global speed_factor
    step_count = len(step_sequence)
    delay_us = int(1000 / speed_factor)  # Adjust delay based on speed factor
    for step in range(steps):
        if direction == 1:
            coil_state = step_sequence[step % step_count]
        else:
            coil_state = step_sequence[-(step % step_count + 1)]
        set_coils(coil_state)
        time.sleep_us(delay_us)

def calculate_angular_velocity(encoder_pulses, step_angle_rad, time_elapsed):
    theta = encoder_pulses * step_angle_rad
    angular_velocity = theta / time_elapsed
    return angular_velocity

def read_encoder_analog():
    return adc_pin.read_u16()

# LCD setup
RED = 0x00F8
GREEN = 0xE007
BLUE = 0x1F00
WHITE = 0xFFFF
BLACK = 0x0000

class LCD_0inch96(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 160
        self.height = 80
        self.cs = Pin(9, Pin.OUT)
        self.rst = Pin(12, Pin.OUT)
        self.cs(1)
        self.spi = SPI(1, 10000_000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=None)
        self.dc = Pin(8, Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.Init()
        self.SetWindows(0, 0, self.width - 1, self.height - 1)

    def reset(self):
        self.rst(1)
        time.sleep(0.2)
        self.rst(0)
        time.sleep(0.2)
        self.rst(1)
        time.sleep(0.2)

    def write_cmd(self, cmd):
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def backlight(self, value):
        pwm = PWM(Pin(13))
        pwm.freq(1000)
        data = int(value * 65536 / 1000)
        pwm.duty_u16(data)

    def Init(self):
        self.reset()
        self.backlight(1000)
        self.write_cmd(0x11)
        time.sleep(0.12)
        self.write_cmd(0x21)
        self.write_cmd(0x21)
        self.write_cmd(0xB1)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_cmd(0xB2)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_cmd(0xB3)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_data(0x05)
        self.write_data(0x3A)
        self.write_data(0x3A)
        self.write_cmd(0xB4)
        self.write_data(0x03)
        self.write_cmd(0xC0)
        self.write_data(0x62)
        self.write_data(0x02)
        self.write_data(0x04)
        self.write_cmd(0xC1)
        self.write_data(0xC0)
        self.write_cmd(0xC2)
        self.write_data(0x0D)
        self.write_data(0x00)
        self.write_cmd(0xC3)
        self.write_data(0x8D)
        self.write_data(0x6A)
        self.write_cmd(0xC4)
        self.write_data(0x8D)
        self.write_data(0xEE)
        self.write_cmd(0xC5)
        self.write_data(0x0E)
        self.write_cmd(0xE0)
        self.write_data(0x10)
        self.write_data(0x0E)
        self.write_data(0x02)
        self.write_data(0x03)
        self.write_data(0x0E)
        self.write_data(0x07)
        self.write_data(0x02)
        self.write_data(0x07)
        self.write_data(0x0A)
        self.write_data(0x12)
        self.write_data(0x27)
        self.write_data(0x37)
        self.write_data(0x00)
        self.write_data(0x0D)
        self.write_data(0x0E)
        self.write_data(0x10)
        self.write_cmd(0xE1)
        self.write_data(0x10)
        self.write_data(0x0E)
        self.write_data(0x03)
        self.write_data(0x03)
        self.write_data(0x0F)
        self.write_data(0x06)
        self.write_data(0x02)
        self.write_data(0x08)
        self.write_data(0x0A)
        self.write_data(0x13)
        self.write_data(0x26)
        self.write_data(0x36)
        self.write_data(0x00)
        self.write_data(0x0D)
        self.write_data(0x0E)
        self.write_data(0x10)
        self.write_cmd(0x3A)
        self.write_data(0x05)
        self.write_cmd(0x36)
        self.write_data(0xA8)
        self.write_cmd(0x29)

    def SetWindows(self, Xstart, Ystart, Xend, Yend):
        Xstart = Xstart + 1
        Xend = Xend + 1
        Ystart = Ystart + 26
        Yend = Yend + 26
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(Xstart)
        self.write_data(0x00)
        self.write_data(Xend)
        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(Ystart)
        self.write_data(0x00)
        self.write_data(Yend)
        self.write_cmd(0x2C)

    def display(self):
        self.SetWindows(0, 0, self.width - 1, self.height - 1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)

    def display_text(self, text, x=0, y=0, color=WHITE):
        self.fill(BLACK)
        self.text(text, x, y, color)
        self.display()

    
    # ... (LCD class code remains the same)

def increase_speed(pin):
    global speed_factor
    speed_factor = min(speed_factor * 1.5, 10.0)  # Increase speed factor, up to a maximum of 10

def decrease_speed(pin):
    global speed_factor
    speed_factor = max(speed_factor / 1.5, 0.1)  # Decrease speed factor, down to a minimum of 0.1

increase_speed_pin.irq(trigger=Pin.IRQ_FALLING, handler=increase_speed)
decrease_speed_pin.irq(trigger=Pin.IRQ_FALLING, handler=decrease_speed)

def main():
    global encoder_pulses, last_time

    lcd = LCD_0inch96()

    while True:
        encoder_pulses = 0
        last_time = time.ticks_us()
        steps_to_measure = 200
        direction = 1

        step_motor(steps_to_measure, direction)

        current_time = time.ticks_us()
        time_elapsed = time.ticks_diff(current_time, last_time) / 1_000_000

        angular_velocity = calculate_angular_velocity(encoder_pulses, step_angle_rad, time_elapsed)
        analog_value = read_encoder_analog()

        display_text = "Vel: {:.2f} rad/s\nADC: {}\nSpeed: {:.2f}x".format(angular_velocity, analog_value, speed_factor)
        lcd.display_text(display_text)

        time.sleep(2)

main()