import requests
import xmltodict, json
from CorreiosPrecoPrazo.validation import Cep, CdServico, DtCalculo, VlPeso, CdFormato, VlDimensao, \
    VlBool, VlDeclarado, Required
from xml.parsers.expat import ExpatError


class Correios:

    def __init__(self, cod_administrativo='', senha=''):
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '0'}
        self.host = 'http://ws.correios.com.br'
        self.endpoint = {'CalcPrazo': '/calculador/CalcPrecoPrazo.asmx/CalcPrazo',
                         'CalcPrazoData': '/calculador/CalcPrecoPrazo.asmx/CalcPrazoData',
                         'CalcPrazoRestricao': '/calculador/CalcPrecoPrazo.asmx/CalcPrazoRestricao',
                         'CalcPreco': '/calculador/CalcPrecoPrazo.asmx/CalcPreco',
                         'CalcPrecoData': '/calculador/CalcPrecoPrazo.asmx/CalcPrecoData',
                         'CalcPrecoPrazo': '/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazo',
                         'CalcPrecoPrazoData': '/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazoData',
                         'CalcPrecoPrazoRestricao': '/calculador/CalcPrecoPrazo.asmx/CalcPrecoPrazoRestricao',
                         'ListaServicos': '/calculador/CalcPrecoPrazo.asmx/ListaServicos'
                         }


        self.cd_empresa = str(cod_administrativo)
        self.ds_senha = str(senha)

    def get_url(self, method):
        return self.host + self.endpoint.get(method)

    def get_response(self, url, payload):
        self.headers['Content-Length'] = str(len(payload))

        status_code = 0
        i = 0
        while status_code != 200 and i < 10:
            response = requests.post(url, data=payload, headers=self.headers)
            status_code = response.status_code
            i += 1

        if i >= 10 and status_code != 200:
            raise TimeoutError ('Aparentemente o webservice dos Correios está indisponível no momento'
                                'Tente novamente mais tarde.')
        try:
            response = xmltodict.parse(response.text)['cResultado']['Servicos']['cServico']
            return response
        except KeyError:
            response = xmltodict.parse(response.text)['cResultadoServicos']['ServicosCalculo']['cServicosCalculo']
            return response
        except ExpatError:
            raise ExpatError ('Não foi possível parsear o XML de resposta do webservice dos Correios')


    def build_payload(self, input):

        payload = ''
        payload += 'nCdEmpresa=' + self.cd_empresa
        payload += '&sDsSenha=' + self.ds_senha
        if input.get('cd_servico') != None:
            payload += '&nCdServico=' + CdServico(input.get('cd_servico')).value()
        if input.get('cep_origem') != None:
            payload += '&sCepOrigem=' + Cep(input.get('cep_origem')).value()
        if input.get('cep_destino') != None:
            payload += '&sCepDestino=' + Cep(input.get('cep_destino')).value()
        if input.get('vl_peso') != None:
            payload += '&nVlPeso=' + VlPeso(input.get('vl_peso')).value()
        if input.get('cd_formato') != None:
            payload += '&nCdFormato=' + CdFormato(input.get('cd_formato')).value()
        if input.get('vl_comprimento') != None:
            payload += '&nVlComprimento=' + VlDimensao(input.get('vl_comprimento'), 'comprimento').value()
        if input.get('vl_altura') != None:
            payload += '&nVlAltura=' + VlDimensao(input.get('vl_altura'), 'altura').value()
        if input.get('vl_largura') != None:
            payload += '&nVlLargura=' + VlDimensao(input.get('vl_largura'), 'largura').value()
        if input.get('vl_diametro') != None:
            payload += '&nVlDiametro=' + VlDimensao(input.get('vl_diametro'), 'diametro').value()
        if input.get('cd_mao_propria') != None:
            payload += '&sCdMaoPropria=' + VlBool(input.get('cd_mao_propria')).value()
        if input.get('valor_declarado') != None:
            payload += '&nVlValorDeclarado=' + VlDeclarado(input.get('valor_declarado')).value()
        if input.get('cd_aviso_recebimento') != None:
            payload += '&sCdAvisoRecebimento=' + VlBool(input.get('cd_aviso_recebimento')).value()
        if input.get('dt_calculo') != None:
            payload += '&sDtCalculo=' + DtCalculo(input.get('dt_calculo')).value()

        return payload

    def calculate(self, method, input):

        validated_input = Required(method, input).value()
        url = self.get_url(method)
        payload = self.build_payload(validated_input)

        return self.get_response(url, payload)

    def list_services(self):
        url = self.get_url('ListaServicos')
        return self.get_response(url, '')
