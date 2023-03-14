#272562015
#MarleyHuskyKim1972!
from playwright.sync_api import Playwright, sync_playwright

import time

def run(playwright: Playwright) -> None:
    
    try:
        pagina_base = 'https://stellar.mlsmatrix.com/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ2MDcwDUAGAwAAAAUGwqJpHg0CCw))&f='
        #Creacion del contexto de la pag web
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # MarHusKim1!
        #entrando a la pagina web
        #wait_until ='networkidle'
        page.goto(pagina_base, wait_until ='networkidle')

        #page.click('#loginId')

        page.get_by_label("MLS ID/NRDS ID Number:").click()
        page.get_by_label("MLS ID/NRDS ID Number:").fill("272562015")
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill("MarleyHuskyKim1972!")
        #page.get_by_role("button", name="Sign In").click()
        #page.fill('#loginId','272562015')
        #page.fill('#password','MarHusKim1!')
        print('lleno los datos')
        page.click('body > div > div > div.row-container > div.auth-container__section')
        
        page.click('#btn-login')
        #page.click('#btn-login') # Opens a new tab
        print('presiono el boton')
        #page.click('#btn-login')



        page.wait_for_load_state('networkidle', timeout=60000)
        page.wait_for_url("https://central.stellarmls.com/pages/home-30", timeout=60000)
        page.goto("https://central.stellarmls.com/pages/home-30", wait_until= 'load')
        print('entro a la pagina')

        page.goto("https://stellar.mlsmatrix.com/Matrix/MyMatrix/MyListings",timeout=60000)
        print('entro directo')
        
        #page.wait_for_load_state('networkidle')
        page.get_by_role("link", name=" Home").click()
        page.wait_for_url("https://central.stellarmls.com/pages/home-30")
        page.get_by_role("link", name=" Products & Services").click()
        page.wait_for_url("https://central.stellarmls.com/pages/products-services-31")
        print('entro a la pagina recursos')
        time.sleep(2)

        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Matrix™ MLS system").click()
        #pagina de los contactos
        page1 = popup_info.value
        print('****')
        page1.locator('#m_ucDisplay_m_pnlDisplay > table > thead > tr > th.Fixed.NoPrint.checkboxTableHeader > span > analyticscontainer > input[type=checkbox]').click()

        '''
        page.wait_for_load_state('networkidle', timeout=60000)
        page.wait_for_url("https://stellar.mlsmatrix.com/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ1MzAyDUAGAwAAAAVzWMOGcw0CCw))&f=", timeout=60000)
        page.goto("https://stellar.mlsmatrix.com/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ1MzAyDUAGAwAAAAVzWMOGcw0CCw))&f=", wait_until='load')
        print('entro a la pagina del pop up')
        #para desaparecer el pop up
        page1.get_by_text("I've Read This").click()
        page1.get_by_text("I've Read This").click()
        page1.get_by_text("I've Read This").click()
        #para desaparecer el pop up'''

        '''page1.get_by_role("link", name="My Listings").click()
        page1.wait_for_url("https://stellar.mlsmatrix.com/Matrix/MyMatrix/MyListings")
        page1.locator(".col-xs-1").click()'''
        # ---------------------
        time.sleep(3)
        context.close()
        browser.close()
        
    except Exception as e:
        print('fallo -> '+str(e))
            
with sync_playwright() as playwright:
    run(playwright)