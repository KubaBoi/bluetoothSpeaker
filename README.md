# Bluetooth rpi

https://www.raspberrypi.org/forums/viewtopic.php?t=247892

## Download 

- sudo apt-get install bluealsa

## Settings

1. unpair pi - ```bluetoothctl```
2. edit - ```sudo nano /lib/systemd/system/bluealsa.service```

```
ExecStart=/usr/bin/bluealsa --profile=a2dp-sink
```

3. create - ```sudo nano /etc/systemd/system/aplay.service```

```
[Unit]
Description=BlueALSA aplay service
After=bluetooth.service
Requires=bluetooth.service
    
[Service]
ExecStart=/usr/bin/bluealsa-aplay 00:00:00:00:00:00
    
[Install]
WantedBy=multi-user.target
```

4. ```sudo systemctl enable aplay```
5. ```reboot```

## Jack output

```sudo bash -c 'echo -e " defaults.pcm.card 1 \ndefaults.ctl.card 1" > /etc/asound.conf'```

## Downgrade rpi

does not work with latest version when display shield is on

```sudo rpi-update 993f47507f287f5da56495f718c2d0cd05ccbc19```

### nejaky kokotiny kolem bluetooth... neni potreba

```systemctl status bluetooth```

```sudo systemctl start bluetooth```

```sudo /etc/init.d/bluetooth start```

## discoverable bluetooth

```sudo nano /etc/bluetooth/main.conf```

```
DiscoverableTimeout = 0
```

# Second postup

https://forums.raspberrypi.com/viewtopic.php?t=235519

```
sudo apt-get install pulseaudio pulseaudio-module-bluetooth

sudo usermod -a -G bluetooth pi

sudo reboot

sudo nano /etc/bluetooth/main.conf

...
Class = 0x41C // add
...
DiscoverableTimeout = 0 // uncomment
...

sudo systemctl restart bluetooth

bluetoothctl

- power on
- discoverable on
- pairable on
- agent on

pulseaudio --start

sudo systemctl status bluetooth // check
```

## Start at boot

```
systemctl --user enable pulseaudio

// tohle jenom prepne, ze se bude zapinat console misto desktopu

sudo raspi-config

Boot options / System options

Boot / Auto Login / Desktop / CLI

Console autologin
```

## Autopairing

```
sudo apt-get install bluez-tools

sudo nano /etc/systemd/system/bt-agent.service

...
[Unit]
Description=Bluetooth Auth Agent
After=bluetooth.service
PartOf=bluetooth.service

[Service]
Type=simple
ExecStart=/usr/bin/bt-agent -c NoInputNoOutput

[Install]
WantedBy=bluetooth.target
...

sudo systemctl enable bt-agent

sudo systemctl start bt-agent

sudo systemctl status bt-agent 
```

## Output from jack

```
sudo raspi-config

System Options

Audio

Headphones
```