# Keyboard and Locales

## Keyboard Layout

If your keyboard layout is not set correctly you can easly fix it by editing `keyboard` file on your *RPI*:

  1. Open `keyboard` file for editing

        $ sudo nano /etc/default/keyboard

  2. Then find a line where it says something like this:

        XKBLAYOUT=”gb”

  3. Change the value of `XKBLAYOUT` with [Alpha-2 code](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) of your country.

    * For example: `XKBLAYOUT="us"`

  4. Save, exit and reboot *RPI*.

## Locales

You can always configure your locales using `raspi-config`.
