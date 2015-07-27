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

### Static IP

Issue following commands and write down addresses you get as output (these are just examples of what they may look like):

  1. `ifconfig wlan0`

    * **inet addr** - *RPI* current IP address: `192.168.1.18`
    * **Bcast** - broadcast IP range: `192.168.1.255`
    * **Mask** - subnet mask address: `255.255.255.0`

  2. `netstat -nr`

    * **Gateway** - gateway address: `192.168.1.1`
    * **Destination** - destination address: `192.168.1.0`

  3. Open your `intefaces` file

    * `sudo nano /etc/network/interfaces`

  4. You will see line `iface wlan0 inet dhcp` or `iface wlan0 inet manual`

    * Replace either of those with `iface wlan0 inet static`

  5. Just below `iface wlan0 inet static` add following:

        address 192.168.1.18
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.1.255
        gateway 192.168.1.1

  6. Reboot *RPI*

Be sure to change numbers I gave you here. These were just examples. Read more about how to set static IP on *RPI* [here](http://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address).

After reboot you should be able to `ping google.com`. If you can't ping Google, or any other address, add this into your `/etc/resolv.conf` file:


    nameserver 8.8.8.8
    nameserver 8.8.4.4

You should also see your new static IP with `hostname -I`.

### Update and Upgrade

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo reboot

### SSH

  1. Change default SSH port to `22219` in `/etc/ssh/sshd_config` file.
  2. Restart ssh service: `sudo service ssh restart`.
  3. Add `authorized_keys` file:

        $ mkdir -p ~/.ssh
        $ sudo nano ~/.ssh/authorized_keys

  4. Append your public ssh key to `~/.ssh/authorized_keys` file.

Read more about changing default SSH port [here](http://linuxlookup.com/howto/change_default_ssh_port)


### NoIP Setup

    $ cd /opt
    $ sudo wget http://www.noip.com/client/linux/noip-duc-linux.tar.gz
    $ sudo tar xvf noip-duc-linux.tar.gz
    $ cd noip-2.1.9-1
    $ sudo make install

Enter your credentials for `no-ip.com`. Set update interval to `5`.

Read more about Linux dynamic update client [here](https://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/).

To make noip start at system starup follow there instructions:

  1. Create custom script for starting and stoping noip:

        $ sudo nano /etc/inid.d/noip

  2. Copy following content, save and exit:

        #!/bin/sh

        ### BEGIN INIT INFO
        # Provides:          noip
        # Required-Start:    $remote_fs $syslog
        # Required-Stop:     $remote_fs $syslog
        # Default-Start:     2 3 4 5
        # Default-Stop:      0 1 6
        # Short-Description: Start noip2 at boot time
        ### END INIT INFO

        case "$1" in
          start)
            echo "Starting noip"
            /usr/local/bin/noip2
            ;;
          stop)
            echo "Stopping noip"
            killall noip2
            ;;
          *)
            echo "Usage: /etc/init.d/noip {start|stop}"
            exit 1
            ;;
        esac

        exit 0

  3. Change premissions:

        $ sudo chmod 755 /etc/init.d/noip

  4. Test script:

        $ sudo /etc/init.d/noip start
        $ sudo /etc/init.d/noip stop

  5. Register script to be run at startup:

        $ sudo update-rc.d noip defaults

  6. If you want to remove script from startup, run the following command:

        $ sudo update-rc.d -f noip defaults

  7. Reboot *RPI*
