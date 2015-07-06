python-i2c-lcd
==============

## Setup

### General
Use ```sudo raspi-config``` to enable I2C.

After that we need to enable the i2c-dev module.
```
sudo modprobe i2c-dev
```

To enable this module on startup we can add this as root into `/etc/modules`:
```
echo "i2c-dev" >> /etc/modules
```

### Packages
```
sudo apt-get install i2c-tools
```

### Pythoon 2.x
```
sudo apt-get install python-smbus
```

### Python 3.x
```
sudo apt-get install python3-smbus
```


## Usage

```
python ./display.py line_1~line_2
```

or clock demo:

```
python ./datetime-test.py
```

## Based on
* Forked from: https://github.com/sweetpi/python-i2c-lcd
* https://github.com/pimatic/pimatic/issues/271
* http://www.gejanssen.com/howto/i2c_display_2004_raspberrypi/index.html
