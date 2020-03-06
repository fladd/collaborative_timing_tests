import expyriment as xpy

from config import settings, process_ttl_data


HALF_REFRESH_CYCLE = 1000 / settings["SCREEN_REFRESH_RATE"] / 2

exp = xpy.design.Experiment("Test 1 - Stimulus presentation latencies")
xpy.control.defaults.open_gl = settings["open_gl"]
xpy.control.defaults.audiosystem_buffer_size = settings["audio_buffer_size"]
xpy.control.initialize(exp)

# STIMULI
rect = xpy.stimuli.Rectangle((400, 400), colour=(255, 255, 255),
                             position=(0, exp.screen.size[1] / 2 - 200))
tone = xpy.stimuli.Tone(200, frequency=440,
                        samplerate=settings["audio_sample_rate"], amplitude=1)
blank = xpy.stimuli.BlankScreen()
rect.preload()
tone.preload()
blank.preload()

# IO
ttl = xpy.io.SerialPort(settings["ttl_port"],
                        baudrate=settings["ttl_baudrate"],
                        parity=settings["ttl_parity"],
                        stopbits=settings["ttl_stopbits"])

# RUN
xpy.control.start()
xpy.stimuli.TextLine("Starting...").present()
exp.clock.wait(10000)
blank.present()
ttl.clear()
data = []
for x in range(1000):
    rect.present()
    exp.clock.reset_stopwatch()
    ttl.send(255)
    tone.present()
    exp.clock.wait(200 - exp.clock.stopwatch_time - HALF_REFRESH_CYCLE)
    blank.present()
    exp.clock.reset_stopwatch()
    ttl.send(0)
    exp.clock.wait(300 - exp.clock.stopwatch_time - HALF_REFRESH_CYCLE)
    data.append(ttl.read_input())

# SAVE DATA
for k,v in xpy.misc.get_system_info().update(settings).items():
    exp.data.add_experiment_info(f"{k}: {v}")
config.process_ttl_data(exp=exp, data=data)

xpy.control.end()
