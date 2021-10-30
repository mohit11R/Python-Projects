from moviepy.editor import VideoFileClip

video_name = ""     # Give video name

clip = VideoFileClip(video_name)

clip.write_gif("mygif.gif" , fps=10)
