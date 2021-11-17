import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=XHF1j9PvowY&list=PLKPf-MHoBx0APPS4kdCi6JAaxEJwZPFuJ")
img.save("Playlist.jpg")