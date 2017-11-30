# -*- coding: utf-8 -*-
import requests
import time

dolarurl = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
eurourl = "https://kur.doviz.com/serbest-piyasa/euro"
btcurl = "https://tr.investing.com/currencies/btc-usd"
ethurl = "https://www.doviz.com/ethereum"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
	r = requests.get(btcurl, headers=headers)
	btc=r.text[r.text.index('-last" id="last_last" dir="ltr">'):r.text.index('-last" id="last_last" dir="ltr">')+100]
	btclast=btc[btc.index(">")+1:btc.index("<")]

	r= requests.get(dolarurl, headers=headers)
	dolar=r.text[r.text.index('<span class="menu-row1">DOLAR</span>'):r.text.index('<span class="menu-row1">DOLAR</span>')+600]
	dolarlast=dolar[dolar.index("row2")+6:dolar.index("row2\">")+12]

	r= requests.get(eurourl, headers=headers)
	euro=r.text[r.text.index('<span class="menu-row1">EURO</span>'):r.text.index('<span class="menu-row1">EURO</span>')+600]
	eurolast=euro[euro.index("row2")+6:euro.index("row2\">")+12]


	r= requests.get(ethurl, headers=headers)
	eth=r.text[r.text.index('<span class="m10-0">Ethereum/T'):r.text.index('<span class="m10-0">Ethereum/T')+600]
	ethlast=eth[eth.index("row2")+290:eth.index("row2\">")+305][eth[eth.index("row2")+290:eth.index("row2\">")+305].index("\"")+2:eth[eth.index("row2")+290:eth.index("row2\">")+305].index("/")-1]



    	print  bcolors.OKBLUE + "BTC  : " + btclast+ bcolors.ENDC+ "    " +bcolors.OKGREEN +  " DOLAR :  "+dolarlast +  "    " + bcolors.WARNING + "  EURO:  "  +eurolast+ "    "  +  bcolors.FAIL + " ETH : "+ ethlast +  "    " + bcolors.ENDC+ time.strftime("%H:%M:%S")  
	time.sleep(10)


