from flask import Flask, stream_with_context, request, Response, flash
import time
from time import sleep
from flask import render_template, Response, make_response, redirect, url_for

import os
import shutil
import cv2 as cv

from testing1 import maskdetect
from cough2 import coughdetect

from playsound import playsound

app = Flask(__name__)

video = cv.VideoCapture(0)
count=1

@app.route("/")
def home():
    return render_template("covid-html.html")

input_dir = './VideoImage'+'/'+'Input'
saved_dir = './VideoImage'+'/'+'Saved'
mask_dir = './VideoImage'+'/'+'Masked'
unmask_dir =  './VideoImage'+'/'+'Unmasked'

def gen(video):
    while True:
        tmpfile_list = os.listdir(input_dir)
        infile_list = [file for file in tmpfile_list if file.endswith(".jpg")]
#        print(infile_list)

        if(len(infile_list) == 0):
            sleep(2)

        for i in range(0,len(infile_list)): 
            infilename = input_dir + '/' + infile_list[i]

#            print(infilename)
            image = cv.imread(infilename,1)

            ret, jpeg = cv.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            sleep(1)
            shutil.move(infilename,saved_dir+'/'+infile_list[i])
#            shutil.copy(infilename,saved_dir+'/'+infile_list[i])
            sleep(1)
        tmpfile_list = ""
#        cv.waitKey(1000)
    cv.destroyAllwindows()

@app.route('/video/feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def detectmask(): 
    savefile_list = os.listdir(saved_dir)
#    print(savefile_list)
    if(len(savefile_list) == 0):
        sleep(2)
        savefile_list = os.listdir(saved_dir)
#        print(savefile_list)

    for i in range(0,len(savefile_list)): 
        filename = saved_dir + '/' + savefile_list[i]

#        print('detectmask:'+filename)
        maskdetect(savefile_list[i])
        os.remove(filename)

def genmask(video):      
    while True:
        mask_list = os.listdir(mask_dir)
#        print(mask_list)
        if(len(mask_list) == 0):
            detectmask()
            mask_list = os.listdir(mask_dir)
                
        for i in range(0,len(mask_list)): 
            maskname = mask_dir + '/'+mask_list[i]
            image = cv.imread(maskname,1)

            ret, jpeg = cv.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            sleep(1)
            shutil.move(maskname,unmask_dir+'/'+mask_list[i])
#            os.remove(filename)
        cv.waitKey(1000)
    cv.destroyAllwindows()

@app.route('/mask/detect')
def mask_detect():
    global video
    return Response(genmask(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/cough')
def download_file():
    cough_dir ='./VideoImage'+'/'+'Input'

    while True:
        tfile_list = os.listdir(cough_dir)
        coughfile_list = [file for file in tfile_list if file.endswith(".wav")]
#        print(coughfile_list)

        if(len(coughfile_list) == 0):
            sleep(2)

        for i in range(0,len(coughfile_list)): 
            audioname = cough_dir + '/' + coughfile_list[i]
            coughdetect(audioname)
            playsound('cough.wav')

#            os.remove(audioname)
            sleep(2)

    return render_template("covid-html.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
