# Connect to The Internet

## WiFi Setup

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

## Static IP

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

## SSH

  0. Enable SSH using `raspi-config`: `Advanced Options` -> `SSH` -> `Enable`
  1. Change default SSH port to `22219` in `/etc/ssh/sshd_config` file. (optional)
  2. Restart ssh service: `sudo service ssh restart`.
  3. Add `authorized_keys` file:

        $ mkdir -p ~/.ssh
        $ sudo nano ~/.ssh/authorized_keys

  4. Append your public ssh key to `~/.ssh/authorized_keys` file.

If you are getting this annoying message when running some commands during ssh session:

    perl: warning: Setting locale failed.
    perl: warning: Please check that your locale settings:
            LANGUAGE = (unset),
            LC_ALL = (unset),
            LC_CTYPE = "UTF-8",
            LANG = "en_US.UTF-8"
        are supported and installed on your system.
    perl: warning: Falling back to the standard locale ("C").

Comment this line `AcceptEnv LANG LC_*` in your `/etc/ssh/sshd_config` file and restart ssh service.

Read more about changing default SSH port [here](http://linuxlookup.com/howto/change_default_ssh_port).

## NoIP Setup

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
