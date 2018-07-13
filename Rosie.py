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
import pygame

import RPi.GPIO as GPIO

pin = 0

# these are given relative to Rosie's perspective, her Left and Right
left_LED = 11
right_LED = 9

audio_files_location = "/home/pi/RPi/Rosie/audio/mp3/"
# initial_wav_audio_file = "/home/pi/RPi/Rosie/audio/wav/rosie_never_fear_while_rosies_here.wav"
initial_mp3_audio_file = "/home/pi/RPi/Rosie/audio/mp3/rosie_never_fear_while_rosies_here.mp3"
audio_file_paths = []

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(left_LED, GPIO.OUT)
GPIO.setup(right_LED, GPIO.OUT)


def main():
    # initialize the pygame.mixer
    # frequency = 22050, size = -16, channels = 2, buffersize = 4096
    # wav files are 2756 Kb/s
    boot()

    while True:

        for x in range(1, 12, 1):
            blink_lights(2, 0.3, 0.3)
            blink_lights(2, 0.3, 0.3)
            time.sleep(5)

        play_random_mp3()


def boot():
    pygame.mixer.pre_init(22050, -16, 2, 4096)
    pygame.mixer.init()
    pygame.mixer.music.load(initial_mp3_audio_file)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(5)
    load_in_audio_files()


def load_in_audio_files():
    audio_files = []
    audio_files_list = os.listdir(audio_files_location)
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

    print("initial music played . . . ?")


def blink_lights(number_of_blinks, blink_on_duration, blink_off_duration):
    for x in range(1, number_of_blinks):
        # print "LEDs on"
        GPIO.output(left_LED, GPIO.HIGH)
        GPIO.output(right_LED, GPIO.HIGH)
        time.sleep(blink_on_duration)

        # print "LEDs off"
        GPIO.output(left_LED, GPIO.LOW)
        GPIO.output(right_LED, GPIO.LOW)
        time.sleep(blink_off_duration)


def play_random_mp3():
    random_file_name = random.choice(os.listdir(audio_files_location))
    mp3_file_location = audio_files_location + random_file_name
    pygame.mixer.music.load(mp3_file_location)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()


main()
