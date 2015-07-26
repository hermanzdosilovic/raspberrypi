# Raspberry Pi Model B+ V1.2

Things about Raspberry Pi.

## Specification

[Here](https://www.raspberrypi.org/products/model-b-plus/) is the official page of this model.

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

### WiFi Setup

After configuring and rebooting *RPI*, login with username `pi` and password you set up earlier.

If you didn't set up password, enter `raspberry` (that is default password).

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
      * `sudo reboot` or unplug and plug back in your *RPI*.


