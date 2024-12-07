from openai import OpenAI
import pandas as pd

def processar_planilha(file_path):
    
    df = pd.read_excel(file_path)

    filtro = (df['Vencimento Base'] == 10500.00) & (df['Gratificação Judicial'] == 1200.00)
    servidores_filtrados = df[filtro]

    resultados = []

    for _, row in servidores_filtrados.iterrows():
        nome = row['Nome']
        matricula = row['Matricula']
        vencimento_base = row['Vencimento Base']
        gratificacao_judicial = row['Gratificação Judicial']

        vencimento_bruto = vencimento_base + gratificacao_judicial
        vencimento_anual = 12 * vencimento_bruto

        provisao_ferias = 1/3 * vencimento_bruto
        provisao_13_salario = vencimento_anual / 12
        total_anual = vencimento_anual + provisao_ferias + provisao_13_salario

        resultados.append({
            "Nome": nome,
            "Matricula": matricula,
            "Provisão mensal de férias": round(provisao_ferias, 2),
            "Provisão mensal de 13º salário": round(provisao_13_salario, 2),
            "Total anual provisionado": round(total_anual, 2)
        })

    return resultados

def main(file_path):
    client = OpenAI()

    resultados = processar_planilha(file_path)

    mensagens = [
        {"role": "system", "content": "Você é um especialista em gestão de provisões da folha de pagamento."},
        {"role": "user", "content": "Analise os seguintes dados e retorne os valores provisionados em formato de tabela:\n"}
    ]

    for res in resultados:
        mensagens.append({
            "role": "system",
            "content": (f"Nome: {res['Nome']}, Matricula: {res['Matricula']}, "
                        f"Provisão mensal de férias: R$ {res['Provisão mensal de férias']}, "
                        f"Provisão mensal de 13º salário: R$ {res['Provisão mensal de 13º salário']}, "
                        f"Total anual provisionado: R$ {res['Total anual provisionado']}\n")
        })

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens
    )

    print("Resposta da OpenAI:")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    caminho_arquivo = "simulacao_provisoes_ferias_13.xlsx"
    main(caminho_arquivo)
