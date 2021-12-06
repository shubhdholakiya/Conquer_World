from pytube import YouTube

link = YouTube("https://www.youtube.com/watch?v=QCIAGwQnJ4Y&list=PLKPf-MHoBx0APPS4kdCi6JAaxEJwZPFuJ&index=2")

video = link.streams.get_highest_resolution()

video.download("E:\WorkSpace\Epic Python Series\Audiobook")