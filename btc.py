import requests
import time

url = "https://tr.investing.com/currencies/btc-usd"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"}

r = requests.get(url, headers=headers)
foostring=r.text[r.text.index('-last" id="last_last" dir="ltr">'):r.text.index('-last" id="last_last" dir="ltr">')+100]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

isFirst=True
startingValue = 0.0
while True:
	r = requests.get(url, headers=headers)
	foostring=r.text[r.text.index('-last" id="last_last" dir="ltr">'):r.text.index('-last" id="last_last" dir="ltr">')+100]
	laststring=foostring[foostring.index(">")+1:foostring.index("<")]
	tmp=foostring[foostring.index(">")+1:foostring.index("<")]+"    "+time.strftime("%H:%M:%S")
	val= float(foostring[foostring.index(">")+1:foostring.index("<")].replace(".", "").replace(",", "."))
    	if isFirst:
		
		print  tmp
		startingValue=val
		time.sleep(10)
		isFirst=False
	else: 
		
		
		if val > startingValue:
			print  bcolors.OKGREEN + laststring+ bcolors.ENDC+ "    " +time.strftime("%H:%M:%S")  
		elif val< startingValue:
			print  bcolors.FAIL + laststring+ bcolors.ENDC+ "    " +time.strftime("%H:%M:%S")  
		else:
			print  laststring+"    "+time.strftime("%H:%M:%S")
		time.sleep(10)


