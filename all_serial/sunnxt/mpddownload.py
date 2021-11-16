#import urllib.request
#for i in range (1,327):
#    a="https://suntvvod.s.llnwi.net/episodes/127277/hd/video/4/seg-"
 #   c=a+str(i)+".m4s"
 #   print(c)
  ##  d=str(i)+".m4s"
 #   urllib.request.urlretrieve(c,d) 
 #   https://suntvvod.s.llnwi.net/episodes/127277/hd/video/4/seg-1.m4s
for i in range(127200,127300):
     print("#EXTINF:-1",end=" ")
     print(i)
     print("https://suntvvod.s.llnwi.net/hls/tvshows/",end="")
     print(i,end="")
     print("/media-1/stream.m3u8?e=1636263905&h=ffb3e7d189cda04d3d5b0a90648d47ee&type=hd&ru=0&PlayBackId=2046245157&cid=127611&country=IN&userid=30107885&nid=0&q=&bw=&op=SUNNXT&did=wuGgLm/s2KnXtGW1Qx/uLg==")