# Step 1: Install Expyriment

1. Download and install Python 3.8 from https://python.org.

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

# Step 3: Run tests
## Test 1 - Stimulus presentation latencies
1. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/test1_stimulus_presentation_latencies.py`

2. The script first starts the Expyriment test suite

3. Navigate to _"1) Visual stimulus presentation"_ and hit <kbd>Enter</kbd> to run the test

4. If the results are red, exit with <kbd>ESC</kbd>, and start the script again with `expyriment -3 /path/to/collaborative_timeing_tests/implementations/expyriment/test1_stimulus_presentation_latencies.py` (NOTE THE ADDED -3 OPTION!) and rerun the visual presentation test

5. Navigate to _"2) Auditory stimulus presentation"_ and hit <kbd>Enter</kbd> to run the test

6. Navigate to _"6) Serial port test"_ and hit <kbd>Enter</kbd> to run the test; fill in the correct settings for the attached equipment

7. Navigate to _"7) Write protocol"_ and hit <kbd>Enter</kbd> to save a test protocol

8. Navigate to _"8) Quit"_ to quit the test suite

9. The test script will now run

## Test 2 - Response time latencies
### Keyboard
1. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/test2_response_time_latencies_keyboard.py`

2. The script first starts the Expyriment test suite

3. Navigate to _"1) Visual stimulus presentation"_ and hit <Enter> to run the test

4. If the results are red, exit with <ESC>, and start the script again with `expyriment -3 /path/to/collaborative_timeing_tests/implementations/expyriment/test2_response_time_latencies_keyboard.py` (NOTE THE ADDED -3 OPTION!) and rerun the visual presentation test

5. Navigate to _"2) Auditory stimulus presentation"_ and hit <Enter> to run the test

6. Navigate to _"7) Write protocol"_ and hit <Enter> to save a test protocol

7. Navigate to _"8) Quit"_ to quit the test suite

8. The test script will now run

### Serial
1. Run `expyriment /path/to/collaborative_timing_tests/implementations/expyirment/test2_response_time_latencies_serial.py`

2. The script first starts the Expyriment test suite

3. Navigate to _"1) Visual stimulus presentation"_ and hit <Enter> to run the test

4. If the results are red, exit with <ESC>, and start the script again with `expyriment -3 /path/to/collaborative_timeing_tests/implementations/expyriment/test2_response_time_latencies_serial.py` (NOTE THE ADDED -3 OPTION!) and rerun the visual presentation test

5. Navigate to _"2) Auditory stimulus presentation"_ and hit <Enter> to run the test

6. Navigate to _"6) Serial port test"_ and hit <Enter> to run the test; fill in the correct settings for the attached equipment

7. Navigate to _"7) Write protocol"_ and hit <Enter> to save a test protocol

8. Navigate to _"8) Quit"_ to quit the test suite

9. The test script will now run

# Step 4: Save test results
1. Create new directory `/path/to/collaborative_timing_tests/results/<SITE_ID>/expyriment/`

2. Move the directories `/path/to/collaborative_timing_tests/implementations/expyriment/events` and `/path/to/collaborative_timing_tests/implementations/expyriment/data` to new directory

3. Move log files recorded by external equipement to new directory
