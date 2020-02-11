import os

import expyriment as xpy


exp = xpy.design.Experiment("Test 2 - Response time latencies (serial)")
xpy.control.initialize(exp)

# TEST SUITE
xpy.control.run_test_suite()
# Get refresh rate and serial port settingstfrom test suite results
if not os.path.exists("test_suite_protocol.xpp"):
    raise RuntimeError("No test suite protocol found!")
with open("test_suite_protocol.xpp") as f:
    protocol = f.readlines()
    for line in protocol:
        if line.startswith("testsuite_visual_sync_refresh_rate:"):
            SCREEN_REFRESH_RATE = float(line.split()[1])
        elif line.startswith("testsuite_serial_port:"):
            BB_PORT = line.split()[1]
        elif line.startswith("testsuite_serial_baudrate:"):
            BB_BAUDRATE = int(line.split()[1])
        elif line.startswith("testsuite_serial_parity:"):
            BB_PARITY = line.split()[1]
        elif line.startswith("testsuite_serial_stopbits:"):
            BB_STOPBITS = int(line.split()[1])
os.remove("test_suite_protocol.xpp")

# DESIGN
main = xpy.design.Block()
trial = xpy.design.Trial()
trial.add_stimulus(xpy.stimuli.BlankScreen())
trial.add_stimulus(xpy.stimuli.Rectangle((400, 400), colour=(255, 255, 255),
                               position=(0, exp.screen.size[1] / 2 - 200)))
trial.preload_stimuli()
main.add_trial(trial, copies=1000)
exp.add_block(main)
for line in protocol:
    exp.add_experiment_info(line)
exp.data_variable_names = ["Key", "RT"]

# IO
bb = xpy.io.EventButtonBox(xpy.io.SerialPort(BB_PORT, baudrate=BB_BAUDRATE,
                                             parity=BB_PARITY,
                                             stopbits=BB_STOPBITS))

# RUN
xpy.control.start()
xpy.stimuli.TextLine("Starting...").present()
exp.clock.wait(10000)
for trial in exp.blocks[0].trials:
    trial.stimuli[0].present()
    exp.clock.wait(300 - 1000 / SCREEN_REFRESH_RATE / 2)
    trial.stimuli[1].present()
    key, rt = bb.wait(duration=200 - 1000 / SCREEN_REFRESH_RATE / 2)
    exp.data.add([key, rt])

xpy.control.end()
