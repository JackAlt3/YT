# install in the cmd
# pip install youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import os
# put in the "" the final part of the video in the address bar of the browser
#srt = YouTubeTranscriptApi.get_transcript("Yy1yx9uTHIs")
video_id = "ce5tWoPPRIQ"
#transcript_list = YouTubeTranscriptApi.list_transcripts("Yy1yx9uTHIs")
transcript = YouTubeTranscriptApi.get_transcript("Yy1yx9uTHIs", languages=['en'])
#transcript = transcript_list.find_transcript(['de', 'en','hi'])
print(transcript)
#print(srt)
'''
text = ""
with open("file.txt", "w") as file:
    for i in srt:
        text += i["text"] + "..."
    file.write(text)
os.startfile("file.txt")
'''
