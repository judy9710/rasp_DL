#!/usr/bin/env python
from flask import Flask, render_template, Response
import picamera
from camera import Camera

import pyaudio
import time
import datetime
import ftplib
import os
import shutil


app = Flask(__name__)


#@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_cap')
def video_cap():
    ftp=ftplib.FTP()
    print('Before connected')
    ftp.connect('192.168.219.157',21)
    ftp.login('user','')
    ftp.cwd('C:\temp\Python\Pi\VideoImage\Input')
    os.chdir('/home/pi/Test/pi/RPIPetFeeder/VideoImage')

    file_list = os.listdir('./')

    picam = picamera.PiCamera()

    while True:
#    for i in range(0,5):
        filename = datetime.datetime.now().strftime("%Y-%-m-%-d %H-%M-%S")
        filename = filename + '.jpg'
        picam.capture(filename)

        myfile=open(filename,'rb')

        ftp.storbinary('STOR ' + str(filename), myfile)

        myfile.close()
#        shutil.move(filename,dest_dir+'/'+filename)  
        os.remove(filename)
        time.sleep(2)
    ftp.close()
    picam.close()

@app.route('/audio')
def audio_cap():

    form_1 = pyaudio.paInt16 #16-bit resolution
    chans = 1
    samp_rate = 44100
    chunk= 4096
    record_secs = 5
    dev_index = 0


#    ftp=ftplib.FTP()
#    ftp.connect('192.168.219.110',21)
#    print('connected')
#    ftp.login('user','')
#    #ftp.cwd('C:\temp\Python\Pi\VideoImage\Input')
#    os.chdir('/home/pi/Test/pi/RPIPetFeeder/AudioSaved')

    audio=pyaudio.PyAudio()

    cnt=0

    while True:
        audio=pyaudio.PyAudio()

        stream = audio.open(format=form_1, rate=samp_rate,channels=chans, \
                    input_device_index = dev_index, input=True, \
                    frames_per_buffer=chunk)

        fname='cough-'+str(cnt)
        cnt=cnt+1
        filename1 = fname+'.wav'

        wav_output_filename= filename1

        frames=[]

#loop through stream and append audio chunks to frame array

        for ii in range(0, int((samp_rate/chunk)*record_secs)):
            data = stream.read(chunk)
            frames.append(data)

#stop the stream, close it, and terminate the pyaudio instantiation

        stream.stop_stream()
        stream.close()

        audio.terminate()

#save the audio frames as .wav file

        wavefile = wave.open(wav_output_filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()


#        myfile=open(wav_output_filename,'rb')

#        ftp.storbinary('STOR ' + str(wav_output_filename), myfile)

#        myfile.close()
#        os.remove(filename1)
#        time.sleep(5)

#ftp.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
