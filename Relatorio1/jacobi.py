import sympy as sp
import common

def jacobi(matrizB, vetorG, precisao, vet_inical = None):
    if common.check_converge(matrizB):
        n = sp.shape(matrizB)[0]
        
        if vet_inical is None:
            vet_inical = sp.zeros(n)

        vet_0 = vet_inical.copy()
        vet_1 = matrizB*vet_0 + vetorG
        
        eabs, erel = common.return_variacao(vet_1, vet_0)
        while(eabs > precisao or erel > precisao):
            vet_0 = vet_1.copy()
            vet_1 = matrizB*vet_0 + vetorG
            eabs, erel = common.return_variacao(vet_1, vet_0)
        return vet_1
    else:
        return None

    
    
