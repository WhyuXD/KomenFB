#Code By WahyuXD
#Gausah So Asik Lah Su
import os,re,sys,bs4,time,json,random,datetime,requests
from rich.panel import Panel as panel
from rich import print as vprint
from time import sleep as turu
ses=requests.Session()

FR = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
sekarang = str(tgl)+" "+str(bln)+" "+str(thn)


def jalan(xnxx):
	for hengker in xnxx + '\n':
		sys.stdout.write(hengker);sys.stdout.flush();turu(0.05)

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi !"
elif 12 <= hour < 15:
  hhl = "Selamat Siang !"
elif 15 <= hour < 17:
  hhl = "Selamat Sore !"
elif 17 <= hour < 18:
  hhl = "Selamat Petang !"
else:
  hhl = "Selamat Malam !"

expired_script = ['01', '11', '2022']

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]


logo = ('''\033[1;91m
 ____    ___   ______      _____  ____  
|    \  /   \ |      T    |     ||    \ 
|  \033[1;92mo\033[1;91m  )Y     Y|      |    |   __j|  \033[1;92mo\033[1;91m  )
|     T|  \033[1;92mO\033[1;91m  |l_j  l_j    |  l_  |     T
|  \033[1;92mO\033[1;91m  ||     |  |  |      |   _] |  \033[1;92mO\033[1;91m  |
|     |l     !  |  |      |  T   |     |
l_____j \___/   l__j      l__j   l_____j

\033[1;97m(+) facebook : WaGyoXD
\033[1;97m(+) whatsapp : 083132458199
\033[1;97m(+) version  : 0.2
''')

def login_cookie():
	os.system('clear')
	print (logo)
	print ("Gunakan Cookie Akun Tumbal, Jangan Akun Kalian")
	cookie = str(input(f"\033[1;97m(+) cookie : \033[1;92m"))
	with requests.Session() as xyz:
		try:
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			jalan ("\n\033[1;97m(+) sedang masuk tunggu sebentar...")
			menu()
		except requests.exceptions.ConnectionError:
			print ("\033[1;97m(+) koneksi internet bermasalah !!!")
			exit()
		except (KeyError,IOError):
			print ("\033[1;97m(+) cookie anda invalid !!!")
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login_cookie() 
			

			

def menu():
	os.system('clear')
	print (logo)
	print ("Selamat Datang Di Menu Tools Bot Facebook")
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	id = jsx["id"]
	print ("\033[1;97m(+) User Active : \033[1;92m"+ nama + "")
	print ("\033[1;97m(+) Facebook Id : \033[1;92m"+ id + "")
	print ("")
	print ("\033[1;97m(1) bot coment posts facebook ")
	print ("\033[1;97m(0) log out ( keluar )")
	pahrul = input ("\n\033[1;97m(+) choose : ")
	if pahrul =="1":
		bot_komen()
	elif pahrul =="0":
		jalan ("\033[1;97m(+) tunggu sebentar sedang menghapus cookie...")
		os.system("rm cookie.txt")
		os.system("rm token.txt")
		login_cookie()
	else:
		print("\033[1;97m(+) ngetik apasih goblog !!!")
		exit()
		

def bot_komen():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	os.system("clear")
	print (logo)
	print ("(!) Masukan Id Akun Target Kalian. Misal: 100070916004396")
	idx = input(f"\033[1;97m(+) id target : ")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	if 'name' not in cek:
		exit()
	else:
		lim = input(f"\033[1;97m(+) limit : ")
		jalan ("\n\033[1;97m(+) please wait...\n")
		post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
		if 'error' in post:
			exit()
		elif 'feed' not in post:
			exit()
		else:
			for i in post['feed']['data']:
				tag = ("@["+ idx +":]")
				texs = random.choice(['"Kamu layaknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey'])
				kom = ("Komentar Ini Ditulis Oleh Bot Wahyu")
				waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
				_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + hhl + "\n"+ tag + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()

				if 'id' in submit:
					print(f"\033[1;92m[✓] SUCCES : "+submit['id'])
				else:
					print(f"\033[1;91m[!] FAILED : "+i['id'])
			else:
				print(f"\n\033[1;97m(+) finished...")
				input(f"\n\033[1;97m[<BACK>]")
				menu()


login_cookie()
