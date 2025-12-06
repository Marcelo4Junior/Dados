import pandas as pd
import numpy as np

n=16000600
dados = {
    "Mes": np.random.choice(
        ["Jan" , "Fev" , "Mar" , "Abr" , "Mai" , "Jun" , "Jul" , "Ago" , "Set" , "Out" , "Nov" , "Dez"], n
    ), 
    "Pagantes": np.random.randint(400, 6000, n), 
    'Inadimplentes': np.random.randint(400, 6000, n)

}
df = pd.DataFrame(dados)

df.to_excel("Dados.xlsx" , index=False)
print("Arquivo gerado com sucesso!")

df = pd.read_excel("Dados.xlsx")

colunas_numericas = df.select_dtypes(include='number')

resumo = pd.DataFrame({
    "Media": colunas_numericas.mean(),
    "Minimo": colunas_numericas.min(),
    "Maximo": colunas_numericas.max(),
})

print ("\nResumo estatistico (Media, Minimo, Maximo)")
print(round(resumo, 4))