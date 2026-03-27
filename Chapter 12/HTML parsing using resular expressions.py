#serach for link values within URL input
import urllib.request,urllib.parse,urllib.error
import re
import ssl

#ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('enter-')
html=urllib.request.urlopen(url,context=ctx).read()
links=re.findall(b'herf="(http[s]?://.*/)"',html)
for link in links:
    print(link.decode())
    