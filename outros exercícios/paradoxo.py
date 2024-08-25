# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 14:39:18 2022

@author: guilh
"""

from random import randint

class portas:
    
    def __init__(self, numeroDePortas):
        self.numeroDePortas = numeroDePortas
        self.portaCerta, self.portaParaASegundaDecisao = 0, 0 
        while self.portaCerta == self.portaParaASegundaDecisao:
            self.portaCerta, self.portaParaASegundaDecisao = randint(1, numeroDePortas), randint(1, numeroDePortas)
          
    def devolveNumeroDePortas(self):
        return self.numeroDePortas
        
    def devolvePortaCerta(self):
        return self.portaCerta
    
    def devolvePortaParaASegundaDecisao(self):
        return self.portaParaASegundaDecisao

def partecipante(numeroDePortas, portaCerta, portaParaASegundaDecisao, dadosEstatisticos):
    
    primeiraPortaEscolhida = randint(1, numeroDePortas)
    
    if primeiraPortaEscolhida != portaCerta:
        dadosEstatisticos.AcrescentarNumeroDeVezesAcertadas()

def dadosInicias():
    
    numeroDePortas = int(input('Quantas portas inicias deve existir: '))
    numeroDeTentativas = int(input('Quantas vezes a experiência deve acontecer: '))
    portasDoJogo = portas(numeroDePortas)
    dadosEstatisticos = estatisticas(numeroDeTentativas)
    
    probabilidadeNaoTrocandoAPorta = 1/numeroDePortas*100
    probabilidadeTrocandoAPorta = 100 - probabilidadeNaoTrocandoAPorta
    
    print()
    print('As probabilidades pela teoria deviam se aproximar de', round(probabilidadeTrocandoAPorta, 3), '% quando se troca de porta e', round(probabilidadeNaoTrocandoAPorta, 3), '% quando não se troca de porta.', end = '\n')
    
    return numeroDeTentativas, portasDoJogo, dadosEstatisticos

class estatisticas():
    
    def __init__(self, numeroDeTentativas):
        self.numeroDeVezesAcertadas = 0
        self.numeroDeTentativas = numeroDeTentativas
    
    def AcrescentarNumeroDeVezesAcertadas(self):
        self.numeroDeVezesAcertadas = self.numeroDeVezesAcertadas + 1
           
    def devolverPorcentagemNumeroDeVezesAcertadas(self):
        return round(self.numeroDeVezesAcertadas/self.numeroDeTentativas*100, 3)
    
def dadosFinais(dadosEstatisticos):
    
    print()
    print('Taxa de sucesso', dadosEstatisticos.devolverPorcentagemNumeroDeVezesAcertadas(), '%.')
    print('Taxa de erro', round(100-dadosEstatisticos.devolverPorcentagemNumeroDeVezesAcertadas(), 3), '%.')
    
    
def main():
    
    numeroDeTentativas, portasDoJogo, dadosEstatisticos = dadosInicias()
    for a in range(numeroDeTentativas):
        partecipante(portasDoJogo.devolveNumeroDePortas(), portasDoJogo.devolvePortaCerta(), portasDoJogo.devolvePortaParaASegundaDecisao(), dadosEstatisticos)
    dadosFinais(dadosEstatisticos)
    
main()    