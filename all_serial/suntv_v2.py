#python program to check working lin
import urllib.request
import os
from urllib.error import HTTPError
links=[]
link=["http://64.31.35.62/~tamilshow/downloads/load//Sun%20Tv/03.11.2021/Roja%20(03.11.2021).mp4","https://www.thiraisorgam.com/v/vijay/0311ps/hd/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311abi/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/abi0311/380/playlist.m3u8","https://www.thiraisix.com/v/vijay/0311ps/720/playlist.m3u8","https://www.thiraisix.com/v/sun/ct0311/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311kay/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0311abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311abi/720/playlist.m3u8","https://www.thiraione.com/v/sun/0311abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/ct1026/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/ct0311/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu1103/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311kay/480/playlist.m3u8","https://www.thiraione.com/v/sun/0311ct/720/playlist.m3u8","https://www.thiraisix.com/v/zee/ct1026/720/playlist.m3u8","https://cdn.tamilbliss.com/v/sun/0311ct/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311abi1634738534/480/playlist.m3u8","https://www.thiraifour.com/v/sun/0311sun/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311vp/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311vp1/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311vp/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0311vp/240/playlist.m3u8","https://www.thiraisix.com/v/sun/1026pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0311pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/pu0311/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0311pu/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu0311/720/playlist.m3u8","https://cdn.tamilbliss.com:443/v/sun/0311aru/720/playlist.m3u8","https://www.thiraione.com:443/v/sun/0311aru/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0311aru/720/playlist.m3u8"]
for a in link:
 try:
   urllib.request.urlretrieve(a,'video_name.m3u8') 
 except HTTPError:
  print("not:",a)
 else:
  links.append(a)
for j in links:
  print(j)
f = open("suntvserial_v2.m3u","w")
f.write("#EXTM3U\n")
keys = ["0311ps","0311sun","aru", "ct", "abi", "vp", "pu", "kay","Roja"]
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
        urllib.request.urlretrieve(i,'abi.m3u8') 
        with open(r'video_name.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r'abi.m3u8','w') as file:
	        file.write(data)
        with open(r'abi.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'abi.m3u8','w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring =="Roja"):
        f.write('#EXTINF:-1 tvg-logo="https://tamildhool.b-cdn.net/wp-content/uploads/2021/08/ROJ-1.jpg" group-title="SERIAL",ROJA\n')
        f.write(i)
        f.write('\n')
      elif(substring =="0311sun"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/7fe542a265f3fef7ece784ed6e984c90d8a74909/all_serial/Images/sundari.png?raw=true" group-title="SERIAL",SUNDARI\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'sun.m3u8') 
        with open(r'sun.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r'sun.m3u8','w') as file:
	        file.write(data)
        with open(r'sun.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'sun.m3u8','w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring == "ct"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/0269331533079bbe982e472bc8f4f7da8ea73184/all_serial/Images/chithi2.png?raw=true" group-title="SERIAL",CHITTHI 2\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'ct.m3u8') 
        with open(r'ct.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r'ct.m3u8','w') as file:
	        file.write(data)
        with open(r'ct.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'ct.m3u8','w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring == "vp"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/7fe542a265f3fef7ece784ed6e984c90d8a74909/all_serial/Images/vanthaipola.png?raw=true" group-title="SERIAL",VANATHA POLA"\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'vp.m3u8')
        with open(r'vp.m3u8','r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r'vp.m3u8','w') as file:
	        file.write(data)
        with open(r'vp.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'vp.m3u8','w') as file:
	        file.write(data)
        print("psText replaced")
      elif(substring == "pu"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/db736b6ae6f1416cca65844856a5f60f7a5753e4/all_serial/Images/pooveunnakaga.png?raw=true" group-title="SERIAL",POOVE UNAKAGA\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'pu.m3u8')
        with open(r'pu.m3u8', 'r') as file:
          data = file.read()
          data = data.replace("fileSequence",i+"fileSequence")
        with open(r'pu.m3u8','w') as file:
	        file.write(data)
        with open(r'pu.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'pu.m3u8','w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring == "kay"):
        f.write('#EXTINF:-1 tvg-logo="https://www.tamildhool.net/wp-content/uploads/2021/10/kal.jpg" group-title="SERIAL",KAYAL\n')
        f.write(i)
        f.write('\n')
      elif(substring == keys[0]):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/87ac4e85cc497653eb5c62349e26cf8496259643/all_serial/Images/pandianstores.png?raw=true" group-title="SERIAL",PANDIAN STORES\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'ps.m3u8')
        with open(r'ps.m3u8','r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r'ps.m3u8','w') as file:
	        file.write(data)
        with open(r'ps.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'ps.m3u8','w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring =="aru"):
        f.write('#EXTINF:-1 tvg-logo="https://tamildhool1.net/wp-content/uploads/2021/10/Aruvi-300x160.jpg" group-title="SERIAL",ARUVI\n')
        f.write(i)
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'aru.m3u8')
        with open(r'aru.m3u8','r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r'aru.m3u8','w') as file:
	        file.write(data)
        with open(r'aru.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r'aru.m3u8','w') as file:
	        file.write(data)
        
        print("psText replaced")
f.close()
