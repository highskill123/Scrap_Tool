import tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from tkinter import Canvas
from tkinter import *
from tkinter.ttk import *
from bs4 import BeautifulSoup as bs
import requests
import os
from multiprocessing.pool import ThreadPool
import _thread
import pandas as pd


def driver1():
    options = Options()
    # options.add_argument("--start-fullscreen")
    options.add_argument('--window-size=1920,1080')
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--enable-javascript")
    return webdriver.Chrome(chrome_options=options)
driver = driver1()
years_for_search = []
listofauctions=[]
selflotn=[]
class Scrapper:
    def __init__(self,pas,year=None):
        self.pas=pas
        self.year=year
        #self.lot_name=lot_name

    def mkdir(self):
        global path
        path = 'pics'
        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)
    def scrap(self):
        self.mkdir()
        global cards
        cards = []
        first_row = driver.find_element_by_xpath('//*[@id="carlist"]').find_element_by_xpath('//*[@id="row1"]').find_element_by_xpath('//*[@id="row1"]/td[2]')
        driver.execute_script("arguments[0].click();", first_row)
        print('CALCULATING RESULTS')
        pagenum = '1'
        try:
            pagenum = str(driver.find_element_by_xpath('//*[@id="detail-pager"]/div/div[2]/div[3]').text).strip('')
        except:
            pass
        counter = []
        count = 0
        while count < int(pagenum[2:]):
            count = count + 1
            counter.append(count)
        print('PAGES TO SCRAP ' + str(count))
        ######################################################
        for number in counter:
            AUCTION_NUM = ''
            LOT_NUM = ''
            YEAR = ''
            MODEL_NAME = ''
            GRADE = ''
            MODEL = ''
            CC = ''
            REGISTRATION_TIME = ''
            KM = ''
            COLOR = ''
            TRANSMISSION = ''
            CONDITIONER = ''
            AUDION_GRADE = ''
            EXTERIOR_GRADE = ''
            INTERIOR_GRADE = ''
            START_PRICE = ''
            LOT_STATUS = ''
            AUCTION_DATE = ''
            AUCTION_TIME = ''
            FINAL_PRICE = ''
            VIN = ''
            EQUIPMENT = ''
            PIC = ''
            PIC2 = ''
            PIC3 = ''
            PIC4 = ''
            PICLINK=''
            PIC2LINK=''
            PIC3LINK=''
            PIC4LINK=''
            try:
                AUCTION_NUM = driver.find_element_by_xpath('//h4[contains(text(),"Number of Times Held")]//following::p').text
            except:
                pass
            try:
                LOT_NUM = driver.find_element_by_xpath('//h4[contains(text(),"Lot No.")]//following::p').text
            except:
                pass
            try:
                YEAR = driver.find_element_by_xpath('//h4[contains(text(),"Year")]//following::p').text
            except:
                pass
            try:
                MODEL_NAME = driver.find_element_by_xpath('//div[@id="detail-name"]/p[1]').get_attribute('innerHTML').strip('<p>&nbsp;')
            except:
                pass
            try:
                GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Grade")]//following::p').text
            except:
                pass
            try:
                MODEL = driver.find_element_by_xpath('//*[@id="detail-name"]/p[2]').get_attribute('innerHTML').strip('<p>&nbsp;')
            except:
                pass
            try:
                CC = driver.find_element_by_xpath('//p[contains(text(),"cc")]').text
            except:
                pass
            try:
                REGISTRATION_TIME = driver.find_element_by_xpath('//h4[contains(text(),"Holding Date")]//following::p').text
            except:
                pass
            try:
                KM = driver.find_element_by_xpath('//p[contains(text(),"km")]').text
            except:
                pass
            try:
                COLOR = driver.find_element_by_xpath('//h4[contains(text(),"Color")]//following::p').text
            except:
                pass
            try:
                TRANSMISSION = driver.find_element_by_xpath('//h4[contains(text(),"Transmission")]//following::p').text
            except:
                pass
            try:
                CONDITIONER = driver.find_element_by_xpath('//h4[contains(text(),"A/C")]//following::p').text
            except:
                pass
            try:
                AUDION_GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Score")]//following::p').text
            except:
                pass
            try:
                EXTERIOR_GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Exterior")]//following::p').text
            except:
                pass
            try:
                INTERIOR_GRADE = driver.find_element_by_xpath('//h4[contains(text(),"Interior")]//following::p').text
            except:
                pass
            try:
                START_PRICE = driver.find_element_by_xpath('//h4[contains(text(),"Start Price")]//following::p').text
            except:
                pass
            try:
                AUCTION_DATE = driver.find_element_by_xpath('//h4[contains(text(),"Bidding Deadline")]//following::p').text
            except:
                pass
            try:
                AUCTION_TIME = driver.find_element_by_xpath('//h4[contains(text(),"Schedule Time")]//following::p').text
            except:
                pass
            try:
                FINAL_PRICE = driver.find_element_by_xpath('//h4[contains(text(),"Result")]//following::p').text
            except:
                pass
            try:
                EQUIPMENT = driver.find_element_by_xpath('//h4[contains(text(),"Equipment")]//following::p').text
            except:
                pass
            try:
                picsource = driver.find_element_by_xpath('//*[@id="detail-imgs"]').get_attribute('innerHTML')
                PIC = bs(picsource, "html.parser").findAll('img')[0]['src']
                PICNAME=PIC.split('/')[-1].split('.')[0]
                PICLINK='www.globalautonet.co.jp/auctiondata/AsnetImg/'+PICNAME
                PIC2 = bs(picsource, "html.parser").findAll('img')[1]['src']
                PIC2NAME=PIC2.split('/')[-1].split('.')[0]
                PIC2LINK='www.globalautonet.co.jp/auctiondata/AsnetImg/'+PIC2NAME
                PIC3 = bs(picsource, "html.parser").findAll('img')[2]['src']
                PIC3NAME=PIC3.split('/')[-1].split('.')[0]
                PIC3LINK='www.globalautonet.co.jp/auctiondata/AsnetImg/'+PIC3NAME
                PIC4 = bs(picsource, "html.parser").findAll('img')[3]['src']
                PIC4NAME=PIC.split('/')[-1].split('.')[0]
                PIC4LINK='www.globalautonet.co.jp/auctiondata/AsnetImg/'+PIC4NAME
                PICS = [PIC, PIC2, PIC3, PIC4]
                for pic in PICS:
                    img = requests.get(pic)
                    with open(path + "/" + pic.split('/')[-1].split('.')[0] + '.jpg', 'wb') as f:
                        f.write(img.content)
            except:
                pass

                # VIN=
                # LOT_STATUS=
            card = {
                'AUCTION_NUM': AUCTION_NUM,
                'LOT_NUM': LOT_NUM,
                'YEAR': YEAR,
                'MODEL_NAME': MODEL_NAME,
                'GRADE': GRADE,
                'MODEL': MODEL,
                'CC': CC,
                'REGISTRATION_TIME': REGISTRATION_TIME,
                'KM': KM,
                'COLOR': COLOR,
                'TRANSMISSION': TRANSMISSION,
                'CONDITIONER': CONDITIONER,
                'AUDION_GRADE': AUDION_GRADE,
                'EXTERIOR_GRADE': EXTERIOR_GRADE,
                'INTERIOR_GRADE': INTERIOR_GRADE,
                'START_PRICE': START_PRICE,
                'LOT_STATUS': LOT_STATUS,
                'AUCTION_DATE': AUCTION_DATE,
                'AUCTION_TIME': AUCTION_TIME,
                'FINAL_PRICE': FINAL_PRICE,
                'VIN': VIN,
                'EQUIPMENT': EQUIPMENT,
                'PIC1':PICLINK,
                'PIC2':PIC2LINK,
                'PIC3':PIC3LINK,
                'PIC4':PIC4LINK
            }
            print(card)
            cards.append(card)
            try:
                next_btn = driver.find_element_by_xpath('//*[@id="btn-next"]')
                driver.execute_script("arguments[0].click();", next_btn)
            except:
                pass
            time.sleep(2)

    def yearfunc(self):
        y_split = str(self.year).split(',')
        year1 = int(y_split[0])
        year2 = int(y_split[1])
        end = year1
        years_for_search.append(end)
        while end < year2:
            end = end + 1
            years_for_search.append(end)
        select_year=driver.find_element_by_xpath('//*[@id="carlist_head"]/tbody/tr[2]/th[2]/a')
        driver.execute_script("arguments[0].click();", select_year)
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="narrow_iframe"]'))
        for year in years_for_search:
            try:
                selected_year = driver.find_element_by_xpath('//*[@id="filter_content"]').find_element_by_xpath("//label/div[contains(text(),'" + str(year) + "')]")
                driver.execute_script("arguments[0].click();", selected_year)
            except:
                print('NO YEAR ' + str(year))
        driver.switch_to.parent_frame()
        driver.find_element_by_xpath('//*[@id="narrow_button"]').click()
        print('SELECTED YEARS ARE'+str(years_for_search))
        time.sleep(5)
    def login(self):
        #driver.execute_script("document.body.style.zoom='60%'")
        page_url = 'https://www.iauc.co.jp/service/login'
        driver.get(page_url)
        print('LOGING IN')
        login_btn = driver.find_element_by_xpath('//a[contains(@class , "login-btn")]')
        driver.execute_script("arguments[0].click();", login_btn)
        driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/div/input').send_keys('W710679')
        driver.find_element_by_xpath('//*[@id="form_login"]/div[2]/div/input').send_keys(self.pas)
        driver.find_element_by_xpath('//*[@id="login_button"]').click()
        driver.find_element_by_xpath('//*[@id="toggle_lang"]').click()
    def logout(self):
        print('LOGOUT')
        logout=driver.find_element_by_xpath('//*[@id="logout"]')
        driver.execute_script("arguments[0].click();", logout)
        driver.close()
    def getauc(self):
        self.login()
        print('SCRAPING AUCTIONS')
        allaucs=[]
        today=driver.find_elements_by_xpath('//div[@id="vehicle_day"]/div[1]/div[2]/div/*[@class="day-site-box"]/label')
        for item in today:
            title=item.get_attribute('title')
            allaucs.append(title)
        tomorrow=driver.find_elements_by_xpath('//div[@id="vehicle_day"]/div[2]/div[2]/div/*[@class="day-site-box"]/label')
        for item in tomorrow:
            title=item.get_attribute('title')
            allaucs.append(title)
        dafter=driver.find_elements_by_xpath('//div[@id="vehicle_day"]/div[3]/div[2]/div/*[@class="day-site-box"]/label')
        for item in dafter:
            title=item.get_attribute('title')
            allaucs.append(title)
        return allaucs
    def carfilters(self):
        print('SELECTING LOT')
        element1 = driver.find_element_by_xpath('//*[@id="button_number_search"]')
        driver.execute_script("arguments[0].click();", element1)
        driver.find_element_by_xpath('//*[@id="exhibitNumFrom"]').send_keys(selflotn[0])
        driver.find_element_by_xpath('//*[@id="exhibitNumTo"]').send_keys(selflotn[1])
        driver.find_element_by_xpath('//*[@id="exhibit_search"]/exhibit/div[3]/button').click()
    def setauc(self):
        driver.find_element_by_xpath('//*[@id="btn_vehicle_day_clear"]').click()
        for auc in listofauctions:
            print('SELECTING '+auc)
            try:
                driver.find_element_by_xpath('//div[@id="vehicle_day"]/div[1]/div[2]/div/*[@class="day-site-box"]/label[@title="'+auc+'"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//div[@id="vehicle_day"]/div[2]/div[2]/div/*[@class="day-site-box"]/label[@title="'+auc+'"]').click()
            except:
                pass
            try:
                driver.find_element_by_xpath('//div[@id="vehicle_day"]/div[3]/div[2]/div/*[@class="day-site-box"]/label[@title="'+auc+'"]').click()
            except:
                pass
        driver.find_element_by_xpath('//button[contains(@class, "page-next-button")]').click()
        self.carfilters()
        self.yearfunc()
        self.scrap()
        self.logout()
        return cards


class GUI:
    def __init__(self):
        pass
    @staticmethod
    def StartGUI():
        def BUTTON(name):
            if name not in listofauctions:
                listofauctions.append(name)

            v.set(str(listofauctions).strip("[]").replace(",", '\n'))

            print(listofauctions)
        def processauc():
            threadp = ThreadPool(processes=1)
            progres.start()
            entery=Scrapper(ent.get(),)
            res = threadp.apply_async(Scrapper.getauc, (entery,))
            return_val = res.get()
            def addcheck():
                global canvas
                canvas = Canvas(window)
                scroll_y = Scrollbar(window, orient="vertical", command=canvas.yview)
                global frame
                frame = Frame(canvas)
                for item in return_val:
                    #Checkbutton(frame, text=item,variable=self.var,onvalue=(lambda x=item:x),offvalue="")
                    Button(frame, text=item,command=(lambda x=item:BUTTON(x))).pack(side=TOP, fill=BOTH)
                canvas.create_window(0, 0, anchor='nw', window=frame)
                canvas.update_idletasks()
                canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll_y.set)
                canvas.pack(fill='both', expand=True, side='left')
                scroll_y.pack(fill='y', side='right')
                btngetauc.destroy()
                ent2.pack(side=TOP, fill=BOTH)
                ent2.insert(0, "Year")
                entlot.pack(side=TOP, fill=BOTH)
                entlot.insert(0,"LOT")
                btn.pack(side=TOP,fill=BOTH)
                lable.pack(side=TOP,fill=BOTH)
            addcheck()
            progres.stop()
        def Launchauc():
            _thread.start_new_thread(processauc, ())
        def processaucselect():
            threadp = ThreadPool(processes=1)
            label.pack(side=TOP, fill=BOTH)
            progres.start()
            entery = Scrapper(ent.get(),year=ent2.get())
            res = threadp.apply_async(Scrapper.setauc, (entery,))
            canvas.destroy()
            lable.destroy()
            return_val = res.get()
            df = pd.DataFrame(return_val)
            global df_forexpor
            df_forexpor = df
            export()
            progres.stop()
        def LaunchScrap():
            stingentery=str(entlot.get()).split(',')
            startlot=stingentery[0]
            endlot=stingentery[1]
            selflotn.append(startlot)
            selflotn.append(endlot)
            print(selflotn)
            _thread.start_new_thread(processaucselect, ())
        def export():
            df_forexpor.to_csv(ent2.get() + '.csv')
        window = Tk()
        window.title('Scrap')
        window.resizable(height=None, width=None)
        v = StringVar()
        entlot=Entry(window,width=10)
        ent = Entry(window, width=10)
        ent.pack(side=TOP, fill=BOTH)
        ent.insert(0, "Password")
        label=Label(window, text="PLEASE WAIT WHEN THE SCRIPT IS DONE WILL EXPORT THE CSV")

        btn = Button(window, text="Start", command=LaunchScrap)
        ent2 = Entry(window, width=10)
        lable = Message(window, textvariable=v)


        btngetauc = Button(window, text="Get Auctions", command=Launchauc)
        btngetauc.pack(side=TOP, fill=BOTH)

        progres = Progressbar(window, orient='horizontal', length=10)
        progres.pack(side=TOP, fill=BOTH)
        window.mainloop()

GUI.StartGUI()

#Scrapper.setauc(Scrapper('alexy1919'))