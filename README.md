# gcadapter_oc-dkms

Kernel module for overclocking the Nintendo Wii U/Mayflash GameCube adapter.

The default overclock is from 125 Hz to 1000 Hz. Official adapters should be able to handle this but if you experience stutter or dropped inputs you can try lowering the rate to 500 Hz.

This [document](https://docs.google.com/document/d/1cQ3pbKZm_yUtcLK9ZIXyPzVbTJkvnfxKIyvuFMwzWe0/edit) by [SSBM_Arte](https://twitter.com/SSBM_Arte) has more detailed information regarding controller overclocking.

## Changing the polling rate

Polling rate is set according to the `bInterval` value in the USB endpoint descriptor. The value sets the polling rate in milliseconds, for example: an interval value of 4 equals 250 Hz.

You can change the rate by using the kernel parameter `gcadapter_oc.rate=n` (if installed), passing the rate to `insmod gcadapter_oc.ko rate=n` or going into `/sys/module/gcadapter_oc/parameters` and using `echo n > rate` to change the value ([video](https://asciinema.org/a/455373)).


## Installing

You can get releases for Fedora, OpenSUSE, and OpenMandriva from my [COPR](https://copr.fedorainfracloud.org/coprs/kylegospo/hid-logitech-dj-dkms/).

If you wish to use this with Secure Boot, follow [this guide](https://gist.github.com/KyleGospo/9adbe078d1d7f160ae43c091df98f773).