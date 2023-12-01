#check if opencv installed 
import cv2
print(cv2.__version__)
#check if ffmpeg installed
import subprocess
subprocess.run(["ffmpeg", "-version"])
#check if flask installed
import flask
print(flask.__version__)
#check if flask_cors installed
import flask_cors
print(flask_cors.__version__)
#check if numpy installed
import numpy
print(numpy.__version__)