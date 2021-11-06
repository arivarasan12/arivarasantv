import urllib.request
for i in range (1,327):
    a="https://suntvvod.s.llnwi.net/episodes/127277/hd/video/4/seg-"
    c=a+str(i)+".m4s"
    print(c)
    d=str(i)+".m4s"
    urllib.request.urlretrieve(c,d) 
 #   https://suntvvod.s.llnwi.net/episodes/127277/hd/video/4/seg-1.m4s