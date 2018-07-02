from setuptools import setup,find_packages

setup(
    name='CorreiosPrecoPrazo',
    version='1.0',
    packages=find_packages(),
    install_requires=['xmltodict', 'requests'],
    keywords='correios preços prazos webservice correio api preço prazo',
    url='https://github.com/andresionek91/CorreiosPrecoPrazo',
    license='MIT',
    classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3.6'],
    author='Andre Sionek',
    author_email='andresionek91@gmail.com',
    description='Correios Preços e Prazos - Python API'
)