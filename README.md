# Test implementation

## Common system settings
- Screen refresh rate: 60 Hz
- Audio buffer: 128 samples

## Test 1 - Stimulus presentation latencies
- Wait once 10 s before starting the procedure to allow equipment to be initialized
- Present a black screen for 300 ms (18 frames), followed by the simultaneous onset of a TTL pulse (`255`, offset with `0`), a white square (top center of the screen, 400 x 400 pixels), and a sound (sine wave, 440 Hz), all lasting 200 ms (12 frames); repeat this 1000 times

## Test 2 - Response time latencies keyboard
- Wait once 10 s before starting the procedure to allow equipment to be initialized
- Present a black screen for 200 ms (12 frames), followed by a white square (top center of screen, 400 x 400 pixels), and measure (and log) the subsequent keyboard response time; repeat this 1000 times

### Test 2b - Response time latencies serial port (PsychoPy, OpenSesame & Expyriment only)
- Wait once 10 s before starting the procedure to allow equipment to be initialized
- Present a black screen for 200 ms (12 frames), followed by a white square (top center of screen, 400 x 400 pixels), and measure (and log) the subsequent serial port response time; repeat this 1000 times

# External equipment

## Test 1 - Stimulus presentation latencies
- Record the TTL pulses

## Test 2 - Response time latencies keyboard
- Record audio onsets and offsets at speaker jack
- Record visual onsets and offsets on screen
- Trigger keyboard response 100 ms after onset of white square at top center of screen

### Test 2b - Response time latencies serial port (PsychoPy, OpenSesame & Expyriment only)
- Record audio onsets and offsets at speaker jack
- Record visual onsets and offsets on screen
- Trigger serial port response 100 ms after onset of white square at top center of screen
