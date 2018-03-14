####################################################################
## Autora: Ana Carolina Pedrosa Monteiro
## Última modificação: 13/03/18
## Sabor: toffu
###################################################################


## bibliotecas
import pandas as pd
import numpy as np
import geopy as gpy
import xlrd
import xlsxwriter

default_endereco=[  'endtrat', 'numEndTrat', 'compltrat','baitrat', 'municTra', 'esttrat', 'ceptrat']
default_endereco=''
# colocar o nome da tabela em excel
def get_dataframe(filename):
    '''
    converte um arquivo (csv, ou excel) para o formato excel 
    e retorna um dataframe 
    '''
    excel = pd.ExcelFile(filename)
    return pd.read_excel(excel)

def get_geoinformation(df,key=default_key,vetor_endereco=default_endereco):
    """
    retorna o dataframe df atualizado com as coordenadas atualizadas
    com as latitudes 'lat' e longitudes 'lon'

    a chave 'key' é chave da API do google

    vetor endereço deve conter os elementos para formar o
    endereço: 
    por exemplo: rua, num, complemento, bairro, cidade, estado
    
    Entradas:
    df = seu dataframe
    key = sua chave da API do googlemaps
    
    vetor_endereco = cada entrada corresponde ao nome da coluna, por
    exemplo: vetor_endereco ['rua','num','bairro',etc... ]
    """
    gcode    = gpy.geocoders.GoogleV3(api_key=key)
    enderecos= get_endereco_from_dataframe(df,vetor_endereco)
    lat=[]
    lon=[]
    for endereco in enderecos:
        # TODO: colocar try e catch
        local = gcode.geocode(endereco,timeout=10) or None 
        if local is not None:
            print(local)
            lat.append(local.latitude)
            lon.append(local.longitude)
        else:
            lat.append('')
            lon.append('')
    df_novo = pd.DataFrame(df)
    df_novo['lat']=lat
    df_novo['lon']=lon
    return df_novo


# vetor endereço, se o usuário não passar o vetor, ele entra o padrão    
def get_endereco(linha,vetor_endereco=default_endereco):
    '''
    cria uma string contendo o endereco de acordo com vetor_endereco
    com os dados da linha 'linha' do dataframe
    
    vetor endereço ele deve conter os elementos para formar o
    endereço: 
    por exemplo: rua, num, complemento, bairro, cidade, estado

    '''
    endereco=''
    for entrada in vetor_endereco:
        if entrada in linha:
            string = str(linha[entrada]) or ''
            string = string.strip()
            if string.find('nan') < 0:
                endereco+=string+', '
    return endereco

def get_endereco_from_dataframe(df,vetor_endereco=default_endereco):
    '''
    retorna uma lista de enderecos a partir de um dataframe df
    de acordo com a especificao em vetor_enderecos
    '''
    endereco=[]
    for entrada in range(len(df)):
        linha = df.loc[entrada]
        endereco.append( get_endereco(linha,vetor_endereco) or '')
    #novo_dataframe = pd.DataFrame(df)
    #novo_dataframe['endereco'] = endereco
    #return novo_dataframe
    return endereco

def modify_dataframe(df,vetor_endereco=default_endereco):
    '''
    retorna uma lista de enderecos a partir de um dataframe df
    de acordo com a especificao em vetor_enderecos
    '''
    endereco=[]
    for entrada in range(len(df)):
        linha = df.loc[entrada]
        endereco.append( get_endereco(linha,vetor_endereco) or '')
    novo_dataframe = pd.DataFrame(df)
    novo_dataframe['endereco'] = endereco
    return novo_dataframe

def save_dataframe_to_excel(df):
    """
    salva o dataframe em formato excel no diretório atual
    """
    writer = pd.ExcelWriter('endereco_geoprocessado.xlsx')
    df.to_excel(writer)
    writer.save()




# def get_geoinformation(df,key=default_key,vetor_endereco=default_endereco):
#     gcode    = gpy.geocoders.GoogleV3(api_key=key)
#     enderecos= get_endereco_from_dataframe(df,vetor_endereco)
#     lat=[]
#     lon=[]
#     for endereco in enderecos:
#         # TODO: colocar try e catch
#         local = gcode.geocode(endereco,timeout=10) or None 
#         if local is not None:
#             lat.append(local.latitude)
#             lon.append(local.longitude)
#         else:
#             lat.append('')
#             lon.append('')
#     df_novo = pd.DataFrame(df)
#     df_novo['lat']=lat
#     df_novo['lon']=lon
#     return df_novo
