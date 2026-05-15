import pandas as pd
df_fl=pd.read_excel("FLOWRACKS CHANGAN - REV04.xlsm")
df_geral=pd.read_csv("database_log_todo.csv",encoding="latin1",
    sep=";",
    on_bad_lines="skip")
linhas = []
for _, row in df_fl.iterrows():
    for end in str(row["ENDEREÇO"]).split("\n"):
        partes = [p.strip() for p in end.split("/")]
        if len(partes) >= 4:
            nova = row.copy()
            nova["Estação"] = partes[0]
            nova["Flowrack"] = partes[1]
            nova["Nível"] = partes[2]
            nova["Posição"] = partes[3]
            linhas.append(nova)
df_fl_tratado = pd.DataFrame(linhas)
df_fl_tratado.drop(columns="ENDEREÇO", inplace=True)
df_fl_tratado["MODELO"] = df_fl_tratado.apply(
    lambda x: df_geral[
        (df_geral["CODIGO"].astype(str).str.strip() == str(x["PART NUMBER"]).strip()) &
        (df_geral["ESTACAO"].astype(str).str.strip() == str(x["Estação"]).strip())
    ]["MODELO"].iloc[0]
    if not df_geral[
        (df_geral["CODIGO"].astype(str).str.strip() == str(x["PART NUMBER"]).strip()) &
        (df_geral["ESTACAO"].astype(str).str.strip() == str(x["Estação"]).strip())
    ].empty
    else None,
    axis=1
)
