from setuptools import setup, find_packages

setup(
    name='CorreiosPrecoPrazo',
    version='1.0',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['xmltodict', 'requests'],
    keywords='correios preços prazos webservice correio api preço prazo',  # Optional
    url='',
    license='MIT',
    author='Andre Sionek',
    author_email='andresionek91@gmail.com',
    description='Correios Preços e Prazos - Python API'
)
