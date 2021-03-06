"""
OscarGonzalez1987/interface_Tk is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license 
notices must be preserved. Contributors provide an express grant of patent rights.
"""

from tkinter import *
import librerias.traduccion as trd
import librerias.interface as lbr
import librerias.EtiquetasTexto as lbtex
import librerias.general as lbgen

#---------------------------------------------------------
# fase 3
#---------------------------------------------------------  
def marco_3(raiz, color_marco, ancho_marco, alto_marco, tam_borde, estilo_borde, tipo_cursor, redimencionamiento, sentido):
    sentido = trd.traduccion(redimencionamiento, sentido)
    
    miframe = Frame(raiz, width = 500, height = 100)
    lbgen.paquetado(miframe)
    constructor(miframe)

def etiqueta_texto(miframe):
    modo = "paquete"
    # modo = "ubicacion"
    # modo = "formato"
    milabel_x = 10  # modo   "formato"   "ubicacion"
    milabel_y = 10  # modo   "formato"   "ubicacion"
    texto = "hola"  # modo   "formato"   "ubicacion"
    color = "red"   # modo   "formato"
    tam = 30        # modo   "formato"
    tipo_letra = "Comic Sans MS" # admite valor vacio "", "Comic Sans MS"
    lbtex.etiquetas_modo(miframe, modo, milabel_x, milabel_y, texto, color, tam, tipo_letra)

def etiqueta_texto2(miframe):
    # modo = "paquete"
    modo = "ubicacion"
    # modo = "formato"
    milabel_x = 10  # modo   "formato"   "ubicacion"
    milabel_y = 30  # modo   "formato"   "ubicacion"
    texto = "hola"  # modo   "formato"   "ubicacion"
    color = "red"   # modo   "formato"
    tam = 30        # modo   "formato"
    tipo_letra = "Comic Sans MS" # admite valor vacio "", "Comic Sans MS"
    lbtex.etiquetas_modo(miframe, modo, milabel_x, milabel_y, texto, color, tam, tipo_letra)

def etiqueta_texto3(miframe):
    # modo = "paquete"
    # modo = "ubicacion"
    modo = "formato"
    milabel_x = 10  # modo   "formato"   "ubicacion"
    milabel_y = 50  # modo   "formato"   "ubicacion"
    texto = "hola"  # modo   "formato"   "ubicacion"
    color = "red"   # modo   "formato"
    tam = 30        # modo   "formato"
    tipo_letra = "Comic Sans MS" # admite valor vacio "", "Comic Sans MS"
    lbtex.etiquetas_modo(miframe, modo, milabel_x, milabel_y, texto, color, tam, tipo_letra)

def constructor(miframe):
    # etiqueta_texto(miframe)
    etiqueta_texto2(miframe)
    etiqueta_texto3(miframe)
  
  
  
  
  
#---------------------------------------------------------
# # fase 2
#---------------------------------------------------------
def marco(color_marco, ancho_marco, alto_marco, tam_borde, estilo_borde, tipo_cursor, redimencionamiento, sentido):
    sentido = trd.traduccion(redimencionamiento, sentido)
    marco = Frame()
    
    # funciones compartidas entre la raiz y los marcos (Frame) # fase 2
    lbr.color_fondo(marco, color_marco)
    lbr.borde_tam(marco, tam_borde)
    lbr.borde_estilo(marco, estilo_borde)
    lbr.cursor_tipo(marco, tipo_cursor)    
    
    # funciones exclusivas para marcos
    marco_ancho_alto(marco, ancho_marco, alto_marco)
    if (redimencionamiento == "alineacion"):
        alineacion(marco, sentido)
    elif (redimencionamiento == "expansion"):
        expansion(marco, sentido)
    elif (redimencionamiento == "orientacion"):
        orientacion(marco, sentido)

#---------------------------------------------------------
# funciones exclusivas para marcos                        # fase 2
#---------------------------------------------------------
def marco_ancho_alto(raiz, ancho_marco, alto_marco): # solo para marcos (Frame)
    raiz.config(width = ancho_marco, height = alto_marco)

def alineacion(marco, sentido):
    marco.pack(side = sentido)
    
def orientacion(marco, sentido):
    marco.pack(side = sentido[0], anchor = sentido[1])
    
def expansion(marco, sentido):
    if(sentido == "x"):
        marco.pack(fill = sentido)
    elif(sentido == "y" or sentido == "both"):
        marco.pack(fill = sentido, expand = True)
    else:
        marco.pack()
