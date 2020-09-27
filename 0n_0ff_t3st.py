import pyaudio
import struct
from datetime import datetime
import time
from playsound import playsound

from binding.python.porcupine import Porcupine



porcupine_commands = None
pa = None
audio_stream = None

try:
    porcupine_commands = Porcupine(library_path='lib/windows/amd64/libpv_porcupine.dll',
                                   model_file_path='lib/common/porcupine_params.pv',
                                   keyword_file_paths=[
                                       'resources/keyword_files/ACbedroom_windows.ppn',
                                       'resources/keyword_files/hi hello_windows.ppn'],
                                   sensitivities=[0.9, 0.9])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine_commands.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine_commands.frame_length)
    print("Engine Started")
    print("Playing assistant wake sound")
    playsound("sounds/hey_how_can_i_help_you.mp3")
   
    time.sleep(1.2)
   
    playsound("sounds/assistant_wake.mp3")
    print("Now reading voice commands")
    
    while True:
        pcm = audio_stream.read(porcupine_commands.frame_length)
        pcm = struct.unpack_from("h" * porcupine_commands.frame_length, pcm)

        command_result = porcupine_commands.process(pcm)
        #print('...')
        if command_result >= 0:
            # print('{} detected command: {}'.format(str(datetime.now()), command_result))
            if command_result == 0:
                # mannequin
                print('Swithcing on bedroom AC')
               
            elif command_result == 1:
                # work out
                print('Hello Apporv')
               

except KeyboardInterrupt:
    print('stopping ...')
finally:
    if porcupine_commands is not None:
        porcupine_commands.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
