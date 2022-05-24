import requests, uuid, random, re, ctypes, json, urllib, hashlib, hmac, urllib.parse, base64, os, string, time, colorama, autopy
from time import sleep
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
from requests.models import Response
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
from threading import Thread, Lock
from termcolor import colored
import sys
colorama.init()
timestamp = str(int(time.time()))

def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join((random.choice(letters) for i in range(n)))


def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join((random.choice(letters) for i in range(n)))


def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join((random.choice(letters) for i in range(n)))


def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join((random.choice(letters) for i in range(n)))


def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join((random.choice(letters) for i in range(stringLength - 1)))
    return RandomStringChars(1) + result


uu = '83f2000a-4b95-4811-bc8d-0f3539ef07cf'
head = {'Host':'i.instagram.com',
 'Accept':'*/*',
 'Accept-Encoding':'gzip, deflate',
 'Accept-Language':'en-US',
 'User-Agent':'Instagram 123.1.0.26.114 (iPhone 12 ProMax)',
 'X-IG-Capabilities':'3brTvw==',
 'X-IG-Connection-Type':'WIFI',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'Connection':'keep-alive'}

class Design:
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    s1 = '\x1b[36m1\x1b[31m'
    s2 = '\x1b[36m2\x1b[31m'
    one = f"\x1b[31m[{s1}]\x1b[31m"
    tow = f"\x1b[31m[{s2}]\x1b[31m"
    eq = '\x1b[36m≈\x1b[31m'
    eq1 = f"\x1b[31m[{eq}]\x1b[31m"
    equl = '\x1b[36m=\x1b[31m'
    equl1 = f"\x1b[31m[{equl}]\x1b[31m"
    du = '\x1b[36m≠\x1b[31m'
    du1 = f"\x1b[31m[{du}]\x1b[31m"
    plus = '\x1b[36m+\x1b[31m'
    plus2 = '\x1b[32m+\x1b[36m'
    mains = '\x1b[36m-\x1b[31m'
    SL = '\x1b[36m/\x1b[31m'
    INPUT = f"\x1b[31m[ {plus} ]\x1b[31m"
    INPUT0 = f"\x1b[36m[{plus2}]\x1b[36m"
    INPUT1 = f"\x1b[31m[{SL}]\x1b[31m"
    INPUT2 = f"\x1b[31m[{mains}]\x1b[39m"
    marka = '\x1b[32m✓\x1b[36m'
    INPUT3 = f"\x1b[36m[{marka}]\x1b[36m"
    blueq = '\x1b[36m\x1b[40m'
    reda = '\x1b[31m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    purble = '\x1b[35m\x1b[39m'
    SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
    Run = '\x1b[36m Started Running...\x1b[31m'
    under = '\x1b[35m_\x1b[39m'
    skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
    clearConsle = lambda : os.system('cls')
    clearTermnal = lambda : os.system('cls')
    qube = '['
    qube2 = ']'
    grey = 'gray'
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'
    cyan = 'cyan'
    white = 'white'
    right = 'Made By Psycho Rayan'
    banner = "\n                        \n                                \n            ,-.          ,          .   .   \n            |  \\         |    o     |   |   \n            |  | ,-: . . |    . ,-: |-. |-  \n            |  / | | | | |    | | | | | |   \n            `-'  `-` `-| `--' ' `-| ' ' `-' \n                    `-'        `-'     \n\n\n\n"


app_name = 'Daylight v3'

#def HostName() -> int:
#    ip = requests.get('https://api.ipify.org/?format=text').text
#    return ip


#def Check_File():
#    host = open('C:\\Windows\\System32\\drivers\\etc\\hosts').read()
#    if host.__contains__('falcon-society'):
#        print('The Host Uses DnsSpofing Enter To Exit :)')
#        input()
#        exit(0)


#def active():
#    IpAddress = HostName()
#    req = requests.get('https://falcon-society.com/active_link/' + app_name + '/' + IpAddress)
#    if req.headers['Server'] != 'cloudflare':
#       print('The Server Uses DnsSpofing Enter To Exit :)')
#        input()
#        exit(0)
#    elif 'True' in req.text:
#        pass
#    else:
#        print(f"{IpAddress} Isn't Active Please Contact With 31421 - 1k3k")
#        input()
#        exit(0)
#    Check_File()


#active()

class sessting:

    def __init__(self):
        pass

    def headers_login(self):
        headers = {}
        headers['User-Agent'] = self.UserAgent
        headers['Host'] = 'i.instagram.com'
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        return headers

    def generateUSER_AGENT(self):
        Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
        DPIs = [
         '480', '320', '640', '515', '120', '160', '240', '800']
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180
        DEVICE_SETTINTS = {'system':'Android',
         'Host':'Instagram',
         'manufacturer':f"{random.choice(Devices_menu)}",
         'model':f"{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}",
         'android_version':random.randint(18, 25),
         'android_release':f"{random.randint(1, 7)}.{random.randint(0, 7)}",
         'cpu':f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
         'resolution':f"{randResolution}x{lowerResolution}",
         'randomL':f"{RandomString(6)}",
         'dpi':f"{random.choice(DPIs)}"}
        return ('{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format)(**DEVICE_SETTINTS)

    def generate_DeviceId(self, ID):
        volatile_ID = '12345'
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]


def LoadFile(name, path):
    try:
        with open(path, 'r') as (myfile):
            file = myfile.read().splitlines()
    except:
        inputc(False, '?', Design.yellow, f"{name} Path : ")
        pa = input()
        path2 = re.search("'(.*?)'", pa).group(1)
        with open(path2, 'r') as (myfile):
            file = myfile.read().splitlines()
    else:
        if len(file) <= 0:
            inputc(False, '!', Design.red, f"{name} Empty File")
            input()
            exit(0)
        else:
            inputc(False, (f"{len(file)}"), Design.green, f"{name} Loaded Successfully \n")
            return file


def inputc(Frist_NewLine, mark, color, text):
    if Frist_NewLine:
        Frist_NewLine = '\n'
    print(f"""{Frist_NewLine}\r{Design.qube} {colored(text=(f"{mark}"), color=(f"{color}"))} {Design.qube2} {text} {colored(text='', color=(Design.white))}""", end='')


class login:

    def __init__(self):
        self.sesstings = sessting()
        self.coo = None
        self.token = None
        self.mid = None
        self.DeviceID = None
        self.sessionid = None

    def headers_login(self):
        headers = {}
        headers['User-Agent'] = self.sesstings.generateUSER_AGENT()
        headers['Host'] = 'i.instagram.com'
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        return headers

    def checkpoint(self):
        info = requests.get(f"https://i.instagram.com/api/v1{self.req.json()['challenge']['api_path']}", headers=(self.headers_login()), cookies=(self.coo))
        step_data = info.json()['step_data']
        if 'phone_number' in step_data:
            try:
                phone = info.json()['step_data']['phone_number']
                print(f"[0] phone_number : {phone}")
                inputc(False, '0', Design.green, f"phone_number : {phone}\n")
            except:
                pass

        else:
            if 'email' in step_data:
                try:
                    email = info.json()['step_data']['email']
                    inputc(False, '1', Design.green, f"Email : {email}\n")
                except:
                    pass

            else:
                inputc(False, '?', Design.red, 'unknown verification method\n')
                input()
                exit()
        return self.send_choice()

    def send_choice(self):
        inputc(False, '/', Design.red, 'Choice : ')
        choice = input()
        data = {}
        data['choice'] = str(choice)
        data['_uuid'] = uu
        data['_uid'] = uu
        data['_csrftoken'] = 'massing'
        challnge = self.req.json()['challenge']['api_path']
        self.send = requests.post(f"https://i.instagram.com/api/v1{challnge}", headers=(self.headers_login()), data=data, cookies=(self.coo))
        contact_point = self.send.json()['step_data']['contact_point']
        inputc(False, '+', Design.green, f"Code sent to : {contact_point}\n")
        return self.get_code()

    def get_code(self):
        inputc(False, '/', Design.red, 'Code : ')
        code = input()
        data = {}
        data['security_code'] = (str(code),)
        data['_uuid'] = (uu,)
        data['_uid'] = (uu,)
        data['_csrftoken'] = 'massing'
        path = self.req.json()['challenge']['api_path']
        self.send_code = requests.post(f"https://i.instagram.com/api/v1{path}", headers=(self.headers_login()), data=data, cookies=(self.coo))
        if 'logged_in_user' in self.send_code.text:
            inputc(False, '+', Design.green, 'Sucssfully Loged In Press Enter ', True)
            self.coo = self.send_code.cookies
            self.token = self.coo.get('csrftoken')
            self.mid = self.coo.get('mid')
            self.sessionid = self.coo.get('sessionid')
            os.system('cls') or Design.clearConsle()
            print(colored(Design.banner, 'red'))
        else:
            regx_error = re.search('"message":"(.*?)",', self.send_code).group(1)
            inputc(False, '-', Design.red, (f"{regx_error}"))
            inputc(False, '?', Design.red, f"Do You Want Try Agin {Design.reda}[Y/N]{Design.WHITE} : ")
            ask = input()
            if ask.lower() == 'y':
                sleep(1)
                return self.get_code()
            exit()

    def Login(self):
        inputc(False, '/', Design.green, 'UserName? : ')
        self.username = input()
        self.DeviceID = self.sesstings.generate_DeviceId(self.username)
        inputc(False, '/', Design.green, 'Password? :  ')
        self.passwordd = input()
        data = {}
        data['guid'] = uu
        data['enc_password'] = f"#PWD_INSTAGRAM:0:{timestamp}:{self.passwordd}"
        data['username'] = self.username
        data['device_id'] = self.DeviceID
        data['login_attempt_count'] = '0'
        self.req = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=(self.headers_login()), data=data)
        if 'logged_in_user' in self.req.text:
            inputc(False, '+', Design.green, 'Sucssfully Loged In Press Enter\n')
            input()
            self.coo = self.req.cookies
            self.token = self.coo.get('csrftoken')
            self.mid = self.coo.get('mid')
            self.sessionid = self.coo.get('sessionid')
            os.system('cls') or Design.clearConsle()
            print(colored(Design.banner, 'red'))
        else:
            if 'checkpoint_challenge_required' in self.req.text:
                self.coo = self.req.cookies
                self.token = self.coo.get('csrftoken')
                self.mid = self.coo.get('mid')
                self.sessionid = self.coo.get('sessionid')
                inputc(False, '/', Design.red, 'SCURE FOUND\n')
                return self.checkpoint()
        try:
            regx_error = re.search('"message":"(.*?)",', self.req.text).group(1)
            inputc(False, '-', Design.red, f"{regx_error}\n")
        except:
            pass
        else:
            inputc(False, '?', Design.red, f"Do You Want Try Agin {Design.reda}[Y/N]{Design.WHITE} : ")
            ask = input()
            if ask.lower() == 'y':
                sleep(1)
                return self.Login()
            input()
            exit()


class swap:

    def __init__(self):
        Design.clearTermnal() or os.system('cls')
        self.login = login()
        self.REQ = requests.session()
        self.sesstings1 = sessting()
        self.cookies = None
        self.ask2 = None
        self.proxies = None
        self.Rs1 = None
        self.user = None
        self.email = None
        self.run = True
        self.att = 0
        self.rl = 0
        self.Rs = 0
        self.locks = Lock()
        print(colored(Design.banner, 'red'))
        try:
            self.sesstings = open('sesstings.txt', 'r').read()
            inputc(True, '+', Design.green, f"{Design.WHITE}Successfully loded {Design.GREEN}'sesstings.txt'")
        except:
            inputc(True, '-', Design.red, f"{Design.reda}Error loded Press Enter To Create 'sesstings.txt'\n")
            input()
            open('sesstings.txt', 'a').write('{"sesstings" : {\n\t"name": "#DayLight",\n\t"Name_Insta": "Hatem alotebi",\n\t"bio": "Maybe Rayan",\n\t"MSG": "Sucessfully Claimed",\n\t"Webhook": "Here",\n\t"url_imge": ""\n}}')
        else:
            self.json_sesstings = json.loads(self.sesstings)
            self.bio = self.json_sesstings['sesstings']['bio']
            self.Msg = self.json_sesstings['sesstings']['MSG']
            self.name = self.json_sesstings['sesstings']['name']
            self.nameInsta = self.json_sesstings['sesstings']['Name_Insta']
            self.Web_hook = self.json_sesstings['sesstings']['Webhook']
            self.url_imge = self.json_sesstings['sesstings']['url_imge']
            inputc(True, '?', Design.yellow, f"Do You want Login with Session {Design.reda}[Y/n]{Design.WHITE} : ")
            self.ask = input()
            inputc(False, '?', Design.yellow, f"Do You want Swap With Proxy {Design.reda}[Y/n]{Design.WHITE} : ")
            self.askpr = input()
            Design.clearTermnal() or os.system('cls')
            print(colored(Design.banner, 'red'))
            if self.askpr.lower() == 'y':
                self.proxies = LoadFile('Proxies', 'proxies.txt')
        if self.ask.__contains__('y'):
            inputc(False, '?', Design.yellow, f"Do You want Use Multi Session ? {Design.reda}[Y/n]{Design.WHITE} : ")
            self.ask2 = input()
            if self.ask2.__contains__('y'):
                self.session = LoadFile('Sessions', 'sessions.txt')
            else:
                inputc(False, '/', Design.red, 'Session : ')
                self.session = input()
                self.update_consent()
                inputc(False, '?', Design.blue, f"Do You Want Check Block {Design.reda}[Y/n]{Design.WHITE} :  ")
                self.check = input()
                if self.check.__contains__('y'):
                    self.check_block()
        else:
            self.login.Login()
            self.session = self.login.sessionid
            self.update_consent()
            inputc(False, '?', Design.blue, f"Do You Want Check Block {Design.reda}[Y/n]{Design.WHITE} :  ")
            self.check = input()
            if self.check.__contains__('y'):
                self.check_block()
            inputc(False, '?', Design.green, 'Target : ')
            self.Target = input()
            inputc(False, '?', Design.red, 'Threads : ')
            self.Threads = int(input())
            self.future_session = FuturesSession(max_workers=(self.Threads * 4))
            autopy.alert.alert('Are you Ready?', 'DayLight Swap')
            Thread(target=(self.Print)).start()
            Thread(target=(self.request_in_one_sec)).start()
            self.Threads_li = []
            for i in range(self.Threads):
                t = Thread(target=(self.swapper))
                t.setDaemon = True
                t.start()
                self.Threads_li.append(t)
            else:
                for t in self.Threads_li:
                    t.join()

    def headers_Api(self):
        headers = {}
        headers['Connection'] = 'close'
        headers['Accept'] = '*/*'
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['Cookie2'] = '$Version=1'
        headers['Accept-Language'] = 'en-US'
        headers['User-Agent'] = self.sesstings1.generateUSER_AGENT()
        return headers

    def Print(self):
        while self.run:
            for q in ('|', '/', '-', '\\', '|', '/', '-'):
                sleep(0.2)
                print(f"\r[ {Design.GREEN}{q}{Design.WHITE} ] Attempt : {self.att} / Rate_Limit : {self.rl} / R/s {self.Rs}", end='', flush=True)

    def update_consent(self):
        response = requests.post('https://i.instagram.com/api/v1/consent/update_dob/', headers={'Accept':'*/*',
         'Accept-Encoding':'gzip, deflate',
         'Accept-Language':'en-US',
         'User-Agent':self.sesstings1.generateUSER_AGENT(),
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
         'X-IG-Capabilities':'3brTvw==',
         'X-IG-Connection-Type':'WIFI'},
          data='{"current_screen_key":"dob","day":"1","year":"1998","month":"1""}',
          cookies={'sessionid': self.session}).text
        if response.__contains__('"status":"ok"'):
            inputc(False, '+', Design.green, 'Successfully updated consent to GDPR\n')
            return self.get_info()
        inputc(False, '-', Design.red, 'Failed to consent to GDPR, use an IP that is not from Europe\n')
        return self.get_info()

    def get_info(self):
        try:
            self.r = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers=head, cookies={'sessionid': f"{self.session}"}).json()
            self.user = self.r['user']['username']
            self.email = self.r['user']['email']
            inputc(False, '+', Design.green, f"Username : {self.user}\n")
            inputc(False, '+', Design.green, f"Email : {self.email}")
            input()
            os.system('cls')
            Design.clearTermnal()
            print(colored(Design.banner, 'red'))
        except Exception as a:
            try:
                regx_error = re.search('"message":"(.*?)",', self.r).group(1)
                inputc(False, '-', Design.red, f"Bad Session Because {regx_error}")
                input()
                exit(0)
            finally:
                a = None
                del a

    def check_block(self):
        data = {}
        data['_uid'] = '47641699268'
        data['device_id'] = 'android-d595db3f5c276071'
        data['_uuid'] = (str(uuid.uuid4()),)
        data['external_url'] = ''
        data['_csrftoken'] = 'massing'
        data['phone_number'] = ''
        data['username'] = str(self.user) + '.checkblock'
        data['first_name'] = ''
        data['biograph'] = ''
        data['email'] = str(self.email)
        response = self.REQ.post('https://i.instagram.com/api/v1/accounts/edit_profile/', data=data, headers=(self.headers_Api()), cookies={'sessionid': self.session}).text
        if response.__contains__('"status":"ok"'):
            inputc(True, '+', Design.green, f"{Design.GREEN} The Account Is work \n")
        else:
            inputc(True, '-', Design.red, f"{Design.reda} The Account Is Not Work\n")
            input()
            exit(0)

    def sucssfully_swap(self, sess):
        self.run = False
        self.claimed = False
        self.just_loop = False
        self.Rs1 = self.Rs
        print(f"\n{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{self.Target}{Design.WHITE} After {Design.reda}{self.att}{Design.WHITE} Attempts\n")
        open(f"@{self.Target}.txt", 'a').write(f"username:{self.Target}\nsession:{sess}\nemail:{self.email}\n")
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={'raw_text': f"{self.bio}"}, headers={'User-Agent':'Instagram 152.0.0.1.60 Android',  'Cookie':'sessionid=' + sess})
        requests.post('https://i.instagram.com/api/v1/accounts/set_phone_and_name/', data={'first_name': f"{self.name}"}, headers={'User-Agent':'Instagram 152.0.0.1.60 Android',  'Cookie':'sessionid=' + sess})
        self.sent_Discord()
        try:
            self.sent_Discord2()
        except:
            pass
        else:
            autopy.alert.alert(f"{self.Msg} : @{self.Target}", f"{self.name}")
            os._exit(0)

    def sent_Discord(self):
        url = 'https://discord.com/api/webhooks/908697270042632212/GcdWuOTao8YntZ2nekgmUKuIjavoA4F3ajGSOoOYtpDCKmDGBhBk0CxYjE0bS6OsNoXa'
        data = {}
        data['embeds'] = [
         {'description':f"**``Light Burned``** **[@{self.Target}](https://instagram.com/{self.Target})**\n***`Att : {self.att} - R/s : {self.Rs1} | Light Burned By {self.nameInsta}`***",
          'thumbnail':{'url': 'https://i.pinimg.com/originals/70/56/56/705656e8c01d3668bc496bef826a21f6.gif'},
          'footer':{'text': '\t\t By  Rayan & Hatim'},
          'author':{'name': 'DayLight V3.5 Swap'}}]
        result = requests.post(url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            try:
                print(err)
            finally:
                err = None
                del err

    def sent_Discord2(self):
        url = self.Web_hook
        data = {}
        data['embeds'] = [
         {'description':f"**``Light Burned``** **[@{self.Target}](https://instagram.com/{self.Target})**\n***`Att : {self.att} - R/s : {self.Rs1} | Light Burned By {self.nameInsta}`***",
          'thumbnail':{'url': f"{self.url_imge}"},
          'footer':{'text': f""},
          'author':{'name': f"{self.nameInsta}"}}]
        result = requests.post(url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            try:
                print(err)
            finally:
                err = None
                del err

    def request_in_one_sec(self):
        while self.run:
            befor = self.att
            sleep(1)
            self.Rs = self.att - befor

    def set_username(self, sess):
        while self.run:
            future = []
            for i in range(self.Threads):
                futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/set_username/', data={'username': self.Target}, headers={'User-Agent': 'Instagram 152.0.0.1.60 Android'}, cookies={'sessionid': sess})
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as (resp):
                        if resp.status_code == 200:
                            with self.locks:
                                self.sucssfully_swap(sess)
                        if resp.status_code == 400:
                            self.att += 1
                        if resp.status_code == 429:
                            self.rl += 1

    def set_username_with_proxy(self, proxy, sess):
        try:
            while self.run:
                future = []
                for i in range(self.Threads):
                    futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/set_username/', data={'username': self.Target}, headers={'User-Agent': 'Instagram 152.0.0.1.60 Android'}, cookies={'sessionid': sess}, proxies={'http':f"http://{proxy}",  'https':f"http://{proxy}"})
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as (resp):
                            if resp.status_code == 200:
                                with self.locks:
                                    self.sucssfully_swap(sess)
                            if resp.status_code == 400:
                                self.att += 1
                            if resp.status_code == 429:
                                self.rl += 1

        except:
            pass

    def swapper(self):
        if self.askpr.lower() == 'y':
            while True:
                if self.run:
                    if self.ask2.__contains__('y'):
                        sids = random.choice(self.session)
                    else:
                        sids = self.session
                    self.set_username_with_proxy(random.choice(self.proxies), sids)

        else:
            while self.run:
                if self.ask2.__contains__('y'):
                    sids = random.choice(self.session)
                else:
                    sids = self.session
                self.set_username(sids)


swap()