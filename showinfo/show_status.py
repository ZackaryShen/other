#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zackary
# @Software: PyCharm
# @Email   : szbltyy@hotmail.com
# @Time    : 2019/12/2 下午2:23

# -*- coding: utf-8 -*-

import signal
import time
import os
import platform
import psutil


def signal_handler(signal_num, frame):
    global is_sigint_up
    is_sigint_up = True
    if platform.system() == "Windows":
        os.system("clr")
    elif platform.system() == "Linux":
        os.system('clear')
    print("Goodbye!")
    time.sleep(1)
    if platform.system() == "Windows":
        os.system("clr")
    elif platform.system() == "Linux":
        os.system('clear')


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

is_sigint_up = False

# refresh the screen
if platform.system() == "Windows":
    os.system("clr")
elif platform.system() == "Linux":
    os.system('clear')

while True:
    try:
        print(
            "========================================================================================================")
        print(
            "                                                   /\                                                   ")
        print(
            "                                                  /||\                                                  ")
        print(
            "                                                 /||||\                                                 ")
        print(
            "                                                /||||||\                                                ")
        print(
            "                                               /||||||||\                                               ")
        print(
            "                                              /||||/\||||\                                              ")
        print(
            "                                             /||||/  \||||\                                             ")
        print(
            "                                            /||||/    \||||\                                            ")
        print(
            "                                           /||||/      \||||\                                           ")
        print(
            "                                          /||||/        \||||\                                          ")
        print(
            "                                         /||||/          \||||\                                         ")
        print(
            "                                        /||||/            \||||\                                        ")
        print(
            "                             ----      /||||/              \||||\      ----                             ")
        print(
            "                             ||||\    /||||/                \||||\    /||||                             ")
        print(
            "                              \||||\ /||||/                  \||||\ /||||/                              ")
        print(
            "                              /||||||||||/                    \||||||||||\                              ")
        print(
            "                       |\    |||||||||||/                      \|||||||||||    /|                       ")
        print(
            "                       \||\  ----||||||                         ||||||----  /||/                        ")
        print(
            "                        \|||\   \|||||\                         /|||||/   /|||/                         ")
        print(
            "                          \|||\    \||||\                     /||||/    /|||/                           ")
        print(
            "                            \|||\      -----       |       -----      /|||/                             ")
        print(
            "                               \|||\              / \              /|||/                                ")
        print(
            "                                  \||||\        /|| ||\        /||||/                                   ")
        print(
            "                                     \||||\--/||||| |||||\--/||||/                                      ")
        print(
            "                                        \---------/ \---------/                                         ")
        print(
            "========================================================================================================")

        print("My Computer info:")
        print("Current Time: " + time.strftime(" %Y.%m.%d %H:%M:%S UTC+8", time.localtime(time.time())))
        print("CPU Usage: %.2f" % psutil.cpu_percent() + "% ")
        memory_data = psutil.virtual_memory()
        total_memory = memory_data.total
        available_memory = memory_data.available
        print("Total Memory: %.1lf bytes" % total_memory)
        print("Memory Available: %.1lf bytes" % available_memory)
        print("Memory Usage: %d" % int(round(memory_data.percent)) + "%  ")
        time.sleep(1)
        # refresh the screen
        if platform.system() == "Windows":
            os.system("clr")
        elif platform.system() == "Linux":
            os.system('clear')
        # catch the signal
        if is_sigint_up:
            break
    except Exception:
        print("Error!")
        break