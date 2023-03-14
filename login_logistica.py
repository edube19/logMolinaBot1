from playwright.sync_api import Playwright, sync_playwright

from recursos import *

def run(playwright: Playwright) -> None:
    
    try:
        filename = 'datos.xlsx'
        #datos
        #articulo = 'QUESO EDAM'
        factura = '20601452651'
        cod_serie = 'E001'
        num_serie = '12654'
        destino = '102'
        #cantidad = '5'
        #precio_unitario = '45.50' 
        lista_productos = extraer_datos(filename)
        long_lista_productos = len(lista_productos)
        print('cantidad de items ',str(long_lista_productos))

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
        '''for producto in lista_productos:
            articulo = producto['producto']
            cantidad = producto['cantidad']
            precio_unitario = producto['precio_unitario']
            main(page,articulo,factura,cod_serie,num_serie,destino,cantidad,precio_unitario)'''
        main(page,lista_productos,long_lista_productos,factura,cod_serie,num_serie,destino)
        context.close()
        browser.close()

    except Exception as e:
        print('fallo -> '+str(e))
            
with sync_playwright() as playwright:
    run(playwright)