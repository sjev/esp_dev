# General

After multiple projects on multiple platforms I tend to make a mess and forget what I was working on.
This documentation is an attempt to write down some notes and avoid wasting time in the future.

There are two ways of programming :

1. Micropython
2. ESPHome


## Directory structure

``` none

├── doc  # documentation  
├── esp32 # esp 32 platform files
│   ├── firmware  # micropython binaries and flashing tool
│   └── nodeMCU # specific platform
├── esp8266 # wemos and sonoff devices
├── esphome # easy integration with HomeAssistant
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


## Development tools

### Ampy

Ampy from adafruit is a handy tool.

!!! tip
    add `export AMPY_PORT="/dev/ttyUSB0"` to `.bashrc`  file, so you don't have to specify the port each time you run ampy


## Visual studio code

Can be used with *pymakr* extension.

settings for VSC:

```json
{
	"address": "/dev/ttyUSB0",
	"username": "micro",
	"password": "python",
	"sync_folder": "",
	"open_on_start": false,
	"safe_boot_on_upload": false,
	"py_ignore": [
		"pymakr.conf",
		".vscode",
		".gitignore",
		".git",
		"project.pymakr",
		"env",
		"venv"
	],
	"fast_upload": false,
	"sync_file_types": "py,txt,log,json,xml,html,js,css,mpy",
	"ctrl_c_on_connect": false,
	"sync_all_file_types": false,
	"auto_connect": false,
	"autoconnect_comport_manufacturers": [
		"Pycom",
		"Pycom Ltd.",
		"FTDI",
		"Microsoft",
		"Microchip Technology, Inc.",
		"QinHeng Electronics HL-340 USB-Serial adapter"
	]
}
```

!!! note
    A correct manufacturer code needs to be added to `autoconnect_comport_manufacturers`. (use `lsusb`)


### Setting up VS Code 

see [using stubs](https://github.com/Josverl/micropython-stubs#using-the-stubs)