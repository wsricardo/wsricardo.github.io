"""
Projeto: AnaliseLinear
Disciplina: Programação 1A
Author: Wandeson Ricardo
Github: www.github.com/wsricardo
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy


class AnaliseLinear:
    """
        Análise linear por minimos quadrados para aproximar os dados
        por uma função linear f(x) = ax + b.
        Dados usados da população do Brasil ao longo dos anos.
        
        Atributos:
            
            data -> dados obtidos em um arquivos csv
            df_country -> armazena um grupo especifico dos dados (neste cado a população para o Brasil)
            x, y -> pontos para os dados Anos x População
            lin_ajus -> armazena resultado restornado pela função linregress
            
        Metodos:
            
            __init__ -> construtor da classe
            ler_dados -> leitura dos dados
            plotar_dados -> desenho dos dados
            ajuste_linear -> calculando o ajuste linear
            mostrar_resultados -> exibe resultados do ajuste
            plotar_ajuste -> desenho gráfico para equação do ajuste e dos dados
            set_country -> define país que será considerado na análise.
    """
    
    
    def __init__( self, filename=None, country=None ):
        
        self.data = None
        self.filename = filename
        self.country = country
        self.x = []
        self.y = []
        self.df_country = None
        self.lin_ajus = None
        
        if country != None and filename != None:
            self.ler_dados( ) 
            self.set_country( country )
    
    def ler_dados( self, filename=''  ):
        """
            Abri e lê os dados no arquivo 'filename' em formato csv.

        """
        
        if filename != '':
            self.filename = filename
            
        self.data = pd.read_csv( self.filename )
        return self.data
    
    def plotar_dados( self ):
        """
            Desenha os pontos dos dados no arquivo csv em gráfico.
        """
        
        df = self.data[ self.data[ 'Country Name' ] == self.country ]
        df.plot.scatter( x = 'Year', y = 'Value' )
        
        
    
    def ajuste_linear( self ):
        """
            Computando valores para o ajuste linear usados na construção da
            função linear f(x) = ax + b qual aproxima os dados.
        """
        
        self.lin_ajus = scipy.stats.linregress( x = self.df_country['Year'].values, 
                                               y = self.df_country['Value'].values )
        
    
    def mostrar_resultado( self ):
        """
            Imprimir resultados, inclinação, intercepto, equação ajustada
            e valor R^2. Após a computação do ajuste linear com a função
            linregress cujo retorno é armazenado em 'lin_ajus' temos nesta 
            os valores da inclinação, intercepto, R nos atributos slope,
            intercept e rvalue respectivamente.
        """
        
        print(f"Inclinação: {self.lin_ajus.slope:.3e}\nIntercepto: {self.lin_ajus.intercept:.3e}")
        print(f"R^2 (coeficiente de determinação [rvalue^2]): {self.lin_ajus.rvalue**2}")
        print(f"Equação ajustada: P(x) = {self.lin_ajus.slope:.3e}x + {self.lin_ajus.intercept:.3e}\n")
        
        
    
    def plotar_ajuste( self ):
        """
            Desenho do gráfico para os pontos dos dados e ajuste linear para
            aproximação destes dados em um mesmo gráfico.
        """
        
        if self.df_country is not None:
            xi = self.df_country['Year'].values
            fig, ax = plt.subplots( figsize=(10,6), layout='constrained' )
            
            ax.plot( xi, self.lin_ajus.slope*xi + self.lin_ajus.intercept, 
                     '-', label='Ajuste Linear', 
                      )
            ax.plot( xi,
                     self.df_country['Value'].values, 
                     'ro', label='Dados Coletados' )
            ax.set_xlabel( 'Ano' )
            ax.set_ylabel( 'População' )
            ax.legend( )
            ax.set_title( "População do Brasil ( Ano x População )")
        
    
    def set_country( self, country = '' ):
        """
            Aqui definimos o país para o qual consideraremos a população
            ao longo dos anos e armazenamos em df_country.
        """
        
        self.df_country = self.data[ self.data[ 'Country Name' ] == country ]
        
    
if __name__ == '__main__':
    
    s = AnaliseLinear( 'population.csv', 'Brazil' )
    #s.ler_dados(  )
    s.plotar_dados()
    s.ajuste_linear() 
    s.plotar_ajuste()
    s.mostrar_resultado()
    

