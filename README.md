# cbpi-homeeasy_nexa433
Plugin for CraftBeerPi for HomeEasy and Nexa 433 mhz self-learning power sockets. Interim solution to enable the use of Nexa/Homeeasy 433 mhz sockets (https://github.com/nbogojevic/piHomeEasy)
<br>
## SOFTWARE INSTALLATION:
### 1. Install nbogojevic/piHomeEasy (https://github.com/nbogojevic/piHomeEasy)

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
- Install repository
```bash
cd ~/craftbeerpi3/modules/plugins/
git://github.com/Lai1337/cbpi-homeeasy_nexa433
```
or put the file `__init__.py` in a new folder in `craftbeerpi3/modules/plugins/`
<br>
- Create 2 files in `/home/pi`: 
`actor-on.sh` and `actor-off.sh` (see examples in repository)
