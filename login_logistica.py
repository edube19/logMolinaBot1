from playwright.sync_api import Playwright, sync_playwright

from recursos import *
import time

def run(playwright: Playwright) -> None:
    
    try:
        #datos
        articulo = 'QUESO EDAM'
        factura = '20601452651'
        cod_serie = 'E001'
        num_serie = '12654'
        destino = '102' #almacen cocina
        cantidad = '5'#tiene q ser string
        precio_unitario = '45' #tiene que ser string

        pagina_base = 'http://190.187.186.218/index.aspx'
        #Creacion del contexto de la pag web
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        #entrando a la pagina web
        #wait_until ='networkidle'
        page.goto(pagina_base, wait_until ='networkidle')

        #page.click('#loginId')
        ingreso(page)
        main(page,articulo,factura,cod_serie,num_serie,destino,cantidad,precio_unitario)
        
        context.close()
        browser.close()

    except Exception as e:
        print('fallo -> '+str(e))
            
with sync_playwright() as playwright:
    run(playwright)