import instagram_full_operation

if __name__ == "__main__":
    ornek_kullanim = instagram_full_operation.InstagramOperation()
    browser = ornek_kullanim.open_browser()
    # limunati ile ornek kullanım bilgileri
    # browser = ornek_kullanim.open_browser("24000",True,True)
    ornek_kullanim.login("hesap_adi", "hesap_sifresi", browser)

    ornek_kullanim.sending_request("kullanicilarin_bulundugu_dosya", browser)

    browser.close()
