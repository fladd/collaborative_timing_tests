# Step 1: Install OpenSesame

## Windows

Download and extract the latest OpenSesame 3.3 prerelease. Make sure to download the Python 3-based package of OpenSesame 3.3.

- <https://github.com/smathot/OpenSesame/releases/>

Double-click on `opensesame.bat` to start OpenSesame

## Mac OS

```
Anaconda installation instructions here
```


## Ubuntu

```
sudo add-apt-repository ppa:smathot/rapunzel
sudo apt update
sudo apt install python3-rapunzel
pip3 install psychopy expyriment
```


# Step 2: Check video card settings

See `../expyriment/README.md`


# Step 3: Run tests

Open `timing_tests.osexp`. Check and modify the `CONSTANTS` at the top of the *settings* item.

Next, run the experiment fullscreen. This will start with a screen that allows you to select one of the three tests. All tests should be run three times, with each of the following backends: *legacy*, *psycho*, and *xpyriment*. The backends can be selected in the general properties tab of OpenSesame.
