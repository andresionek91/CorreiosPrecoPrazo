from setuptools import setup

setup(
    name='CorreiosPrecoPrazo',
    version='1.0',
    py_modules=["api"],
    install_requires=['xmltodict', 'requests'],
    keywords='correios preços prazos webservice correio api preço prazo',  # Optional
    url='',
    license='MIT',
    classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3.6'],
    author='Andre Sionek',
    author_email='andresionek91@gmail.com',
    description='Correios Preços e Prazos - Python API'
)