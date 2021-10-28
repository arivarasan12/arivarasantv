import urllib.request
import os
from urllib.error import HTTPError
links=[]
link=["https://www.thiraisix.com/v/vijay/2810ps/720/playlist.m3u8","https://www.thiraisix.com/v/sun/ct2710/720/playlist.m3u8","https://www.thiraisix.com/v/sun/2710kay/720/playlist.m3u8","https://www.thiraifour.com/v/sun/2710abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/2710abi/720/playlist.m3u8","https://www.thiraione.com/v/sun/2710abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/ct1026/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/2710ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/ct2710/720/playlist.m3u8","https://www.thiraione.com/v/sun/2710ct/720/playlist.m3u8","https://www.thiraisix.com/v/zee/ct1026/720/playlist.m3u8","https://cdn.tamilbliss.com/v/sun/2710ct/720/playlist.m3u8","https://www.thiraisix.com/v/sun/2710abi1634738534/480/playlist.m3u8","https://www.thiraifour.com/v/sun/2710sun/720/playlist.m3u8","https://www.thiraisix.com/v/sun/2710sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/2710sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/2710vp/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/2710vp1/720/playlist.m3u8","https://www.thiraisix.com/v/sun/2710vp/720/playlist.m3u8","https://www.thiraifour.com/v/sun/2710vp/240/playlist.m3u8","https://www.thiraisix.com/v/sun/1026pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/2710pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/pu2710/720/playlist.m3u8","https://www.thiraisix.com/v/sun/2710pu/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu2710/720/playlist.m3u8","https://cdn.tamilbliss.com:443/v/sun/2710aru/720/playlist.m3u8","https://www.thiraione.com:443/v/sun/2710aru/720/playlist.m3u8","https://www.thiraifour.com/v/sun/2710aru/720/playlist.m3u8"]
for a in link:
 try:
   urllib.request.urlretrieve(a, 'video_name.m3u8') 
 except HTTPError:
  pass
 else:
  links.append(a)
for j in links:
  print(j)
file ="suntvserial_v2.m3u"
path = os.getcwd()+file
f = open(path, "w")
f.write("#EXTM3U\n")
keys = ["2810ps", "2710sun", "aru", "ct", "abi", "vp", "pu", "kay"]
for i in links:
 fullstring = i
 for j in keys:
    substring = j
    z=int(fullstring.find(substring))
    if (z!=-1):
      if(substring == "abi"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/99682071a6d6cab85d7290fda4e100e03fdb78eb/all_serial/Images/abhium_nanum.png?raw=true" group-title="SERIAL",ABHIYUM NANUM\n')
        f.write(i)
        f.write('\n')
      elif(substring == "2710sun"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/7fe542a265f3fef7ece784ed6e984c90d8a74909/all_serial/Images/sundari.png?raw=true" group-title="SERIAL",SUNDARI\n')
        f.write(i)
        f.write('\n')
      elif(substring == "ct"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/0269331533079bbe982e472bc8f4f7da8ea73184/all_serial/Images/chithi2.png?raw=true" group-title="SERIAL",CHITTHI 2\n')
        f.write(i)
        f.write('\n')
      elif(substring == "vp"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/7fe542a265f3fef7ece784ed6e984c90d8a74909/all_serial/Images/vanthaipola.png?raw=true" group-title="SERIAL",VANATHA POLA"\n')
        f.write(i)
        f.write('\n')
      elif(substring == "pu"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/db736b6ae6f1416cca65844856a5f60f7a5753e4/all_serial/Images/pooveunnakaga.png?raw=true" group-title="SERIAL",POOVE UNAKAGA\n')
        f.write(i)
        f.write('\n')
      elif(substring == "kay"):
        f.write('#EXTINF:-1 tvg-logo="https://www.tamildhool.net/wp-content/uploads/2021/10/kal.jpg" group-title="SERIAL",KAYAL\n')
        f.write(i)
        f.write('\n')
      elif(substring == "2810ps"):
        f.write('#EXTINF:-1 tvg-logo="https://gi"https://github.com/arivarasan12/arivarasantv/blob/87ac4e85cc497653eb5c62349e26cf8496259643/all_serial/Images/pandianstores.png?raw=true" group-title="SERIAL",PANDIAN STORES\n')
        f.write(i)
        f.write('\n')
f.close()
