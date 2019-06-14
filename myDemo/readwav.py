# !usr/bin/env python
# coding=utf-8

from tkinter import *
import wave
import matplotlib.pyplot as plt
import numpy as np


def read_wave_data(file_path):
    # open a wave file, and return a Wave_read object
    f = wave.open(file_path, "rb")
    # read the wave's format infomation,and return a tuple
    params = f.getparams()
    # get the info
    nchannels, sampwidth, framerate, nframes = params[:4]
    # Reads and returns nframes of audio, as a string of bytes.
    str_data = f.readframes(nframes)
    # close the stream
    f.close()
    # turn the wave's data to array
    # wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data = np.frombuffer(str_data, 'int16')
    # for the data is stereo,and format is LRLRLR...
    # shape the array to n*2(-1 means fit the y coordinate)
    wave_data.shape = -1, 2
    # transpose the data
    wave_data = wave_data.T
    # calculate the time bar
    time = np.arange(0, nframes) * (1.0 / framerate)
    len_time = len(time) / 2
    time = time[0:int(len_time)]

    print("nchannels = ", nchannels)
    print("time length = ", len(time))
    print("wave_data[0] length = ", len(wave_data[0]))

    return wave_data, time


def wave_plot(filename):
    # open wave file
    wf = wave.open(filename, 'r')
    channels = wf.getnchannels()  # 追記
    print(wf.getparams())

    # load wave data
    chunk_size = 256
    amp = (2 ** 8) ** wf.getsampwidth() / 2
    data = wf.readframes(chunk_size)  # バイナリ読み込み
    data = np.frombuffer(data, 'int16')  # intに変換
    data = data / amp  # 振幅正規化

    # make time axis
    rate = wf.getframerate()
    size = float(chunk_size)
    x = np.arange(0, size / rate, 1.0 / rate)

    # len_x = len(x) / 2
    # x = x[0:int(len_x)]
    print("nchannels = ", channels)
    print("time length = ", len(x))
    print("wave_data[0] length = ", len(data))

    return data, x


def main():
    wave_data, time = read_wave_data(
        r"C:\work\developer\20181026-SpeakerSegregationJar\inputWav\C000056.wav")
    # draw the wave
    plt.subplot(211)
    plt.plot(time, wave_data[0])
    plt.subplot(212)
    plt.plot(time, wave_data[1], c="g")
    plt.show()


if __name__ == "__main__":
    main()
