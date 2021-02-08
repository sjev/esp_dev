# Experiments

## Stepper motor

Motor: [28BYJ-48](https://www.tinytronics.nl/shop/nl/robotica/motoren/motor/stappen-motor-met-uln2003-motoraansturing)

Driver: uln2003

Code location: `/esp32/nodeMCU/stepper.py`

see also [jangeox blog](http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html) for in detail explanation and torque measurementes.

**Takeaways:**

  * only half stepping works
  * delays lower than 900us ar too short (motor does not move)

## Load cell

**Hardware** :  10 kg loadcell with [HX711](https://www.tinytronics.nl/shop/nl/sensoren/gewicht-druk-kracht/load-cell-versterker-hx711) amplifier.  The board was [patched](https://hackaday.io/project/1741-honeybee-hive-monitoring/log/9780-modifying-the-hx711-breakout-board-for-33v-operation) to work on 3.3V.

**Code location**: `/esp/nodeMCU/load_cell.py`

driver from [here](https://github.com/SergeyPiskunov/micropython-hx711)

### Load Cell - ESPHome

Why write custom glue, when just the right code is already available!
A version of scales measurement was built in `/esphome` folder.

to run locally - `esphome scale.yaml run`

added to home assistant by uploading the yaml file via file manager.
