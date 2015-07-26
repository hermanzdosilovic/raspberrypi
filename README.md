# Raspberry Pi Model B+ V1.2

Things about Raspberry Pi.

## Specification

[Here](https://www.raspberrypi.org/products/model-b-plus/) is the official page of this model and complete  *RPI* documentation is available [here](https://www.raspberrypi.org/documentation/).

  * `512MB`
  * `700MHz`

## Setup

### Install

  * Follow [instructions](https://www.raspberrypi.org/help/noobs-setup/) up to **FIRST BOOT** section `5`.

### Raspberry Pi Configuration

After instalation you should see Raspberry Pi Configuration window. Here we are going to configurate our Raspberry Pi.

  1. Expand Filesystem
  2. Change User Password
    * Choose whatever password you want and **remember it**.
  3. Internationalisation Options
    * Change Locale
        * Install `All locales`.
        * Use `en_US.UTF-8` as default locale
    * Change Timezone
        * `Europe` -> `Zagreb`
  4. Overclock
    * `Modest 800MHz ARM, 250MHz core, 400MHz SDRAM, 0 overvold`
  5. Advanced Options
    * Hostname
        * Choose whatever hostname you want
    * SSH
        * `Enable`
    * Update

Select `Finish` and issue command `sudo reboot` if *RPI* does not reboot automatically.

Read more about `raspi-config` [here](https://www.raspberrypi.org/documentation/configuration/raspi-config.md).

### Default Username and Password

  * username: `pi`
  * password: `raspberry`

If you cannot login with these credentials, you maybe changed your password using `raspi-config`.

### WiFi Setup

To connect to your WiFi network follow these steps (your WiFi Dongle doesn't have to be plugged in):

  1. Run this command to open your `wpa_supplicant` configuration file:

        $ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

  2. On the end of the file add this:

        network={
            ssid="<Network Name>"
            psk="<Network Password>"
        }

  3. Insert your WiFi Dongle if you already didn't.

  4. Reboot *RPI*
      * `sudo reboot` or unplug and plug back in your *RPI*

Read more about setting up WiFi on *RPI* [here](https://www.raspberrypi.org/documentation/configuration/wireless/).

### Keyboard Layout

If your keyboard layout is not set correctly you can easly fix it by editing `keyboard` file on your *RPI*:

  1. Open `keyboard` file for editing

        $ sudo nano /etc/default/keyboard

  2. Then find a line where it says something like this:

        XKBLAYOUT=”gb”

  3. Change the value of `XKBLAYOUT` with [Alpha-2 code](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) of your country.

    * For example: `XKBLAYOUT="us"`

  4. Save, exit and reboot *RPI*.
