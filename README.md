# nlp_hindi

Setting up raspberry Pi:
1. Get the image:
https://www.raspberrypi.org/downloads/raspberry-pi-os/ ([debian-buster] [recommended version])
  (August 2020 used)
2. Flash using balenaEtcher/any other flashing software.
3. Insert the SD Card into PC, open /boot folder, (SUPPRESS WINDOWS WARNINGS ELSE ISSUES MIGHT ARISE IN FUTURE) insert the files(ssh & wpa_supplicant.conf)  given here: https://drive.google.com/drive/folders/1o876gj-mGMFaEAVKJAsYVoRnLtR4MB9f?usp=sharing. Do edit the wpa_supplicant.conf file.

NOTE:
  If you have already booted Rpi for first time, (or changed wifi router) , it WILL have problems detecting new network, I followed this article to solve this problem:
  https://www.raspberrypi.org/forums/viewtopic.php?t=266724.

4. Install puTTy, Advanced IP scanner, scan IP Address , then paste this address to puTTY, start the terminal using puTTy, (use id:pi, pass: gr8there) or (use id:pi, pass: gr8there)
5. If booting for first time, configure few settings by:
sudo raspi-config  --> Interfacing --> VNC - SET TO ENABLE --> back to Advanced options --> set a resolution suitable for you,(I HAD SOME PROBLEMS here, so be careful,  some high resolution MSI monitor issue) --feel free to check resolution.
6. Install VNC, paste IP address. I'd Password same as above. (abhi k liye, in general later.)

NOTE:
If anyone who doesn't have a pi can simply download VNC Viewer and ask me code, the work with this is similar to me doing on my laptop (same lags etc.)


link for model https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.hi.300.vec.gz
