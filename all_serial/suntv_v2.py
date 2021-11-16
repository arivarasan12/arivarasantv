#python program to check working link
#"http://64.31.35.62/~tamilshow/downloads/load//Sun%20Tv/03.11.2021/Roja%20(03.11.2021).mp","http://83.149.126.229/~tamildub/serials/load//Sun%20Tv/03.11.2021/Roja%20(03.11.2021).mp",
import urllib.request
from urllib.error import HTTPError
links=[]
link=[]
from datetime import date
today = date.today()
today=str(today)


print(today)
month=today[-5:-3]
day=today[-2:]
print("mon",month)
print("day",day)
rdate=day+"-"+month+"-"+"2021"
print("dsfa",rdate)
if(day[0]==0):
 cdate=str(0)+str((int(day)-1))+month
else:
  cdate=str((int(day)-1))+month
cdateps=day+month
olddate=str(0)+str(int(day)-2)+month
print("olddate",olddate)
print("cdate",cdate)
print("cdateps",cdateps)
lin=["https://www.thiraitwo.com/v/sun/0611abi/720/playlist.m3u8","https://www.thiraione.com/v/vijay/1511tsps/sd/playlist.m3u8","https://www.thiraisix.com/v/vijay/1511tsps/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/abi0611/380/playlist.m3u8","https://www.thiraisix.com/v/vijay/0711/720/playlist.m3u8","http://www.thiraione.com/v/vijay/0711ps/hd/playlist.m3u8","https://www.thiraitwo.com/v/vijay/0711ps/720/playlist.m3u8","https://www.thiraisix.com/v/vijay/0711ps/720/playlist.m3u8","https://www.thiraisix.com/v/vijay/0711ps/hd/playlist.m3u8","https://www.thiraisix.com/v/sun/ct0611/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611kay/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0611abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/ct1106/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0611ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/ct0611/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu1106/720/playlist.m3u8","https://www.thiraisix.com/v/sun/poo1106/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0611kay/480/playlist.m3u8","https://www.thiraisix.com/v/zee/ct1106/720/playlist.m3u8","https://cdn.tamilbliss.com/v/sun/0611ct/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611abi/480/playlist.m3u8","https://www.thiraifour.com/v/sun/0611sun/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0611sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0611vp/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0611vp1/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611vp/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0611vp/240/playlist.m3u8","https://www.thiraisix.com/v/sun/1106pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0611pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/pu0611/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0611pu/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu0611/720/playlist.m3u8","https://cdn.tamilbliss.com:443/v/sun/0611aru/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0611aru/720/playlist.m3u8"]
for a in lin:
 a1=a
 b=a1.replace("0711",cdateps)
 b=b.replace("0611",cdate)
 link.append(b)
print("Date Replaced")
for a in link:
 try:
   urllib.request.urlretrieve(a,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\video_name.m3u8") 
 except HTTPError or tiimeout :
  print("not:",a)
 else:
   if("Roja" in a):
     roja.mp4=video.m3u8
   links.append(a)
for j in links:
  print(j)
f = open("C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\suntvserial_v2.m3u","w")
f.write("#EXTM3U\n")
sun=cdate+"sun"
ps=cdateps+"tsps"
keys = [ps,sun,"aru", "ct", "abi", "vp", "pu", "kay","Roja","poo"]
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
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\abi.m3u8") 
        with open(r'C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\abi.m3u8', 'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\abi.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\abi.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\abi.m3u8",'w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring =="Roja"):
        f.write('#EXTINF:-1 tvg-logo="https://tamildhool.b-cdn.net/wp-content/uploads/2021/08/ROJ-1.jpg" group-title="SERIAL",ROJA\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,'roja.mp4')
      elif(substring ==keys[1]):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/7fe542a265f3fef7ece784ed6e984c90d8a74909/all_serial/Images/sundari.png?raw=true" group-title="SERIAL",SUNDARI\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\sun.m3u8") 
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\sun.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\sun.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\sun.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\sun.m3u8",'w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring == "ct"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/0269331533079bbe982e472bc8f4f7da8ea73184/all_serial/Images/chithi2.png?raw=true" group-title="SERIAL",CHITTHI 2\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ct.m3u8") 
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ct.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ct.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ct.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ct.m3u8",'w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring == "vp"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/7fe542a265f3fef7ece784ed6e984c90d8a74909/all_serial/Images/vanthaipola.png?raw=true" group-title="SERIAL",VANATHA POLA"\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\vp.m3u8")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\vp.m3u8",'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\vp.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\vp.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\vp.m3u8",'w') as file:
	        file.write(data)
        print("psText replaced")
      elif(substring =="pu" or substring =="poo"):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/db736b6ae6f1416cca65844856a5f60f7a5753e4/all_serial/Images/pooveunnakaga.png?raw=true" group-title="SERIAL",POOVE UNAKAGA\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\pu.m3u8")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\pu.m3u8", 'r') as file:
          data = file.read()
          data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\pu.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\pu.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\pu.m3u8",'w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring == "kay"):
        f.write('#EXTINF:-1 tvg-logo="https://www.tamildhool.net/wp-content/uploads/2021/10/kal.jpg" group-title="SERIAL",KAYAL\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\kay.m3u8")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\kay.m3u8",'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\kay.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\kay.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\kay.m3u8",'w') as file:
	        file.write(data)
      elif(substring == keys[0]):
        f.write('#EXTINF:-1 tvg-logo="https://github.com/arivarasan12/arivarasantv/blob/87ac4e85cc497653eb5c62349e26cf8496259643/all_serial/Images/pandianstores.png?raw=true" group-title="SERIAL",PANDIAN STORES\n')
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ps.m3u8")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ps.m3u8",'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ps.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ps.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\ps.m3u8",'w') as file:
	        file.write(data)
        
        print("psText replaced")
      elif(substring =="aru"):
        f.write('#EXTINF:-1 tvg-logo="https://tamildhool1.net/wp-content/uploads/2021/10/Aruvi-300x160.jpg" group-title="SERIAL",ARUVI\n')
        f.write(i)
        f.write(i)
        f.write('\n')
        urllib.request.urlretrieve(i,"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\aru.m3u8")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\aru.m3u8",'r') as file:
         data = file.read()
         data = data.replace("fileSequence",i+"fileSequence")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\aru.m3u8",'w') as file:
	        file.write(data)
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\aru.m3u8", 'r') as file:
         data = file.read()
         data = data.replace("playlist.m3u8","")
        with open(r"C:\\Users\\ariva\\OneDrive\\Desktop\\TV\\arivarasantv\\aru.m3u8",'w') as file:
	        file.write(data)
        
        print("psText replaced")
f.close()