import time

#ingreso de las credenciales para el LOGIN
def ingreso(page):
    page.get_by_label("Usuario :").click()
    page.get_by_label("Usuario :").fill("jsanchez")
    page.get_by_label("Clave :").click()
    page.get_by_label("Clave :").fill("logmol2")
    print('lleno los datos')
    page.get_by_role("button", name="Ingresar").click()
    print('presiono el boton')

#ingreso a la seccion de ordenes de compra y registro de los datos
def main(page,articulo,factura,cod_serie,num_serie,destino,cantidad,precio_unitario):
    page.wait_for_url("http://190.187.186.218/Default.aspx")
    page.get_by_role("link", name="Compras").click()
    page.wait_for_url("http://190.187.186.218/Compras/Default.aspx")
    page.get_by_role("link", name="5. Ordenes de Compra").click()
    page.wait_for_url("http://190.187.186.218/Compras/Ordenes_Com.aspx")

    page.locator("input[name=\"ctl00\\$Main\\$ImageButton1\"]").click()
    page.wait_for_url("http://190.187.186.218/Compras/Orden_Com.aspx")
    page.locator("input[name=\"ctl00\\$Main\\$cod_clipro\"]").click()
    page.locator("input[name=\"ctl00\\$Main\\$cod_clipro\"]").fill(factura)#FACTURA
    print('lleno la factura')
    page.locator("#Main_UpdatePanel1").click()
    page.locator("select[name=\"ctl00\\$Main\\$TIPO_DOC_REF\"]").select_option("FC")
    page.locator("input[name=\"ctl00\\$Main\\$ser_doc_ref\"]").click()
    page.locator("input[name=\"ctl00\\$Main\\$ser_doc_ref\"]").fill(cod_serie)# CODIGO SERIE
    page.locator("input[name=\"ctl00\\$Main\\$num_doc_ref\"]").click()
    page.locator("input[name=\"ctl00\\$Main\\$num_doc_ref\"]").fill(num_serie)#NUMERO DE SERIE
    print('lleno el codigo de factura')
    page.locator("select[name=\"ctl00\\$Main\\$ALMACEN\"]").select_option(destino)
    page.get_by_role("button", name="Adicionar Item").click()
    page.locator("input[name=\"ctl00\\$Main\\$descri_articulo\"]").click()
    print('ingresando el producto ',articulo)
    page.keyboard.type(articulo, delay=200)
    #page.locator("input[name=\"ctl00\\$Main\\$descri_articulo\"]").fill(articulo_recortado,timeout=30000)
    #page.locator("input[name=\"ctl00\\$Main\\$descri_articulo\"]").click()
    time.sleep(3)
    page.get_by_text(articulo).click()
    time.sleep(3)
    print('ingresando la cantidad')
    page.locator("input[name=\"ctl00\\$Main\\$cantidad\"]").fill(cantidad)
    page.locator("input[name=\"ctl00\\$Main\\$cantidad\"]").press("Tab")
    print('ingresando el precio unitario')
    page.get_by_role("cell", name="Precio Unitario").click()
    page.locator("input[name=\"ctl00\\$Main\\$valor_uni\"]").click()
    time.sleep(3)
    page.locator("input[name=\"ctl00\\$Main\\$valor_uni\"]").fill(precio_unitario)
    time.sleep(3)
    page.locator("input[name=\"ctl00\\$Main\\$valor_uni\"]").press("Tab")
    page.get_by_role("button", name="ACEPTAR").click()
    print('se añadio el producto ',articulo)
    time.sleep(3)
    page.locator("input[name=\"ctl00\\$Main\\$descri_articulo\"]").click()
    page.locator('#Main_btnCerrar').click()
    #page.get_by_role("button", name="SALIR").click()
    print('saliendo ... ')

    time.sleep(3)

