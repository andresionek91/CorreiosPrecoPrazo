from datetime import datetime

class Cep:

    def __init__(self, cep):
        self.cep = str(cep).replace('-','').replace(' ','')
        self.is_valid()

    def is_valid(self):
        if len(self.cep) != 8:
            raise ValueError('CEP {} possui {} dígitos. Favor informar um CEP válido.'.format(self.cep, len(self.cep)))
        if not self.cep.isdigit():
            raise ValueError('O CEP {} contém caracteres inválidos. Use somente números.'.format(self.cep))

    def value(self):
        return self.cep

class CdServico:

    def __init__(self, cd_servico):
        self.cd_servico = str(cd_servico)
        self.is_valid()

    def is_valid(self):
        if not self.cd_servico.isdigit():
            raise ValueError('O código de serviço {} contém caracteres inválidos. '
                             'Use somente números.'.format(self.cd_servico))

    def value(self):
        return self.cd_servico


class DtCalculo:

    def __init__(self, dt_calculo):
        self.dt_calculo = str(dt_calculo)
        self.is_valid()
        try:
            self.dt_calculo = datetime.strptime(self.dt_calculo, '%Y-%m-%d')
        except ValueError:
            raise ValueError('A data de cálculo deve estar no formato YYYY-MM-DD.')
        self.dt_calculo = datetime.strftime(self.dt_calculo, '%d/%m/%Y')


    def is_valid(self):
        if len(self.dt_calculo) != 10:
            raise ValueError('A data de cálculo deve estar no formato YYYY-MM-DD.')

    def value(self):
        return self.dt_calculo



class VlPeso:

    def __init__(self, peso):
        try:
            self.vl_peso = float(peso)
        except ValueError:
            raise ValueError('Erro com o peso {} do pacote. '
                             'Favor informar o peso em gramas.'.format(peso))
        if self.vl_peso % 1 != 0:
            raise ValueError('O peso {} do pacote deve inteiro e em gramas.'.format(peso))
        else:
            self.vl_peso = int(self.vl_peso)

    def value(self):
        return str(self.vl_peso/1000.0)


class CdFormato:

    def __init__(self, formato):

        if formato in ['caixa', 'pacote', 1, '1']:
            self.cd_formato = 1
        elif formato in ['rolo', 'prisma', 2, '2']:
            self.cd_formato = 2
        elif formato in ['envelope', 3, '3']:
            self.cd_formato = 3
        else:
            raise ValueError('Favor informar um formato válido. '
                             'Consulte a documentação para ver os formatos aceitos.')

    def value(self):
        return str(self.cd_formato)


class VlDimensao:

    def __init__(self, dimensao):
        try:
            self.vl_dimensao = float(dimensao)
        except ValueError:
            raise ValueError('Erro com a dimensão {} do pacote. '
                             'Favor informar as dimensões em centímetros.'.format(dimensao))
        if self.vl_dimensao % 1 != 0:
            raise ValueError('A dimensão {} do pacote deve ser inteira e em centímetros.'.format(dimensao))
        else:
            self.vl_dimensao = int(self.vl_dimensao)

    def value(self):
        return str(self.vl_dimensao)


class VlBool:

    def __init__(self, bool):
        if bool in ['SIM', 'S', 'sim', 'Sim', 's']:
            bool = True
        elif bool in ['NAO', 'N', 'nao', 'Nao', 'n', 'Não', 'NÃO']:
            bool = False

        if type(bool) != type(True):
            raise TypeError('Mão própria e aviso de recebimento devem ser Booleanos.')
        elif bool:
            self.vl_bool = 'S'
        else:
            self.vl_bool = 'N'

    def value(self):
        return str(self.vl_bool)


class VlDeclarado:

    def __init__(self, valor_declarado):
        try:
            self.vl_valor_declarado = float(valor_declarado)
        except ValueError:
            raise ValueError('O valor declarado deve ser inteiro ou decimal e em reais.')


    def value(self):
        return str(self.vl_valor_declarado)


class Required:

    def __init__(self, method, input):
        self.method = method
        self.input = input
        self.validate()

    def validate(self):
        if self.method == 'CalcPrazo':
            reqs = {'cd_servico', 'cep_origem', 'cep_destino'}
            if not reqs <= self.input.keys():
                raise AttributeError ('Os atributos {} são obrigatórios no método {}.'.format(reqs, self.method))

        elif self.method == 'CalcPrazoData':
            reqs = {'cd_servico', 'cep_origem', 'cep_destino', 'dt_calculo'}
            if not reqs <= self.input.keys():
                raise AttributeError ('Os atributos {} são obrigatórios no método {}.'.format(reqs, self.method))

        elif self.method == 'CalcPrazoRestricao':
            reqs = {'cd_servico', 'cep_origem', 'cep_destino', 'dt_calculo'}
            if not reqs <= self.input.keys():
                raise AttributeError ('Os atributos {} são obrigatórios no método {}.'.format(reqs, self.method))

        elif self.method in ['CalcPreco', 'CalcPrecoData', 'CalcPrecoPrazo',
                             'CalcPrecoPrazoData', 'CalcPrecoPrazoRestricao']:
            reqs = self.reqs_formato()
            if not reqs <= self.input.keys():
                raise AttributeError('Os atributos {} são obrigatórios no método {} '
                                     'para o cd_formato {}.'.format(reqs,
                                                                 self.method,
                                                                 self.input.get('cd_formato')))


        else:
            raise ValueError('O método {} não está disponível.'.format(self.method))


    def reqs_formato(self):
        formato = CdFormato(self.input.get('cd_formato')).value()

        if formato == '1':
            reqs = {'cd_servico', 'cep_origem', 'cep_destino', 'vl_peso', 'cd_formato',
                    'vl_comprimento', 'vl_largura', 'vl_altura'}
        elif formato == '2':
            reqs = {'cd_servico', 'cep_origem', 'cep_destino', 'vl_peso', 'cd_formato',
                    'vl_diametro'}
        elif formato == '3':
            reqs = {'cd_servico', 'cep_origem', 'cep_destino', 'vl_peso', 'cd_formato',
                    'vl_comprimento', 'vl_largura'}
        else:
            raise AttributeError('O atributo cd_formato é obrigatório para o método {}'.format(self.method))

        if self.method in ['CalcPrecoData', 'CalcPrecoPrazoData', 'CalcPrecoPrazoRestricao']:
            reqs.add('dt_calculo')

        return reqs


    def value(self):
        if self.method in ['CalcPreco', 'CalcPrecoData', 'CalcPrecoPrazo',
                           'CalcPrecoPrazoData', 'CalcPrecoPrazoRestricao']:

            if self.input.get('vl_diametro') == None:
                self.input.update({'vl_diametro': 5})

            if self.input.get('vl_declarado') == None:
                self.input.update({'vl_declarado': 0})

            if self.input.get('cd_aviso_recebimento') == None:
                self.input.update({'cd_aviso_recebimento': False})

            if self.input.get('cd_mao_propria') == None:
                self.input.update({'cd_mao_propria': False})

            if self.input.get('vl_comprimento') == None:
                self.input.update({'vl_comprimento': 18})

            if self.input.get('vl_altura') == None:
                self.input.update({'vl_altura': 0})

            if self.input.get('vl_largura') == None:
                self.input.update({'vl_largura': 0})

        return self.input
