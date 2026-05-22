<h1>Real-Time-Stepper-Monitor</h1>

<h2>Description</h2>
This project is a MicroPython-based embedded system that controls a stepper motor while monitoring its movement in real time using an encoder and a small 0.96” SPI TFT LCD screen. The motor rotates through a programmed step sequence, and encoder pulses are counted using interrupts to measure how fast the motor is spinning. The system then calculates the angular velocity and displays it live on the LCD together with the encoder’s analog sensor value and the current motor speed setting. Two touch buttons are used to increase or decrease the motor speed while the program is running, making the system interactive and easy to control. The project uses MicroPython’s machine module to handle GPIO pins, ADC readings, PWM, SPI communication, and interrupt functions, while the framebuf library is used to draw and update the display. By combining motor control, sensor feedback, and live visual monitoring, the project demonstrates a practical real-time embedded control system.
<br />

<h2>Technologies Used</h2>

- MicroPython  
- GPIO Control  
- SPI Communication  
- PWM (Pulse Width Modulation)  
- ADC (Analog-to-Digital Conversion)  
- Interrupt Handling (IRQ)  
- FrameBuffer Graphics (`framebuf`)  
- Real-Time Embedded Systems Programming  
- Stepper Motor Control  
- Sensor Feedback Monitoring
<br />

<h2>Hardware Used</h2>

- Raspberry Pi Pico  
- Bipolar Stepper Motor  
- Rotary Encoder  
- 0.96” SPI TFT LCD Display  
- Capacitive Touch Buttons  
- Motor Driver Circuit / H-Bridge  
- External Power Supply 5v 
- Breadboard and jumper wires
<br />

<h2>🔌Wiring Connections</h2>

<table>
  <tr>
    <th>Component</th>
    <th>Pin/Signal</th>
    <th>Raspberry Pi Pico GPIO</th>
  </tr>

  <tr>
    <td rowspan="4">Stepper Motor Driver</td>
    <td>Motor Coil 1A</td>
    <td>GPIO 16</td>
  </tr>
  <tr>
    <td>Motor Coil 1B</td>
    <td>GPIO 17</td>
  </tr>
  <tr>
    <td>Motor Coil 2A</td>
    <td>GPIO 18</td>
  </tr>
  <tr>
    <td>Motor Coil 2B</td>
    <td>GPIO 19</td>
  </tr>

  <tr>
    <td rowspan="4">Rotary Encoder</td>
    <td>Digital Output (DO)</td>
    <td>GPIO 15</td>
  </tr>
  <tr>
    <td>Analog Output (AO)</td>
    <td>GPIO 26 (ADC0)</td>
  </tr>
  <tr>
    <td>VCC</td>
    <td>3.3V</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>GND</td>
  </tr>

  <tr>
    <td rowspan="2">Touch Buttons</td>
    <td>Increase Speed Button</td>
    <td>GPIO 6</td>
  </tr>
  <tr>
    <td>Decrease Speed Button</td>
    <td>GPIO 7</td>
  </tr>

  <tr>
    <td rowspan="6">0.96” SPI TFT LCD</td>
    <td>CS</td>
    <td>GPIO 9</td>
  </tr>
  <tr>
    <td>DC</td>
    <td>GPIO 8</td>
  </tr>
  <tr>
    <td>SCK</td>
    <td>GPIO 10</td>
  </tr>
  <tr>
    <td>MOSI</td>
    <td>GPIO 11</td>
  </tr>
  <tr>
    <td>RST</td>
    <td>GPIO 12</td>
  </tr>
  <tr>
    <td>Backlight (PWM)</td>
    <td>GPIO 13</td>
  </tr>
</table>

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

---

<!--
```diff
- red text (errors)
+ green text (adds)
! orange text (warnings)
# gray text (notes)
@@ purple bold text (important)@@
