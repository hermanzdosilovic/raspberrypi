# Backup and Restore

First, with `df -h` find out where is your SD card located. For example on my Mac I get following output:

    Filesystem      Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
    /dev/disk1     233Gi   87Gi  145Gi    38% 22846079 38132735   37%   /
    devfs          189Ki  189Ki    0Bi   100%      653        0  100%   /dev
    map -hosts       0Bi    0Bi    0Bi   100%        0        0  100%   /net
    map auto_home    0Bi    0Bi    0Bi   100%        0        0  100%   /home
    /dev/disk2s5    60Mi   19Mi   41Mi    32%      512        0  100%   /Volumes/boot
    /dev/disk2s1   821Mi  746Mi   75Mi    91%        0        0  100%   /Volumes/RECOVERY

As you can see my SD card is located at `/dev/disk2`

Now you can backup your whole SD card like this:

    $ sudo dd bs=4m if=/dev/disk2 of=raspbian.img

If above command reports an error (`dd: bs: illegal numeric value`), please change `bs=4m` to `bs=4M`.

Before doing any backup please read these two articles about [backups](https://www.raspberrypi.org/documentation/linux/filesystem/backup.md) and [writing image to the sd card](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)
