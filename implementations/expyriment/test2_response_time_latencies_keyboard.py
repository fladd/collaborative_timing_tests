import expyriment as xpy

from config import settings


HALF_REFRESH_CYCLE = 1000 / settings["SCREEN_REFRESH_RATE"] / 2

exp = xpy.design.Experiment("Test 2 - Response time latencies (keyboard)")
exp.data_variable_names = ["Key", "RT"]
xpy.control.defaults.open_gl = settings["open_gl"]
xpy.control.initialize(exp)

# STIMULI
blank = xpy.stimuli.BlankScreen())
rect = xpy.stimuli.Rectangle((400, 400), colour=(255, 255, 255),
                             position=(0, exp.screen.size[1] / 2 - 200)))
blan.preload()
rect.preload()

# RUN
xpy.control.start()
xpy.stimuli.TextLine("Starting...").present()
exp.clock.wait(10000)
blank.present()
for x in range(1000):
    rect.present()
    key, rt = exp.keyboard.wait(duration=200 - HALF_REFRESH_CYCLE)
    blank.present()
    exp.clock.reset_stopwatch()
    exp.data.add([key, rt])
    exp.clock.wait(300 - exp.clock.stopwatch_time - HALF_REFRESH_CYCLE)

# SAVE DATA
for k,v in xpy.misc.get_system_info().update(settings).items():
    exp.data.add_experiment_info(f"{k}: {v}")

xpy.control.end()
