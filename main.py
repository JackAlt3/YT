# install in the cmd
# pip install youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import os
# put in the "" the final part of the video in the address bar of the browser
transcript = YouTubeTranscriptApi.get_transcript("Yy1yx9uTHIs", languages=['hi']) #put yr yt code and language

text = ""

for i in transcript:
    text += i["text"] + "..."
print(text)
