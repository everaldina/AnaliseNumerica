import sympy as sp
import common

def jacobi(matrizB, vetorG, precisao, vet_inical = None):
    # verifica se a matriz B como é convergente 
    if common.check_converge(matrizB):
        n = sp.shape(matrizB)[0]
        
        # se vet_inical for None, vet_inical = vetor nulo
        if vet_inical is None:
            vet_inical = sp.zeros(n, 1)

        # vet_0 recebe vet_inical
        vet_0 = vet_inical.copy()
        
        # vet_1 vai receber o resultado da iteração
        vet_1 = matrizB*vet_0 + vetorG
        
        # calcula erro absoluto e relativo
        eabs, erel = common.return_variacao(vet_1, vet_0)
        
        # enquanto erro absoluto ou relativo for maior que precisao continua iteração
        while(eabs > precisao or erel > precisao):
            vet_0 = vet_1.copy() # vet_0 recebe vet_1
            vet_1 = matrizB*vet_0 + vetorG # recalcula vet_1
            eabs, erel = common.return_variacao(vet_1, vet_0) # recalcula erro absoluto e relativo
        return vet_0
    else:
        return None


#mA = sp.Matrix([[10,2,1],[1,5,1],[2,3,10]])
#mb = sp.Matrix([[7],[-8],[6]])
#B = common.return_matrizB(mA, 3)
#print(B)
#g = common.return_vetorG(mA, mb, 3)
#print(g)
#print(jacobi(B, g, 10**-2, sp.Matrix([[0.7],[-1.6],[0.6]])))

    
    
