CorreiosPrecoPrazo
===========

Overview
========

CorreiosPrecoPrazo is a Python wrapper for Correios webservice. Use it to get 
freight prices and delivery time. Send a json payload with the parameters for 
calculation and get back a json with the requested info.  

Status
======

This library is in testing mode and is not inteded for production environments.

Installation
===============
Install directly from this git repository:

`pip install git+https://github.com/andresionek91/CorreiosPrecoPrazo`


Usage sample
============

.. code-block:: python

    >>> from CorreiosPrecoPrazo.core import Correios
    >>> consulta = Correios()
    >>> r = consulta.calculate('CalcPrecoPrazo',
                                {'cd_servico': '04014',
                                'cep_origem': '01311-000',
                                'cep_destino': '70083-900',
                                'vl_peso': 1550,
                                'cd_formato': 'caixa',
                                'vl_largura': 24,
                                'vl_altura': 23,
                                'vl_comprimento': 20,
                                'valor_declarado': 189.90,
                                })
    >>> print(json.dumps(r, indent=4)) 
                            
    {
        "Codigo": "4014",
        "Valor": "40,47",
        "PrazoEntrega": "1",
        "ValorMaoPropria": "0,00",
        "ValorAvisoRecebimento": "0,00",
        "ValorValorDeclarado": "2,57",
        "EntregaDomiciliar": "S",
        "EntregaSabado": "S",
        "Erro": "0",
        "MsgErro": null,
        "ValorSemAdicionais": "37,90",
        "obsFim": null
    }


Available Methods
===================

* CalcPrazo
* CalcPrazoData
* CalcPrazoRestricao
* CalcPreco
* CalcPrecoData
* CalcPrecoPrazo
* CalcPrecoPrazoData
* CalcPrecoPrazoRestricao


If You Have a Contract
===================
Optional, only if you have a contract with Correios.

. code-block:: python

    >>> from CorreiosPrecoPrazo.core import Correios
    >>> consulta = Correios(cod_administrativo='cod_administrativo', senha='password')

    
Available Services
===================
Get the service numbers by seeing wich services are currently available for use.

. code-block:: python

    >>> from CorreiosPrecoPrazo.core import Correios
    >>> consulta = Correios()
    >>> s = consulta.list_services()
    >>> print(json.dumps(s, indent=4))
    
    [
    {
        "codigo": "02259",
        "descricao": "MALA DIRETA PERFIL EXTERNO",
        "calcula_preco": "N",
        "calcula_prazo": "S",
        "erro": null,
        "msgErro": null
    },
    {
        "codigo": "02267",
        "descricao": "CORREIOS LISTA DISTR URGENTE",
        "calcula_preco": "N",
        "calcula_prazo": "S",
        "erro": null,
        "msgErro": null
    },
    {
        "codigo": "02275",
        "descricao": "CORREIOS LISTA DISTRIBUICAO",
        "calcula_preco": "N",
        "calcula_prazo": "S",
        "erro": null,
        "msgErro": null
    },
    ...

Input Parameters
===================

cd_servico
---------
Service code. See wich services are available for you by calling the 
method `list_services()`

cep_origem
--------------
Origin zip code. Formats that are acceptable:

* 12345-678
* 12345678

cep_destino
--------------
Destination zip code. Formats that are acceptable:

* 12345-678
* 12345678

vl_peso
---------------
Integer. Weight value. **Must be in gram**.

cd_formato
--------------
Package format, either of the values bellow are acceptable:

* Boxes: `'caixa', 'pacote', 1, '1'`
* Cilinders/Prims: `'rolo', 'prisma', 2, '2'`
* Envelopes: `'envelope', 3, '3'`

vl_comprimento
-------------
Integer. Length value. **Must be in cm**.

*Required for:*
* Boxes
* Envelopes

vl_largura
-----------
Integer. Width value. **Must be in cm**.

*Required for:*
* Boxes
* Envelopes

vl_altura
----------
Integer. Height value. **Must be in cm**.

*Required for:*
* Boxes

vl_diametro
--------------
Integer. Diameter value. **Must be in cm**.

*Required for:*
* Cilinders/Prims

cd_mao_propria
--------------
*Optional* Boolean. If you want a quote with Mão Própria service.

cd_aviso_recebimento
-------------------
*Optional* Boolean. If you want a quote with Aviso de Recebimento service.

valor_declarado 
----------------
*Optional* Decimal. If you want a quote with insurance service, pass the value in BRL.

dt_calculo
------------
Reference date for calculations. 

*Required for the following methods:*
* CalcPrazoData
* CalcPrazoRestricao
* CalcPrecoData
* CalcPrecoPrazoData
* CalcPrecoPrazoRestricao

License
=======

This library is published under the terms of the MIT License. Please check the
LICENSE file for more details.
