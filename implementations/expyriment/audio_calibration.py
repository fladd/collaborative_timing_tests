"""Audio calibration

Repeatedly plays a sound with increasing buffer size, starting with 32 samples,
and asks user to confirm whether the sound was distorded or not, in order to
assess the lowest buffer size the system is cabable of.

"""

import pygame

import expyriment as xpy

from config import settings


exp = xpy.control.initialize()
tone = xpy.stimuli.Tone(3000, frequency=440,
                        samplerate=settings["audio_sample_rate"], amplitude=1)
xpy.stimuli.TextScreen("Audio calibration", "Press [ENTER] to start").present()
exp.keyboard.wait(xpy.misc.constants.K_RETURN)
buffer_size = 32
while True:
    pygame.mixer.quit()
    pygame.mixer.pre_init(settings["audio_sample_rate"], -16, 2, buffer_size)
    pygame.mixer.init()
    pygame.mixer.init()
    tone.present()
    xpy.stimuli.TextScreen(f"Testing buffer size of {buffer_size} samples",
                           "Was the sound clear, without any distortion, clicking or crackling?\n\n[y/n]").present()
    key, rt = exp.keyboard.wait([xpy.misc.constants.K_y, xpy.misc.constants.K_n])
    if key == xpy.misc.constants.K_y:
        xpy.stimuli.TextScreen("Done", f"Your system can handle a buffer size of {buffer_size} samples!\n\nPress [ENTER] to quit").present()
        exp.keyboard.wait(xpy.misc.constants.K_RETURN)
        break
    else:
        buffer_size *= 2
