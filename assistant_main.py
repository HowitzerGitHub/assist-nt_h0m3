import struct
from datetime import datetime
import time
from playsound import playsound
import pyaudio
import arduinointerference as ai
from binding.python.porcupine import Porcupine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import threading




# GUI STARTS


# app = QApplication(sys.argv)
# win = QMainWindow()
# win.setGeometry(200,200,1001,301)
# win.setWindowTitle("Assistant GUI")
# win.setObjectName("MainWindow")
# win.resize(1001, 301)
# win.setTabShape(QtWidgets.QTabWidget.Rounded)
# win.centralwidget = QtWidgets.QWidget(win)
# win.setObjectName("centralwidget")
#
#
# mains_button = QtWidgets.QPushButton(win)
# mains_button.setGeometry(QtCore.QRect(20, 20, 111, 71))
# mains_button.setObjectName("mains_button")
#
#
#
#
# door_button = QtWidgets.QPushButton(win)
# door_button.setGeometry(QtCore.QRect(160, 20, 111, 71))
# door_button.setObjectName("door_button")
#
# socket_two_button = QtWidgets.QPushButton(win)
# socket_two_button.setGeometry(QtCore.QRect(300, 20, 111, 71))
# socket_two_button.setObjectName("socket_two_button")
#
# socket_one_button = QtWidgets.QPushButton(win)
# socket_one_button.setGeometry(QtCore.QRect(440, 20, 111, 71))
# socket_one_button.setObjectName("socket_one_button")
#
# water_pump_button = QtWidgets.QPushButton(win)
# water_pump_button.setGeometry(QtCore.QRect(580, 20, 111, 71))
# water_pump_button.setObjectName("water_pump_button")
#
# bathroom_geyser_button = QtWidgets.QPushButton(win)
# bathroom_geyser_button.setGeometry(QtCore.QRect(720, 20, 111, 71))
# bathroom_geyser_button.setObjectName("bathroom_geyser_button")
#
# stairs_lights_button = QtWidgets.QPushButton(win)
# stairs_lights_button.setGeometry(QtCore.QRect(860, 20, 111, 71))
# stairs_lights_button.setObjectName("stairs_lights_button")
#
# mains_label = QtWidgets.QLabel(win)
# mains_label.setGeometry(QtCore.QRect(40, 100, 61, 31))
# mains_label.setObjectName("mains_label")
#
# door_label = QtWidgets.QLabel(win)
# door_label.setGeometry(QtCore.QRect(180, 100, 61, 31))
# door_label.setObjectName("door_label")
#
# socket_one_label = QtWidgets.QLabel(win)
# socket_one_label.setGeometry(QtCore.QRect(450, 100, 81, 31))
# socket_one_label.setObjectName("socket_one_label")
#
# socket_two_label = QtWidgets.QLabel(win)
# socket_two_label.setGeometry(QtCore.QRect(310, 100, 91, 31))
# socket_two_label.setObjectName("socket_two_label")
#
# water_pump_label = QtWidgets.QLabel(win)
# water_pump_label.setGeometry(QtCore.QRect(570, 100, 121, 31))
# water_pump_label.setObjectName("water_pump_label")
#
# bathroom_geyser_label = QtWidgets.QLabel(win)
# bathroom_geyser_label.setGeometry(QtCore.QRect(720, 100, 131, 31))
# bathroom_geyser_label.setObjectName("bathroom_geyser_label")
#
# stairs_lights_label = QtWidgets.QLabel(win)
# stairs_lights_label.setGeometry(QtCore.QRect(860, 100, 131, 31))
# stairs_lights_label.setObjectName("stairs_lights_label")
#
# hall_lights_button = QtWidgets.QPushButton(win)
# hall_lights_button.setGeometry(QtCore.QRect(300, 170, 111, 71))
# hall_lights_button.setObjectName("hall_lights_button")
#
# porch_lights_button = QtWidgets.QPushButton(win)
# porch_lights_button.setGeometry(QtCore.QRect(20, 170, 111, 71))
# porch_lights_button.setObjectName("porch_lights_button")
#
# room_lights_button = QtWidgets.QPushButton(win)
# room_lights_button.setGeometry(QtCore.QRect(440, 170, 111, 71))
# room_lights_button.setObjectName("room_lights_button")
#
# room_ac_label = QtWidgets.QLabel(win)
# room_ac_label.setGeometry(QtCore.QRect(580, 250, 111, 31))
# room_ac_label.setObjectName("room_ac_label")
#
# room_ac_button = QtWidgets.QPushButton(win)
# room_ac_button.setGeometry(QtCore.QRect(580, 170, 111, 71))
# room_ac_button.setObjectName("room_ac_button")
#
# garden_lights_label = QtWidgets.QLabel(win)
# garden_lights_label.setGeometry(QtCore.QRect(150, 250, 141, 31))
# garden_lights_label.setObjectName("garden_lights_label")
#
# garden_lights_button = QtWidgets.QPushButton(win)
# garden_lights_button.setGeometry(QtCore.QRect(160, 170, 111, 71))
# garden_lights_button.setObjectName("garden_lights_button")
#
# hall_lights_label = QtWidgets.QLabel(win)
# hall_lights_label.setGeometry(QtCore.QRect(300, 250, 111, 31))
# hall_lights_label.setObjectName("hall_lights_label")
#
# rx_label = QtWidgets.QLabel(win)
# rx_label.setGeometry(QtCore.QRect(720, 250, 121, 31))
# rx_label.setObjectName("rx_label")
#
# porch_lights_label = QtWidgets.QLabel(win)
# porch_lights_label.setGeometry(QtCore.QRect(10, 250, 131, 31))
# porch_lights_label.setObjectName("porch_lights_label")
#
# room_lights_label = QtWidgets.QLabel(win)
# room_lights_label.setGeometry(QtCore.QRect(440, 250, 121, 31))
# room_lights_label.setObjectName("room_lights_label")
#
# rx_major_label = QtWidgets.QLabel(win)
# rx_major_label.setGeometry(QtCore.QRect(720, 170, 111, 71))
# rx_major_label.setObjectName("rx_major_label")
#
# tx_major_label = QtWidgets.QLabel(win)
# tx_major_label.setGeometry(QtCore.QRect(860, 170, 111, 71))
# tx_major_label.setObjectName("tx_major_label")
#
# tx_label = QtWidgets.QLabel(win)
# tx_label.setGeometry(QtCore.QRect(860, 250, 121, 31))
# tx_label.setObjectName("tx_label")
#
# _translate = QtCore.QCoreApplication.translate
#
# win.setWindowTitle(_translate("MainWindow", "Assistant"))
# mains_button.setText(_translate("MainWindow", "OFF"))
# door_button.setText(_translate("MainWindow", "OFF"))
# socket_two_button.setText(_translate("MainWindow", "OFF"))
# socket_one_button.setText(_translate("MainWindow", "TURN ON"))
# water_pump_button.setText(_translate("MainWindow", "TURN ON"))
# bathroom_geyser_button.setText(_translate("MainWindow", "TURN ON"))
# stairs_lights_button.setText(_translate("MainWindow", "TURN ON"))
# mains_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">MAINS</span></p></body></html>"))
# door_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">DOOR</span></p></body></html>"))
# socket_one_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">SOCKET 1</span></p></body></html>"))
# socket_two_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">SOCKET 2</span></p></body></html>"))
# water_pump_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">WATER PUMP</span></p></body></html>"))
# bathroom_geyser_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">BATHROOM GEYSER</span></p></body></html>"))
# stairs_lights_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">STAIRS LIGHTS</span></p></body></html>"))
# hall_lights_button.setText(_translate("MainWindow", "TURN ON"))
# porch_lights_button.setText(_translate("MainWindow", "TURN ON"))
# room_lights_button.setText(_translate("MainWindow", "TURN ON"))
# room_ac_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">ROOM AC</span></p></body></html>"))
# room_ac_button.setText(_translate("MainWindow", "TURN ON"))
# garden_lights_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">GARDEN LIGHTS</span></p></body></html>"))
# garden_lights_button.setText(_translate("MainWindow", "TURN ON"))
# hall_lights_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">HALL LIGHTS</span></p></body></html>"))
# rx_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">DATA LED - RX </span></p></body></html>"))
# porch_lights_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">PORCH LIGHTS</span></p></body></html>"))
# room_lights_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">ROOM LIGHTS</span></p></body></html>"))
# rx_major_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; text-decoration: underline;\">DATA LED</span></p></body></html>"))
# tx_major_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; text-decoration: underline;\">DATA LED</span></p></body></html>"))
# tx_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">DATA LED - TX</span></p></body></html>"))
#
#
#
# t1=threading.Thread(target=win.show)
# t1.start()
#
# print("Yeahhhh boiiiiyaahhh")



    ## GUI END invoke win.show() to view GUI



porcupine_wakeword = None
pa = None
audio_stream = None
awake = False
start_time = None
wake_time = 6500  # ms

try:
    porcupine_wakeword = Porcupine(library_path='lib/windows/amd64/libpv_porcupine.dll',
                                   model_file_path='lib/common/porcupine_params.pv',
                                   keyword_file_paths=['resources/keyword_files/home-auto/hey christina_windows.ppn'],
                                   sensitivities=[0.9])

    porcupine_commands = Porcupine(library_path='lib/windows/amd64/libpv_porcupine.dll',
                                   model_file_path='lib/common/porcupine_params.pv',
                                   keyword_file_paths=[
                                       'resources/keyword_files/home-auto/room ac_windows.ppn',
                                       'resources/keyword_files/home-auto/room lights_windows.ppn',
                                       'resources/keyword_files/home-auto/hall lights_windows.ppn',
                                       'resources/keyword_files/home-auto/garden lights_windows.ppn',
                                       'resources/keyword_files/home-auto/porch lights_windows.ppn',
                                       'resources/keyword_files/home-auto/stairs lights_windows.ppn',
                                       'resources/keyword_files/home-auto/bathroom geyser_windows.ppn',
                                       'resources/keyword_files/home-auto/water pump_windows.ppn',
                                       'resources/keyword_files/home-auto/socket one_windows.ppn',
                                       'resources/keyword_files/home-auto/socket two_windows.ppn',
                                       'resources/keyword_files/home-auto/open the door_windows.ppn',
                                       'resources/keyword_files/home-auto/close the door_windows.ppn',
                                       'resources/keyword_files/home-auto/mains on_windows.ppn',
                                       'resources/keyword_files/home-auto/mains off_windows.ppn'
                                   ],
                                   sensitivities=[0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90,
                                                  0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine_wakeword.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine_wakeword.frame_length)
    print("Assistant is UP and running,ready to take wake commands")
    while True:
        pcm = audio_stream.read(porcupine_wakeword.frame_length)
        pcm = struct.unpack_from("h" * porcupine_wakeword.frame_length, pcm)

        if not awake:
            #print('...')

            result = porcupine_wakeword.process(pcm)
            if result:
                awake = True
                playsound("sounds/hey_how_can_i_help_you.mp3")
                start_time = time.time()
                print('Voice Assistant activated, give command...')
                playsound("sounds/assistant_wake.mp3")
                command_result="";
        else:
            if (time.time() - start_time) * 1000 > wake_time:
                print('Voice assistant going back to sleep')
                playsound("sounds/assistant_sleep.mp3")
                awake = False
            command_result = porcupine_commands.process(pcm)
            if command_result >= 0:
                print('{} detected command: {}'.format(str(datetime.now()), command_result))

                # if command_result == 0:
                #
                #     print('Turning off AC Hall')
                #     playsound("sounds/turning_off_ac_hall.mp3")
                #     time.sleep(1)
                #     playsound("sounds/device_down.mp3")
                #
                # elif command_result == 1:
                #
                #     print('Turning ON AC Hall')
                #     playsound("sounds/turning_on_ac_hall.mp3")
                #     time.sleep(1)
                #     playsound("sounds/device_up.mp3")
                #     command_result = "";

                if command_result == 0:

                    u = 'u2'
                    d = 'd2'

                    if ai.state[2]==1:
                        ai.command(d)
                        print('Turning off AC Room')
                        playsound("sounds/turning_off_ac_room.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[2]==0:
                        ai.command(u)
                        print('Turning on AC Room')
                        playsound("sounds/turning_on_ac_room.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 1:

                    u = 'u3'
                    d = 'd3'

                    if ai.state[3] == 1:
                        ai.command(d)
                        print('Turning off Room Lights')
                        playsound("sounds/turning_off_the_room_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[3] == 0:
                        ai.command(u)
                        print('Turning on Room Lights')
                        playsound("sounds/turning_on_the_room_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 2:

                    u = 'u4'
                    d = 'd4'

                    if ai.state[4] == 1:
                        ai.command(d)
                        print('Turning off Hall Lights')
                        playsound("sounds/turning_off_the_hall_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[4] == 0:
                        ai.command(u)
                        print('Turning on Hall Lights')
                        playsound("sounds/turning_on_the_hall_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 3:

                    u = 'u5'
                    d = 'd5'

                    if ai.state[5] == 1:
                        ai.command(d)
                        print('Turning off Garden Lights')
                        playsound("sounds/turning_off_garden_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[5] == 0:
                        ai.command(u)
                        print('Turning on Garden Lights')
                        playsound("sounds/lighting_up_the_garden.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 4:

                    u = 'u6'
                    d = 'd6'

                    if ai.state[6] == 1:
                        ai.command(d)
                        print('Turning off Porch Lights')
                        playsound("sounds/turning_off_the_porch_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[6] == 0:
                        ai.command(u)
                        print('Turning on Porch Lights')
                        playsound("sounds/turning_on_the_porch_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 5:

                    u = 'u7'
                    d = 'd7'

                    if ai.state[7] == 1:
                        ai.command(d)
                        print('Turning off Stairs Lights')
                        playsound("sounds/turning_off_stairs_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[7] == 0:
                        ai.command(u)
                        print('Turning on Stairs Lights')
                        playsound("sounds/turning_on_stairs_lights.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 6:

                    u = 'u8'
                    d = 'd8'

                    if ai.state[7] == 1:
                        ai.command(d)
                        print('Turning off Bathroom Geyser')
                        playsound("sounds/turning_off_the_geyser.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[7] == 0:
                        ai.command(u)
                        print('Turning on Bathroom Geyser')
                        playsound("sounds/turning_on_the_geyser.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 7:

                    u = 'u9'
                    d = 'd9'

                    if ai.state[9] == 1:
                        ai.command(d)
                        print('Turning off Water Pump')
                        playsound("sounds/turning_off_water_pump.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[9] == 0:
                        ai.command(u)
                        print('Turning on Water Pump')
                        playsound("sounds/turning_on_water_pump.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 8:

                    u = 'uA'
                    d = 'dA'

                    if ai.state[10] == 1:
                        ai.command(d)
                        print('Turning off Socket One')
                        playsound("sounds/turning_off_socket_one.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[10] == 0:
                        ai.command(u)
                        print('Turning on Socket One')
                        playsound("sounds/turning_on_socket_one.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 9:

                    u = 'uB'
                    d = 'dB'

                    if ai.state[11] == 1:
                        ai.command(d)
                        print('Turning off Socket Two')
                        playsound("sounds/turning_off_socket_two.mp3")
                        time.sleep(1)
                        playsound("sounds/device_down.mp3")
                        command_result = ""

                    elif ai.state[11] == 0:
                        ai.command(u)
                        print('Turning on Socket Two')
                        playsound("sounds/turning_on_socket_two.mp3")
                        time.sleep(1)
                        playsound("sounds/device_up.mp3")
                        command_result = ""

                elif command_result == 10:

                    u = 'uC'

                    ai.command(u)
                    print('Opeaning the door')
                    playsound("sounds/unlocking_the_door.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    command_result = ""

                elif command_result == 11:

                    d = 'dC'
                    playsound("sounds/locking_the_door.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    ai.command(d)
                    print('Closing the door')
                    command_result = None

                elif command_result == 12:

                    u = 'uD'
                    playsound("sounds/supplying_the_main_power.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    ai.command(u)
                    print('Main power is now ON')
                    command_result = None

                elif command_result == 13:

                    d = 'dD'
                    playsound("sounds/cutting_the_main_power.mp3")
                    time.sleep(1)
                    playsound("sounds/device_down.mp3")
                    ai.command(d)
                    print('Main power is now SHUT')
                    command_result = None


            awake = False

except KeyboardInterrupt:
    print('stopping ...')
finally:
    if porcupine_wakeword is not None:
        porcupine_wakeword.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
        pa.terminate()
