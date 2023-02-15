from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import fundamentus
import datetime
from tqdm import tqdm
from Model.acao import Acao

'''Esta função busca no fundamentus os detalhes de cada papel listado
Parâmetro: não tem parâmetro de entrada
Saída: entrega um array de objetos da classe Acao'''
def pegar_acoes_fundamentus():
    data = datetime.datetime.now()
    ano = data.year
    list_papel = fundamentus.list_papel_all()
    acoes = []
    for papel in tqdm(list_papel, desc="Extração das Ações"):
        try:
            acao_aux = fundamentus.get_detalhes_papel(f'{papel}')
            dividend = buscar_dividendos_por_ano(papel)
            div_0 = '0'
            div_1 = '0'
            div_2 = '0'
            div_3 = '0'
            div_4 = '0'
            cotacao = float(acao_aux['Cotacao'][0])
            for dividendo in dividend:
                dividendo['valor'] = dividendo['valor'].replace(',','.')
                if dividendo['ano'] == f'{ano}':
                    div_0 = float(dividendo['valor'])
                if dividendo['ano'] == f'{ano-1}':
                    div_1 = float(dividendo['valor'])
                if dividendo['ano'] == f'{ano-2}':
                    div_2 = float(dividendo['valor'])
                if dividendo['ano'] == f'{ano-3}':
                    div_3 = float(dividendo['valor'])
                if dividendo['ano'] == f'{ano-4}':
                    div_4 = float(dividendo['valor'])
            tick = acao_aux['Papel'][0]
            nome = acao_aux['Empresa'][0]   
            acao = Acao(
                ticket=tick, 
                nome_empresa = nome, 
                cotacao = cotacao, 
                dividend_ano_0 = div_0,
                dividend_ano_1 = div_1,
                dividend_ano_2 = div_2,
                dividend_ano_3 = div_3,
                dividend_ano_4 = div_4
                )
            Acao.add_update(acao=acao)
        except:
            resposta = ''
    return acoes





'''Esta função busca no fundamentus os dividendos pagos por ação
Parâmetro: ticket
Return: array de dict do tipo {'ano': '1999', 'valor':'1,25'}'''
def buscar_dividendos_por_ano(papel):

    req = Request(
        url=f'https://www.fundamentus.com.br/proventos.php?papel={papel}&tipo=2',
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html5lib')

    tabela = soup.find("table", id="resultado-anual")
    
    aux = []
    for item in tabela:
        text_aux = item.text
        arr_aux = text_aux.split('\n')
        aux.append(arr_aux)

    n = 1
    while n != 0:
        n = 0
        for item in aux:
            for sub in item:
                if sub == '':
                    n +=1
                    item.remove('')
                if sub == ' ':
                    n +=1
                    item.remove(' ')
                if sub == '  ':
                    n +=1
                    item.remove('  ')

    table = []
    for item in aux:
        if item != []:
            table.append(item)

    dividendo = {
        'ano':'',
        'valor':''
    }
    aux = table[1]


    aux2 = []
    arr_dividendo = []
    n = 0
    while n < len(aux):
        try:
            dividendo['ano'] = aux[n]
            dividendo['valor'] = aux[n+1]
            aux2 = dividendo.copy()
            arr_dividendo.append(aux2)
            n += 2
        except:
            n = len(aux)
            arr_dividendo = ['Error']
    return arr_dividendo
