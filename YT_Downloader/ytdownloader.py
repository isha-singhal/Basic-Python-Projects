#pytube library 
from pytube import YouTube 
Destination=r"C:\Users\HP\Desktop\YT_Downloader\Downloaded_vids"
link="https://youtu.be/qKodeIY-uSI"
try:
	yt=YouTube(link)
except:
	print("SORRY link not working")
#vidfilter=yt.streams.first()
vidfilter = yt.streams.get_highest_resolution()
try:
	vidfilter.download(Destination)
except:
	print("SORRY unable to download")
print("Video is downloaded.. check out the folder")