class Filmes:
    def __init__(self, nome,realizador,ano,classificacao, genero, sala, reservas):
        self.nomeInit = nome
        self.realizadorInit = realizador
        self.anoInit = ano
        self.classificacaoInit = classificacao
        self.generoInit = genero
        self.salaInit = sala
        self.reservasInit = reservas
    
    def obterNome(self):
        return self.nomeInit
    
    def obterRealizador(self):
        return self.realizadorInit
    
    def obterAno(self):
        return self.anoInit
    
    def obterClassificacao(self):
        return self.classificacaoInit
    
    def obterGenero(self):
        return self.generoInit
    
    def obterSala(self):
        return self.salaInit
    
    def obterReservas(self):
        return self.reservasInit
    
    def alterarReservas(self,reservasAtuais):
        self.reservasInit = reservasAtuais

objFilmes = []

import pandas as pd
import matplotlib as plt

df = pd.DataFrame (objFilmes,["nome","realizador","ano","genero","classificação","sala","reservas"])


