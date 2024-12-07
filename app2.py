from openai import OpenAI
import pandas as pd

def carregar_planilha(file_path):
    return pd.read_excel(file_path)

def executar_prompt(df, prompt):
    client = OpenAI()

    mensagens = [
        {"role": "system", "content": "Você é um assistente que ajuda a manipular dados de planilhas."},
        {"role": "user", "content": f"Aqui está a estrutura da planilha: {df.to_string()}. {prompt}"}
    ]

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens
    )

    return resposta.choices[0].message.content

def main(file_path):
    df = carregar_planilha(file_path)

    print("Planilha carregada com sucesso!")

    prompt = input("Digite o que deseja fazer com os dados da planilha: ")

    resposta = executar_prompt(df, prompt)

    print("Resposta da OpenAI:")
    print(resposta)

if __name__ == "__main__":
    caminho_arquivo = "simulacao_provisoes_ferias_13.xlsx"
    main(caminho_arquivo)
