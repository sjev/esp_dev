# General

After multiple projects on multiple platforms I tend to make a mess and forget what I was working on.
This documentation is an attempt to write down some notes and avoid wasting time in the future.

## Directory structure

``` none

├── doc  # documentation  
├── esp32 # esp 32 platform files
│   ├── firmware  # micropython binaries and flashing tool
│   └── nodeMCU # specific platform
└── README.md
```

## Flashing firmware

cd into corresponding firmware directory and run `flash_xxx /dev/ttyUSBX` script

updated firmware can be downloaded from [micropython site](http://micropython.org/download/esp32/)

## Python environment

A virtual environment should be used to separate tooling from the system python envrionment.

1. Create a virtual environment `python3 -m venv venv`
2. Activate it `source venv/bin/activate`
3. Install required packages `pip instal -r requirements.txt`


## Managing files

### Ampy

Ampy from adafruit is a handy tool.

!!! tip
    add `export AMPY_PORT="/dev/ttyUSB0"` to `.bashrc`  file, so you don't have to specify the port each time you run ampy
