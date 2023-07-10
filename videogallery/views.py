from django.http import HttpResponse
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer


class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        url1 = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        url2 = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"
        url3 = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
        url4 = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4"
        url5 = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
        url6 = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4"

        video = Video()
        video.title = "Big Buck Bunny"
        video.videoUrl = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        video.thumbnail = "images/BigBuckBunny.jpg"
        video1 = Video("1", "Big Buck Bunny", url1, "images/ForBiggerBlazes.jpg")
        video2 = Video("2", "Elephant Dream", url2, "images/ElephantsDream.jpg")
        video3 = Video("3", "For Bigger Blazes", url3, "images/ForBiggerBlazes.jpg")
        video4 = Video("4", "For Bigger Escapes", url4, "images/ForBiggerEscapes.jpg")
        video5 = Video("5", "For Bigger Fun", url5, "images/ForBiggerFun.jpg")
        video6 = Video("6", "For Bigger Joyrides", url6, "images/ForBiggerJoyrides.jpg")

        # videos = [video]
        videos = [video1, video2, video3, video4, video5, video6]
        # videos = [video1, video2]
        # video_url = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
        # response = requests.get(video_url, stream=True)
        # videos = response.json()
        return videos

# def fetch_video(self):
#     video_url = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
#     response = requests.get(video_url, stream=True)
#
#     if response.status_code == 200:
#         response_content_type = response.headers['Content-Type']
#         return HttpResponse(response, content_type=response_content_type)
#
#     return HttpResponse('Video Not Found', status=response.status_code)
