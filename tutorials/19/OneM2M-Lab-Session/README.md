# Lab : OneM2M session, IIIT-Hyderabad
---
![](https://github.com/suraj2596/OneM2M-IIITH/blob/master/OneM2M-Lab-Session/media/lab2.png)

Link to video : [Lab overview and Student's experience](https://drive.google.com/open?id=1m7o4IiXaHgOug8kIIe8BSRWgp-HO3kgz)

## Contents of this sub-repo 
1. [OneM2M_Lab_Manual_IIIT.pdf](https://github.com/suraj2596/OneM2M-IIITH/blob/master/OneM2M-Lab-Session/OneM2M_Lab_Manual_IIIT.pdf) : An instruction manual for the lab session that describes the pre-requisites, the experiment in-detail and other details are given here. 


2. [Code](https://github.com/suraj2596/OneM2M-IIITH/tree/master/OneM2M-Theory-Session/Code) for lab experiment : 
In this lab experiment, students build a resource tree using oneM2M python methods, latched-up hardware and conducted the following experiment 
    1. Build the OneM2M resource tree using code python methods and communicate with the OneM2M resource tree to get an understanding of how resources like AEs, containers and content instances are created.
    2. Then, a logic to read from the tree was written to read the tapped event. The GET method was used here.
    3. Based on this event, a logic to actuate odd/even LEDs on/off based on single/double tap on the sensor board was written. POST method was demonstrated here.

    This experiment is discussed in detail in this above mentioned lab manual

---

At the end of the lab session, students were comfortable with the following concepts:
- Visualizing the resource tree
- 101 of talking to OM2M server : Creating your first payload
- Creating/deleting entities
- Posting data
- Reading data
- Latching the hardware setup
- Creating the payload with sensor data
- Posting the data to the OM2M tree
- Reading from the OM2M tree
- Sending commands to the actuator

The inter-operability of OneM2M framework was demonstrated by using 2 different kinds of boards:
1. ESP8266
2. Nucleo F401RE

NOTE: The codes for ESP8266 and the Nucleo board were given before-hand. Students had to write the python code on their systems that scans the tree, perform logic and actuate LEDs.
