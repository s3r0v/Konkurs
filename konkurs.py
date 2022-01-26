'''
Гайд по установке
Установленный python 3.7+(если будет время потом скомпилирую,или скомпилируй ты анонче)
потом в терминал
pip install requests
pip install selenium
pip install webdriver-manager
 
Нихуя не надо, просто запускай. 
 
Вроде прокси не требуются,ну если возникли проблемы с регой - юзай впн
 
По всем вопросам,багам в тред
КТО БУДЕТ ПИСАТЬ СООБЩЕНИЯ ПО ТИПУ - "КОКОКО ГОВНОКОД","ХРЮХРЮХРЮ ПИТОН";Просьба пойти срать на хабр
Удачного вечера анон!
'''

import requests
import string,random,time,re
import warnings
import uuid
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
warnings.filterwarnings("ignore")
 
banner = """
 +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+
 |O|P|E|R|A|T|I|O|N| |B|L|A|C|K| |M|A|M|B|A|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |B|y| |A|n|o|n| |f|o|r| |2|c|h|.|h|k|      
 +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+      
 |V|e|r| |1|.|2|b|                          
 +-+-+-+ +-+-+-+-+   
"""
class Post_shift():
 
    postshift_api_hash = ""
    mail = {"email":"","key":""}
    def __generate_random_string(self,min: int = 12, max: int = 16):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(min, max)))
 
    #не исользуется(защита от дебилов)
    def Regestration(self):
        try:
            resp = requests.get(f"https://post-shift.ru/api.php?action=reg&email={self.__generate_random_string()}@domain.ru")
            if resp.status_code != 200:
                raise Exception
            return True
        except Exception as e:
            print(f"Ошибка при регистрации на postshift!!!\nЛог:{e}")
            return  False
 
    def CreateMail(self):
        try:
            # resp = requests.get(f"https://post-shift.ru/api.php?action=new&hash={self.postshift_api_hash}")
            resp = requests.post(f"https://api.mail.tm/accounts")
            if resp.status_code != 200:
                raise Exception
            resp = resp.json()
            self.mail["email"] = resp["email"]
            self.mail["key"] = resp["key"]
            return True
        except Exception as e:
            print(f"Ошибка при получении ящика!!!\nЛог:{e}")
            return False
 
    def Clear(self):
        try:
            resp = requests.get(f"https://post-shift.ru/api.php?action=deleteall")
            if resp.status_code != 200:
                raise Exception
            return True
        except Exception as e:
            print(f"Ошибка при Удалении ящиков!!!\nЛог:{e}")
            return False
 
    def getEmailMessage(self, token):
        resp = requests.get('https://api.mail.tm/messages', headers={'Authorization': 'Bearer ' + token})
        if resp.status_code != 200:
            raise Exception
        emails = resp.json()['hydra:member']
        if len(emails) != 0:
            id = emails[0]['id']
            resp = requests.get('https://api.mail.tm/messages/' + id, headers={'Authorization': 'Bearer ' + token})
            if resp.status_code != 200:
                raise Exception
            return resp.json()['html'][0]
        return None
 
 
    def GetEmailList(self):
        try:
            resp = requests.get(f"https://post-shift.ru/api.php?action=getlist&hash={self.postshift_api_hash}&key={self.mail['key']}")
            if resp.status_code != 200:
                raise Exception
            return resp.json()
        except Exception as e:
            print(f"Ошибка при Получении списка сообщений!!!\nЛог:{e}")
            return None
 
    def GetEmailText(self):
        try:
            resp = requests.get(f"https://post-shift.ru/api.php?action=getmail&hash={self.postshift_api_hash}&key={self.mail['key']}&id=1")
            if resp.status_code != 200:
                raise Exception
            return resp.json()
        except Exception as e:
            print(f"Ошибка при Получении списка сообщений!!!\nЛог:{e}")
            return None
    def __init__(self,hash):
        self.postshift_api_hash=hash
def ExtractPwd(message):
    match = re.search(r'href=[\'"]?([^\'" >]+)', message)
    if match:
        return match.group(0).replace('href="',"")
    else:
        return None
 
def GenPassword(min: int = 20, max: int = 20):
    pwd = ""
    special_list = ["!","@","#","$","%"]
    pwd += ''.join(random.choice(string.ascii_uppercase) for i in range(5))
    pwd += ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    pwd += ''.join(random.choice(string.digits) for i in range(5))
    pwd += ''.join(random.choice(special_list) for i in range(5))
    return ''.join(random.sample(pwd,len(pwd)))
 
def main():
    itter = 0
    print(banner)
    # apihash = input("Ввдите api ключ от post shift: ")
    apihash = '542524'
    # if len(apihash) != 32:
    #     print("Неверный api hash!")
    #     return 0
    while True:
        try:
            login = uuid.uuid4().hex.replace('-', '-')
            resp = requests.post(f"https://api.mail.tm/accounts", json={"address": login + "@sinaite.net",
                                                                        "password": "2@k6O8iJ"})
            if resp.status_code != 201:
                raise Exception
            email = resp.json()['address']
 
            resp = requests.post(f"https://api.mail.tm/token", json={"address": email,
                                                                     "password": "2@k6O8iJ"})
            if resp.status_code != 200:
                raise Exception
            token = resp.json()['token']
 
            resp = requests.get('https://api.mail.tm/messages', headers={'Authorization': 'Bearer ' + token})
            if resp.status_code != 200:
                raise Exception
 
            a = Post_shift(apihash)
            
            options = webdriver.ChromeOptions()
            options.add_extension('./ub.crx')
            
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.implicitly_wait(5)
            driver.get("https://63.ru/text/education/2022/01/25/70386878/")
            try:
                driver.find_element_by_xpath('//*[@id="onesignal-slidedown-cancel-button"]').click()
            except:
                print()
 
            driver.find_element_by_xpath('//*[@id="app"]/div[2]/header/div[1]/div[2]/a').click()
            driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div/div[2]/div/form/div[3]/button').click()
            a.Clear()
            # a.Regestration()
            a.CreateMail()
            # driver.find_element_by_xpath('//*[@id="register_login"]').send_keys(a.mail['email'])
            driver.find_element_by_xpath('//*[@id="register_login"]').send_keys(email)
            driver.find_element_by_xpath('//*[@id="register_password"]').send_keys(GenPassword())
            driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div/div/div[2]/div/form/button').click()
            print(f"Мыло: {email}")
            while True:
                time.sleep(1)
 
                message = a.getEmailMessage(token)
                if message is not None:
                    break
 
                # respmails = a.GetEmailList()
                # if type(respmails) == list:
                #     if respmails[0]["subject"] == "Регистрация на сайтах Сети городских порталов и Fontanka.ru":
                #         break
                #     else:
                #         print("Ошибка письма!!!")
                #         return 0
                print("Ожидаю письмо")
            driver.get(ExtractPwd(message))
            driver.get("https://63.ru/text/education/2022/01/25/70386878/")
            driver.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[21]/div[2]/div[7]/div[2]/div[2]/div/button').click()
            driver.close()
            itter += 1
            print(f"Успешно!!!Итерация:{itter}")
        except:
            print("shhiiet")
            if driver is not None:
                try:
                    driver.close()
                except:
                    print("sssssshhhhhhhhieeet")
        finally:
            time.sleep(10)
 
if __name__ == '__main__':
 
        main()