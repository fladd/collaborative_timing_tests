# Step 1: Install Expyriment

1. Download and install Python 3.7 from [python.org](https://www.python.org/downloads/release/python-376/).

2. Create a virtual environment for Expyriment:
   ```
   python3 -m pip install venv
   python3 -m venv timing_tests
   ```

3. Activate virtual environment:
   ```
   # Windows
   .\timing_tests\Scripts\activate
   
   # Linux and MacOS
   source ./timinig_tests/bin/activate
   ```
   
4. Install expyriment into virtual environment
   ```
   pip install expyriment[all]
   ```
   
# Step 2: Check video card settings
1. Switch off desktop effects (video compositor in Linux)

2. Open video card settings programme ("NVIDIA Control Panel", "Intel Graphics Settings", etc.)

3. Turn on vertical synchronization ("Vertical Sync", "V-sync" or similar; often under 3D settings)

4. If video card has power management setting (e.g. "Power management mode" for NVIDIA cards or "Graphics Power Plan" for Intel cards), make sure it is set to give best performance (e.g. "Prefer maximum performance" for NVIDIA cards or "Maximum Performance" for Intel cards)

# Step 3: Configure tests
1. Run `expyriment -T`
2. Run _1) Visual stimulus presentation_ by hitting <kbd>Enter</kbd>
3. If results are marked red, exit with <kbd>ESC</kbd> and run `expyriment -3T` (**note the added `3`!**) to switch OpenGL mode to alternative blocking
4. **If results are still red, please let us know!**
5. Note down that you switched OpenGL mode to `3` (for use in step 9)
6. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/audio_calibration.py`
7. Write down the resulting audio buffer size (for use in step 9)
8. Open `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/config.py`
9. Adept the `settings` dictionary where necessary
10. If your external measuring device sends back measurement results after each trial via the serial port, you can adapt the function `write_ttl_data` to save that data in the Expyriment data file

# Step 4: Run tests
## Test 1 - Stimulus presentation latencies
1. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/test1_stimulus_presentation_latencies.py`

2. The test script will now run

## Test 2 - Response time latencies
### Keyboard
1. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/test2_response_time_latencies_keyboard.py`

2. The test script will now run

### Serial
1. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/test2_response_time_latencies_serial.py`

2. The test script will now run

# Step 4: Save test results
1. Create new directory `/path/to/collaborative_timing_tests/results/<SITE_ID>/expyriment/`

2. Move the directories `/path/to/collaborative_timing_tests/implementations/expyriment/events` and `/path/to/collaborative_timing_tests/implementations/expyriment/data` to new directory

3. If you recorded any log files on external equipement, put those into new directory
