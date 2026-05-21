<h1>Real-Time-Stepper-Monitor</h1>

<h2>Description</h2>
This project is a MicroPython-based embedded system that controls a stepper motor while monitoring its movement in real time using an encoder and a small 0.96” SPI TFT LCD screen. The motor rotates through a programmed step sequence, and encoder pulses are counted using interrupts to measure how fast the motor is spinning. The system then calculates the angular velocity and displays it live on the LCD together with the encoder’s analog sensor value and the current motor speed setting. Two touch buttons are used to increase or decrease the motor speed while the program is running, making the system interactive and easy to control. The project uses MicroPython’s machine module to handle GPIO pins, ADC readings, PWM, SPI communication, and interrupt functions, while the framebuf library is used to draw and update the display. By combining motor control, sensor feedback, and live visual monitoring, the project demonstrates a practical real-time embedded control system.
<br />


<h2>Technologies Used</h2>

- MicroPython
- Python (embedded systems)

<h2>Hardware Used</h2>

- Raspberry Pi Pico 
- 0.96” SSD1306 OLED Display 
- Built-in Temperature Sensor
- Breadboard and jumper wires
  
---

<h2>How It Works</h2>

<p>
The system continuously reads temperature data from the microcontroller’s built-in ADC sensor. This raw value is converted into degrees Celsius using a simple formula, then sent to the OLED display.
</p>

<p>
Every 2 seconds, the screen is cleared and updated with the latest temperature reading. This creates a real-time display that is easy to read and always up to date.
</p>

<p>
The MicroPython <b>machine</b> module handles both the ADC reading and I2C communication with the OLED screen, while the SSD1306 library is used to render text on the display.
</p>
<br/>

<h2>🔌 Wiring Connections (GPIO Pins)</h2>

<table>
  <tr>
    <th>OLED Pin</th>
    <th>Raspberry Pi Pico Pin</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>VCC</td>
    <td>3.3V</td>
    <td>Power supply</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>GND</td>
    <td>Ground connection</td>
  </tr>
  <tr>
    <td>SDA</td>
    <td>GP8</td>
    <td>I2C Data line</td>
  </tr>
  <tr>
    <td>SCL</td>
    <td>GP9</td>
    <td>I2C Clock line</td>
  </tr>
</table>
<br/>

---

<!--
```diff
- red text (errors)
+ green text (adds)
! orange text (warnings)
# gray text (notes)
@@ purple bold text (important)@@
