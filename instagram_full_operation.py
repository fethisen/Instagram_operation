import random
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class InstagramOperation():
    """
    instagrama ait butun fonksiyonların yer aldığı class yapisi
    """

    def open_browser(self, proxy_port=None, refresh_session=True, use_proxy=True):
        """
        seleniumda kullanilacak browsere acan metot.
        :param refresh_session:
        :param use_proxy:
        :return:
        """
        # refresh session - ip change
        # if refresh_session:
        #     proxies = {
        #         "http": "http://127.0.0.1:%s" % proxy_port,
        #         "https": "http://127.0.0.1:%s" % proxy_port,
        #     }
        #
        #     response = requests.get('https://lumtest.com/myip.json', proxies=proxies).json()
        #     old_ip = response.get('ip')
        #     new_ip = old_ip
        #     requests.post("http://127.0.0.1:22999/api/refresh_sessions/" + proxy_port)
        #     time.sleep(3)
        #
        #     i = 0
        #     while old_ip == new_ip:
        #         time.sleep(3)
        #         response = requests.get('https://lumtest.com/myip.json', proxies=proxies).json()
        #         new_ip = response.get('ip')
        #         print('new ip')
        #         print(new_ip)
        #         print(response.get('country'))
        #         print(response.get('geo'))
        #         print(response.get('asn'))
        #
        #         i += 1
        #         if (i > 10):
        #             i = 0
        #             requests.post("http://127.0.0.1:22999/api/refresh_sessions/" + proxy_port)

        # region browser settings
        driver_path = "/home/fethi/PythonProje/chromedriver"
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-popup-blocking")
        # options.add_argument('--headless')

        options.add_argument("no-sandbox")
        options.add_argument(
            '--User-Agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"')

        # if use_proxy:
        #     options.add_argument('--proxy-server=http://127.0.0.1:%s' % proxy_port)

        # ssl hatası
        # options.addArguments("ignore-certificate-errors")
        # browser = webdriver.Chrome(options=options)

        return webdriver.Chrome(
            options=options,
            executable_path=driver_path
        )

    def login(self, account_name, account_pass, browser):
        """
        instagram hesabina giris icin kullanilacak metot.
        :param account_name: kullanici adi bilgisi
        :param account_pass: hesabin sifresi
        :param browser: tarayici nesnesi
        :return:
        """
        browser.get("https://www.instagram.com/")
        time.sleep(2)
        sign_in = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
        sign_in.click()
        time.sleep(4)

        user_name = browser.find_element_by_name("username")
        password = browser.find_element_by_name("password")

        user_name.send_keys(account_name)
        password.send_keys(account_pass)

        login_button = browser.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")

        login_button.click()

        time.sleep(5)

    def sending_request(self, file_name, browser):
        """
        verilen dosya ismini acarak sırasıyla istek yollar: (dosya farklı dizinde ise dosya yoluyla birlikte verilmeli.)
        :param file_name: dosya ismi
        :param browser: tarayici nesnesi
        :return:
        """
        numberList = [4, 6, 20, 10, 15, 5]
        request_limit = 0
        file = open(file_name, "r")
        count = 1
        for line in file:
            url_name = "https://www.instagram.com/{}/".format(line)
            browser.get(url_name)
            time.sleep(random.choice(numberList))
            try:
                followers_button = browser.find_element_by_css_selector(".BY3EC")
                hov = ActionChains(browser).move_to_element(followers_button)
                hov.click().perform()
            except:
                print("{} profiline istek atılamadı ****************************************".format(line))
                continue

            time.sleep(random.choice([45, 40, 55]))
            # time.sleep(45)
            followers_button_text = followers_button.text

            if followers_button_text in ("Follow", "Takip Et"):
                print(
                    " ********************************************* Arkadaşlık istek sınırı dolmuş **********************************",
                    line)
                request_limit += 1
                if request_limit >= 20:
                    browser.close()
                    file.close()
            else:
                print("{} hesabına istek atıldı, toplam istek adedi. {}".format(line, count))
                count += 1

            if count % 60 == 0:
                # time.sleep(1200)
                time.sleep(random.choice([1200, 1204, 1277]))

        file.close()
