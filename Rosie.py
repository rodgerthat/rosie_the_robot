"""
 " ;FileName: Rosie
 " ;Author: goat 
 " ;Created: 7/12/18
 " ;Description: Rosie the Robot!
 " ;URL
 """

import os
import random
import time
import threading
import pygame

import RPi.GPIO as GPIO

import ADXL345.Adafruit_I2C as Adafruit_I2C
import ADXL345.Adafruit_ADXL345 as Adafruit_ADXL345

from mutagen.mp3 import MP3

# TODO : Don't 4get to add a script to run on system boot

class Rosie:
    # um, some pin for holding a pin number. . .
    pin = 0
    ticks = 0  # an increment tracker for the timer

    # these are given relative to Rosie's perspective, her Left and Right
    left_LED = 11
    right_LED = 9

    # audio file paths & setup
    audio_files_location = "/home/pi/RPi/Rosie/audio/mp3/"
    # initial_wav_audio_file = "/home/pi/RPi/Rosie/audio/wav/rosie_never_fear_while_rosies_here.wav"
    initial_mp3_audio_file = "/home/pi/RPi/Rosie/audio/mp3/rosie_never_fear_while_rosies_here.mp3"
    wheels_noise_mp3_audio_file = "/home/pi/RPi/Rosie/audio/mp3/rosie_wheels_noise.mp3"
    audio_file_paths = []

    accelerometer = object

    def __init__(self):

        # Setup Pi Board
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.left_LED, GPIO.OUT)
        GPIO.setup(self.right_LED, GPIO.OUT)


    # boot up rosie,
    # initialize the pygame mixer and load in an initial sound byte(s) to play
    def boot(self):

        # set the accelerometer
        self.accelerometer = Adafruit_ADXL345()

        # initialize the pygame.mixer
        # frequency = 22050, size = -16, channels = 2, buffersize = 4096
        # wav files are 2756 Kb/s
        pygame.mixer.pre_init(22050, -16, 2, 4096)
        pygame.mixer.init()
        pygame.mixer.music.load(self.initial_mp3_audio_file)
        # while !pygame.mixer.get_busy():

        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        # load_in_audio_files()

    # run, rosie, run!
    def run(self):

        self.update()

    def update(self):

        # set timer to execute update method every second
        threading.Timer(1.0, self.update).start()
        print("ticks: " + str(self.ticks))

        self.ticks += 1  # iterator, iterate

        # python treats non~zero values as true, so we have to not this conditional
        # here, we control the timing of LED blinks and audio soundbites playing
        if not self.ticks % 30:
            # get length of soundbite
            # soundbite_length = self.get_mp3_audio_length()
            self.blink_lights(2, 0.3, 0.3)
            self.play_random_soundbite()

        if not self.ticks % 11:
            self.blink_lights(2, 0.3, 0.3)
            self.play_wheel_noise()

        # display accelerometer data
        print(self.get_accelerometer_values())

    def load_in_audio_files(self):

        audio_files = []
        audio_files_list = os.listdir(self.audio_files_location)
        print(audio_files_list)
        # for v in audio_files_list:
        #     print(v)
        #     print(audio_files_location + v)
        #     audio_files.append(pygame.mixer.Sound(audio_files_location + v)

        # return audio_files

        # initial_sound = pygame.mixer.Sound(initial_wav_audio_file)
        # initial_sound.set_volume(1.0)
        # initial_sound.play()
        # print("initial sound played . . . ?")
        # initial_sound.stop()

    def blink_lights(self, number_of_blinks, blink_on_duration, blink_off_duration, blink_time):

        for x in range(1, number_of_blinks):
            # print "LEDs on"
            GPIO.output(self.left_LED, GPIO.HIGH)
            GPIO.output(self.right_LED, GPIO.HIGH)
            time.sleep(blink_on_duration)

            # print "LEDs off"
            GPIO.output(self.left_LED, GPIO.LOW)
            GPIO.output(self.right_LED, GPIO.LOW)
            time.sleep(blink_off_duration)

    def play_wheel_noise(self):

        # make sure no other sound is being played first.
        if not pygame.mixer.get_busy():
            pygame.mixer.music.load(self.wheels_noise_mp3_audio_file)
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()

    def play_random_soundbite(self):

        # make sure no other sound is being played first.
        if not pygame.mixer.get_busy():
            random_file_name = random.choice(os.listdir(self.audio_files_location))
            mp3_file_location = self.audio_files_location + random_file_name
            pygame.mixer.music.load(mp3_file_location)
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()

    # uses mutagen to get the length of an mp3 file in milliseconds
    def get_mp3_audio_length(self, file_path):
        audio = MP3(file_path)
        print audio.info.length
        return audio.info.length

    def get_accelerometer_values(self):
        return self.accelerometer.read()


def main():

    rosie = Rosie()
    rosie.boot()
    rosie.run()


main()
