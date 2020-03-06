"""Test configuration

The settings in the `settings` dictionary will be applied to all tests.
In case the external measuring device send results back after every trial,
the function `write_ttl_data` can be customized to handle the received data.

"""

settings = {
    "ttl_port": "COM3",
    "ttl_baudrate": 115200,
    "ttl_parity": "N",
    "ttl_stopbits": 1,
    "screen_refresh_rate": 60,
    "screen_open_gl": 2,
    "audio_sample_rate": 44100,
    "audio_buffer_size": 512
}

def write_ttl_data(**kwargs):
    kwargs["exp"].add_data_variable_names(
        ["Serial", "LightOn", "LightOff", "Sound"])
    for line in kwargs["data"]:
        line = [chr(x) for x in line].strip()
        kwargs["exp"].data.add([int(x) for x in line.split(b" ")[1::2]])
