from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def combine_video_image(video_path, image_path, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Load image clip
    image_clip = ImageClip(image_path, duration=video_clip.duration)

    # Composite video and image
    final_clip = CompositeVideoClip([video_clip.set_position('center'), image_clip.set_position('center')])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

if __name__ == "__main__":
    video_path = "3.mp4"
    image_path = "man.png"
    output_path = "output_combined.mp4"

    combine_video_image(video_path, image_path, output_path)
