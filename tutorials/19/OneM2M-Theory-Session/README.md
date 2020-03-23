# Theory : OneM2M session, IIIT-Hyderabad
--- 

## Contents of this sub-repo 
1. [OneM2M_IIIT_Class_Slides.pptx](https://github.com/suraj2596/OneM2M-IIITH/blob/master/OneM2M-Theory-Session/OneM2M_IIIT_Class_Slides.pptx) : Introduces OneM2M framework and its potential features like scalability and interoperability and why they are important in deploying large-scale IoT solutions


2. [Code](https://github.com/suraj2596/OneM2M-IIITH/tree/master/OneM2M-Theory-Session/Code) for in-class experiment : 
![](https://github.com/suraj2596/OneM2M-IIITH/blob/master/OneM2M-Theory-Session/media/in-class-exp-pic.png)
Through this experiment, the pipeline of using OneM2M standard framework was demonstrated alongside theory:
    - A simple sign board with 4 characters “O,M,2,M” was illuminated with 4 LEDs respectively.
    - It was then demonstrated how each LED would be registered as AE to the resource tree, pass few labels, create DATA and DESCRIPTOR containers.
    - Based on the labels, the LEDs were actuated. 
    For eg: Switch on all Ms in “O,M,2,M” sign board. Or, Switch off all numerical characters in the same sign board. 
    - All this was done using a simple python library that consists of OneM2M procedures and ESP8266 was the underlying hardware
