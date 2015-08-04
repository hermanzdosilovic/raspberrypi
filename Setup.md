# Install NOOBS and Configure *RPI*

## Install NOOBS

Follow [instructions](https://www.raspberrypi.org/help/noobs-setup/) up to the (including the) *FIRST BOOT* section, number *4*.

## Raspberry Pi Configuration

After instalation you should see Raspberry Pi Configuration window. Here we are going to configurate your Raspberry Pi.

  1. Expand Filesystem
  2. Change User Password (optional)
    * Choose whatever password you want and **remember it**.
  3. Internationalisation Options
    * Change Locale
        * Install locales you want (`All locales`).
        * Select your default locale (`en_US.UTF-8`).
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
