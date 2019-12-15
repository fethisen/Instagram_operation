from selenium import webdriver
import time

driver_path = "/home/fethi/PythonProje/chromedriver"

browser = webdriver.Chrome(executable_path=driver_path)

def login(account_name, account_pass):
    """
    Bu fonksiyon hesap bilgileri ile beraber sisteme giriş icin kullanilir.
    """
    browser.get("https://www.instagram.com/")
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

def sending_request(file_name):
    """
    verilen dosya ismini acarak sırasıyla istek yollar: (dosya farklı dizinde ise dosya yoluyla birlikte verilmeli.)
    """
    request_limit = 0
    file = open(file_name, "r")
    count = 1
    for line in file:
        url_name = "https://www.instagram.com/{}/".format(line)
        browser.get(url_name)
        time.sleep(30)
        followers_button = browser.find_element_by_css_selector(".BY3EC")
        followers_button.click()
        time.sleep(30)
        followers_button_text = followers_button.text

        if followers_button_text in ("Follow", "Takip Et"):
            print(" ********************************************* Arkadaşlık istek sınırı dolmuş **********************************",line)
            request_limit += 1
            if request_limit >= 10:
                file.close()
                browser.close()

        print("{} hesabına istek atıldı, toplam istek adedi. {}".format(line,count))
        count += 1

    file.close()

if __name__ == "__main__":
    login("account_name", "account_pass")
    sending_request("dgf")

    browser.close()

