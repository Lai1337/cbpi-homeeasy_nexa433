Plugin for CraftBeerPi for HomeEasy and Nexa 433 mhz self-learning power sockets. Feel free to improve the code. I know nothing about coding. I am a copy-paste monkey.
<br>
## HARDWARE PREREQUISITES
- Self-learning Nexa/HomeEasy 433 mhz power socket (tested with [Nexa PE-3](https://www.clasohlson.com/se/Fj%C3%A4rrstr%C3%B6mbrytare-3-pack-Nexa-PE-3/36-4602) och [Nexa MYCR-3](https://www.clasohlson.com/se/Fj%C3%A4rrstr%C3%B6mbrytare-3-pack-Nexa-MYCR-3/36-6902))
- Rf 433 mhz transmitter, e.g. FS1000A ([2-3 USD on Ebay](https://www.ebay.com/sch/i.html?_nkw=433+mhz+transmitter)). No need for the receiver. The power socket is self-learning.
- [3 female-female dupont cables](https://www.ebay.com/sch/i.html?_nkw=female-female+dupont+cables)

## SOFTWARE INSTALLATION
### 1. [Install piHomeEasy](https://github.com/nbogojevic/piHomeEasy)

#### Install WiringPi
```bash
cd ~
sudo apt-get install git-core
git clone git://git.drogon.net/wiringPi
cd wiringPi
sudo ./build
```
#### Install piHomeEasy
```bash
cd ~
git clone git://github.com/nbogojevic/piHomeEasy
cd piHomeEasy
sudo make install
```

### 2. Install the plugin
- Install on the Craftbeerpi3 plugin/addon page in the GUI/web-interface
- Edit and configure `actor-on.sh` and `actor-off.sh` [see examples in repository](actor-on.sh) in the home folder (`/pi/home/`). Do not forget to change file permissions.

ALTERNATIVE (manual installation)
- Install repository
```bash
cd ~/craftbeerpi3/modules/plugins/
git clone git://github.com/Lai1337/cbpi-homeeasy_nexa433
```

## HARDWARE INSTALLATIONS
- The Rf transmitter has 3 pins: VCC, GND och DATA
Default is to connect DATA to GPIO 17 (Pin 0 i WiringPi)
![alt text](https://github.com/Lai1337/cbpi-homeeasy_nexa433/blob/master/Wiring.png)
- Pair power socket EXAMPLE `piHomeEasy 0 56123 1 on` [see comments in example files](actor-on.sh).
