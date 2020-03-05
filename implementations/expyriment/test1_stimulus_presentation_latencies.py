import expyriment as xpy

# SETTINGS
TTL_PORT = "COM3"
TTL_BAUDRATE = 115200
TTL_PARITY = "N"
TTL_STOPBITS = 1
SCREEN_REFRESH_RATE = 60
xpy.control.defaults.audiosystem_buffer_size = 1024

# DESIGN
exp = xpy.design.Experiment("Test 1 - Stimulus presentation latencies")
xpy.control.initialize(exp)
rect = xpy.stimuli.Rectangle((400, 400), colour=(255, 255, 255),
                             position=(0, exp.screen.size[1] / 2 - 200))
tone = xpy.stimuli.Tone(200, frequency=440, amplitude=1)
blank = xpy.stimuli.BlankScreen()
rect.preload()
tone.preload()
blank.preload()

# IO
ttl = xpy.io.MarkerOutput(xpy.io.SerialPort(TTL_PORT, baudrate=TTL_BAUDRATE,
                                            parity=TTL_PARITY,
                                            stopbits=TTL_STOPBITS))

# RUN
data = []
xpy.control.start()
xpy.stimuli.TextLine("Starting...").present()
exp.clock.wait(10000)
print("".join([chr(x) for x in ttl.interface.read_input()]))
blank.present()
for x in range(10):
    rect.present()
    exp.clock.reset_stopwatch()
    ttl.send(255)
    tone.present()
    exp.clock.wait(2000 - exp.clock.stopwatch_time - 1000 / SCREEN_REFRESH_RATE / 2)
    blank.present()
    exp.clock.reset_stopwatch()
    ttl.send(0)
    data.append(ttl.interface.read_line())
    print(data[-1])
    exp.clock.wait(3000 - exp.clock.stopwatch_time - 1000 / SCREEN_REFRESH_RATE / 2)

# WRITE DATA FROM ARDUINO
exp.add_data_variable_names(["Serial", "LightOn", "LightOff", "Sound"])
for line in data:
    exp.data.add([int(x) for x in line.split(b" ")[1::2]])

xpy.control.end() 
