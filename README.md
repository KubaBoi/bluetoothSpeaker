# Bluetooth rpi

https://www.raspberrypi.org/forums/viewtopic.php?t=247892

## Download 

- sudo apt-get install bluealsa

## Settings

1. unpair pi - ```bluetoothctl```
2. edit - ```sudo nano /lib/systemd/system/bluealsa.service```

```json
ExecStart=/usr/bin/bluealsa --profile=a2dp-sink
```

3. create - ```sudo nano /etc/systemd/system/aplay.service```

```json
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