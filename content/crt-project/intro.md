Title: Creating a clock out of a soviet-era ESCRT
Date: 2017-01-16
Modified: 2017-01-16
Tags: microcontroller, circuits
Slug: escrt-clock-intro

In this series of posts, I'm going to document creating a clock out of a
Soviet-era electrostatic CRT (ESCRT). A lot of the circuit motivation came from
[Oscilloscope CRT Clock](https://web.jfet.org/vclk/) and the original datasheet for the CRT I'll be using
can be found at [7QR20.pdf](https://frank.pocnet.net/sheets/183/7/7QR20.pdf).

# How ESCRTs work

ESCRTs differ in their implementations, but all share some common attributes:

1. Filament
2. Stopping voltage
3. Focusing voltage
4. Deflection plates
5. Anode and cathode
6. Screen

Heating the filament causes electrons to boil off with some initial velocity.
The stopping voltage will cause electrons with lower velocities to deflect back
toward the filament, effectively controlling the brightness of the beam. The
anode to cathode voltage accelerates the electrons toward the screen, and the 
focusing voltage collimates the beam. Finally, the deflection plates move the
beam horizontally/vertically on the screen.

# The 7QR20 ESCRT

This project uses the 7QR20 ESCRT created by Tesla. It has a double-ended
deflection plate pair for one direction and a single-ended deflection for the
other direction (one of the plates is tied to the anode voltage).

Operating values:

Filament voltage is 6.3VAC

Name                                        | Min. | Max. | Absolute max. 
------------------------------------------- | ---- | ---- | --------------
Anode voltage                               | 500  | 800  | 1000          
Stopping voltage                            | -40  | -25  | 0             
Focusing voltage                            | 120  | 190  | 500           
Deflection plate D1/D2 sensitivity (mm/V)   | .44  | .275 |                
Deflection plate D3/D4 sensitivity (mm/V)   | .4   | .25  |                
Peak voltage between any deflection plates  |      |      | 500           
