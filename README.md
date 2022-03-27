# nlp_hindi
Project by [Aryaman Singh Kushwaha](https://github.com/aryamanprince), [Harshit Garg](https://www.linkedin.com/in/harshitgrg/) and [Pavnesh Chaturvedi](https://github.com/pc-beast). 

Demo Video: https://drive.google.com/file/d/1-WAITmAOhLg1u8oT1Egho3UXAesyLGPQ/view?usp=sharing

The purpose of this project is to create a bot(A mannequin) that could provide a QnA interface for teachers(volunteer teacher actually) as well as students of a NGO-based school in jaipur. This mannequin is an RPi, students invoke it and ask questions, sort of like an assistant.
The recurrent theme for this project is to make students aware about road-safety through interactive questions and answers, much like a digital assistant.

Languages currently supported, Hindi, English. 
Coming to what it does, we invoke it using snowboy, calling, google stt, then we make a vector, in N Dimensional space, calculating, the cosines' (all shadows) and then finally returning the one with high priority, letting the bot speak using tts.

Installation:

Setting up raspberry Pi:
1. Get the image:
https://www.raspberrypi.org/downloads/raspberry-pi-os/ ([debian-buster] [recommended version])
  (August 2020 used)
2. Flash using balenaEtcher/any other flashing software.
3. Insert the SD Card into PC, open /boot folder, (SUPPRESS WINDOWS WARNINGS ELSE ISSUES MIGHT ARISE IN FUTURE) insert the files(ssh & wpa_supplicant.conf)  given here: https://drive.google.com/drive/folders/1o876gj-mGMFaEAVKJAsYVoRnLtR4MB9f?usp=sharing. It is preferable to edit the wpa_supplicant.conf file.

NOTE:
  If the RPI has already been booted for first time, or WI-Fi network is different, it WILL have problems detecting new network, this article can be followed to solve this problem:
  https://www.raspberrypi.org/forums/viewtopic.php?t=266724.

4. Install puTTy, Advanced IP scanner, scan IP Address , then paste this address to puTTY, start the terminal using puTTy, (use id:pi, pass: gr8there) or (use id:pi, pass: gr8there) //for current Rpi 
5. If booting for first time, configure few settings by:
sudo raspi-config  --> Interfacing --> VNC - SET TO ENABLE --> back to Advanced options --> set a resolution suitable -->feel free to check resolution. 
6. Install VNC, paste IP address. I'd Password same as above.

NOTE:
1. If anyone who doesn't have a pi can simply download VNC Viewer and ask me code, the work with this is similar to me doing on my laptop (same lags etc.)
2. For installing pygobject use \
 sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 \
 and then pip3 install pygobject


Link for model: https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.hi.300.vec.gz
![image](https://user-images.githubusercontent.com/56971013/134643812-64d1b618-d3b8-4774-bead-74c359ae899f.png)
![image](https://user-images.githubusercontent.com/56971013/134643894-19b584ed-8339-4a00-89fc-538de00a1fa2.png)

Example I/O
1. Input: https://drive.google.com/file/d/1SJ75hsULpJvtQP5kkDVL5sjlzcaENEo6/view?usp=sharing
2. Output: https://drive.google.com/file/d/12vg56LSSY-A_tg8XTkms27GXRuQffXqh/view?usp=sharing

Major work to do:

1. Make Hindi Model faster.
2. Train a model so that it works offline too.
