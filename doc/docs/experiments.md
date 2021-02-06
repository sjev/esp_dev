# Experiments

## Stepper motor

Motor: [28BYJ-48](https://www.tinytronics.nl/shop/nl/robotica/motoren/motor/stappen-motor-met-uln2003-motoraansturing)

Driver: uln2003

Code location: `/esp32/nodeMCU/stepper.py`

see also [jangeox blog](http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html) for in detail explanation and torque measurementes.

**Takeaways:**

  * only half stepping works
  * delays lower than 900us ar too short (motor does not move)
