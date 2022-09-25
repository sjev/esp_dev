#!/bin/bash

echo "Flashing micropython"
esptool.py  --port /dev/ttyUSB0 --baud 460800 erase_flash
esptool.py  --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 micropython_camera_feeeb5ea3_esp32_idf4_4.bin
