from datetime import date
today = date.today()
today=str(today)
print(today)
month=today[-5:-3]
day=today[-2:]
print(month)
print(day)
cdate=str(0)+str((int(day)-1))+month
cdateps=day+month
olddate=str(0)+str(int(day)-2)+month
print(olddate)
print(cdate)
print(cdateps)
link=["https://www.thiraitwo.com/v/sun/0511abi/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/abi0511/380/playlist.m3u8","https://www.thiraisix.com/v/vijay/0611ps/720/playlist.m3u8","http://www.thiraione.com/v/vijay/0611ps/hd/playlist.m3u8","https://www.thiraitwo.com/v/vijay/0611ps/720/playlist.m3u8","https://www.thiraisix.com/v/vijay/0611ps/hd/playlist.m3u8","https://www.thiraisix.com/v/sun/ct0511/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511kay/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0511abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511abi/720/playlist.m3u8","https://www.thiraisix.com/v/sun/ct0511/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0511ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/ct0511/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu1106/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511ct/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0511kay/480/playlist.m3u8","https://www.thiraisix.com/v/zee/ct0511/720/playlist.m3u8","https://cdn.tamilbliss.com/v/sun/0511ct/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511abi/480/playlist.m3u8","https://www.thiraifour.com/v/sun/0511sun/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0511sun/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0511vp/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0511vp1/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511vp/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0511vp/240/playlist.m3u8","https://www.thiraisix.com/v/sun/0511pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/0511pu/720/playlist.m3u8","https://www.thiraitwo.com/v/sun/pu0511/720/playlist.m3u8","https://www.thiraisix.com/v/sun/0511pu/720/playlist.m3u8","https://www.thiraisix.com/v/sun/pu0511/720/playlist.m3u8","https://cdn.tamilbliss.com:443/v/sun/0511aru/720/playlist.m3u8","https://www.thiraifour.com/v/sun/0511aru/720/playlist.m3u8"]
for a in lin:
 a1=a
 b=a1.replace(cdate,cdateps)
 b=b.replace(olddate,cdate)
 links.append(b)


