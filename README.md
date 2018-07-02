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
    >>> consulta.calculate('CalcPrecoPrazo',
                            {'cd_servico': '04669',
                            'cep_origem': '80250220',
                            'cep_destino': '01023302',
                            'vl_peso': 1500,
                            'cd_formato': 'caixa',
                            'vl_largura': 20,
                            'vl_altura': 20,
                            'vl_comprimento': 20,
                            'valor_declarado': 180,
                            })
                            
    {
    "Codigo": "4669",
    "Valor": "19,06",
    "PrazoEntrega": "6",
    "ValorMaoPropria": "0,00",
    "ValorAvisoRecebimento": "0,00",
    "ValorValorDeclarado": "1,13",
    "EntregaDomiciliar": "S",
    "EntregaSabado": "N",
    "Erro": "0",
    "MsgErro": null,
    "ValorSemAdicionais": "17,93",
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
    >>> consulta.list_services()
    
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
Weight value. **Must be in gram**.

cd_formato
--------------
Package format, either of the values bellow are acceptable:

* Boxes: `'caixa', 'pacote', 1, '1'`
* Cilinders/Prims: `'rolo', 'prisma', 2, '2'`
* Envelopes: `'envelope', 3, '3'`

vl_comprimento
-------------
Length value. **Must be in cm**.

*Required for:*
* Boxes
* Envelopes

vl_largura
-----------
Width value. **Must be in cm**.

*Required for:*
* Boxes
* Envelopes

vl_altura
----------
Height value. **Must be in cm**.

*Required for:*
* Boxes

vl_diametro
--------------
Diameter value. **Must be in cm**.

*Required for:*
* Cilinders/Prims

cd_mao_propria *Optional*
--------------
Boolean. If you want a quote with Mão Própria service.

cd_aviso_recebimento *Optional*
-------------------
Boolean. If you want a quote with Aviso de Recebimento service.

valor_declarado *Optional*
----------------
Decimal. If you want a quote with insurance service, pass the value in BRL.

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
