# `lab.js` benchmark implementation

## Step 1: Installation

To unpack the experiment files, please unzip `timing-validation-export.zip` to the local hard drive.

## Step 2: Check browser

Next, please (install and) open a local browser, preferably Google Chrome (Version 80+) or Firefox (73+). Make take note of any installed plugins or add-ons; disable them for best results (we have no evidence that common plugins affect browser speed, but we're looking for maximum performance here).

## Step 3: Run tests

### Test 1: Stimulus presentation latencies

* Open the file `index.html` from the extracted archive contents in the browser, and change into fullscreen mode.
* Press any key to initialize the benchmark study, which will start after 10 seconds.
* At the end of the study, the collected data will be provided as a download.

### Test 2: Response time latencies

#### Keyboard

Open the study as above, but append `?response=true` to the `URL` bar. This will disable audio, and enable responses on the white screens.

#### Serial

`lab.js` does not support serial output at present.
