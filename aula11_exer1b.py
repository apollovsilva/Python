class matriz5x5:

    def __init__(self):
        self.matrix = {(0,3): 1, (2,1): 2, (4,3): 3}

    def __str__(self):
        
        
    def teste(self, x, y):
        print(self.matrix.get((x,y), 0))




a = matriz5x5()
#a.teste(4,3)
#a.teste(2,2)
for x in range(5):
    for y in range(5):
        a.teste(x,y)










   # matrix = {(0,3): 1, (2,1): 2, (4,3): 3}


    #def gerar_matriz (n_linhas, n_colunas):
     #   matrix = {}
      #  for x in range(5):
       #     for y in range(5):
        #        t = matrix.get((x,y))
            # print(t)

   # for i in range(n_linhas):
   #     matrix[i] = ( [t] * n_colunas )

   # return matrix


#print(gerar_matriz(5,5))




