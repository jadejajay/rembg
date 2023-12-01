# -y -i http://itekindia.com/chats/videos/13.mp4 -i http://itekindia.com/chats/frames/format20.webp -filter_complex "[0:v]scale=1024:1024 [video]; [video][1:v]overlay=0:0 [output]" -map 0:a -c:a copy -map 0:a -strict -2 -c:a aac -map "[output]"  -q:v 1 temp.mp4
import time
import subprocess

def run_ffmpeg_command(command):
    ffmpeg_command2 = f"ffmpeg {command}"
    temp_file_name = f"temp_{int(round(time.time() * 1000))}.mp4"
    ffmpeg_command = """ffmpeg -hide_banner -i http://itekindia.com/chats/videos/13.mp4 -i http://itekindia.com/chats/frames/format20.webp -filter_complex "[0:v]scale=1024:1024 [video]; [video][1:v]overlay=0:0 [output]" -map 0:a -c:a copy -map 0:a -strict -2 -c:a aac -map "[output]"  -q:v 1 """+temp_file_name
    process = subprocess.run(ffmpeg_command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = process.stdout
    delete_temp_file = f"rm {temp_file_name}"
    subprocess.run(delete_temp_file, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    print("Output length:", len(output))  # Add this line to check the length of the output
    #output status code
    print("Output status code:", process.returncode)  # Add this line to check the status code of the process
    return output

if __name__ == "__main__":
    print(run_ffmpeg_command("-h"))
##################################################################################################################################
import time
import subprocess
from flask import Flask, request, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def run_ffmpeg_command(input_video: str, input_image: str, temp_file_name: str):
    ffmpeg_command = f"""ffmpeg -hide_banner -i {input_video} -i {input_image} -filter_complex "[0:v]scale=1024:1024 [video]; [video][1:v]overlay=0:0 [output]" -map 0:a -c:a copy -map 0:a -strict -2 -c:a aac -map "[output]"  -q:v 1 {temp_file_name}"""
    process = subprocess.run(ffmpeg_command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = process.returncode
    return output

def read_file(file: str):
    with open(file, "rb") as image_file:
        return image_file.read()

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        input_image = request.files['image']
        input_video = request.form['video']
        temp_file_video = f"temp_{int(round(time.time() * 1000))}.mp4"
        temp_file_image = f"temp_{int(round(time.time() * 1000))}{input_image.filename}"
        #write image to temp file 
        input_image.save(temp_file_image)
        exit_code = run_ffmpeg_command(input_video, temp_file_image, temp_file_video)
        if (exit_code != 0):
            return "Error in processing the video"
        else:
            fileData = read_file(temp_file_video)
            delete_temp_file = f"rm {temp_file_video}"
            delete_temp_file2 = f"rm {temp_file_image}"
            subprocess.run(delete_temp_file, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            subprocess.run(delete_temp_file2, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            header = {'Content-type': 'video/mp4', 'Content-Disposition': 'attachment; filename="output.mp4"'}
            return make_response(fileData, header)
    else:
        return "Hello, You are an Imposter!, You are not supposed to be here!, Go away!, Shoo!, Shoo!, Shoo!"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)