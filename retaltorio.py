from datetime import datetime
from weasyprint import HTML
from variaveis_relatorios import styles
from slugify import slugify

def criar_relatorio():
    nome_ferramenta ="FA_TESTE"
    header = criar_html_header(nome_ferramenta,"Giovani", "logo.png")
    resumo =criar_html_resumo ("Apenas um resumo de teste")
    testes = [
            {"nome_teste":"aaaa","testes":[
                {"metrica":"org", "esperado":"A","recebido":"A"},
                {"metrica":"tes", "esperado":"A","recebido":"A"},
                {"metrica":"oqe", "esperado":"A","recebido":"A"},
                {"metrica":"eee", "esperado":"A","recebido":"A"},
                ] },
            {"nome_teste":"bbbb","testes":[
                {"metrica":"org", "esperado":"B","recebido":"A"},
                {"metrica":"tes", "esperado":"A","recebido":"A"},
                {"metrica":"oqe", "esperado":"A","recebido":"A"},
                {"metrica":"eee", "esperado":"C","recebido":"A"},
                ] },
            ]

    resumo_testes_0 = criar_html_resumo_teste(testes[0]['nome_teste'], testes[0]['testes'])
    resumo_testes = criar_html_resumo_teste(testes[1]['nome_teste'], testes[1]['testes'])

    saida_detalhada =criar_html_saida_detalhada("bbbb", "aa","asf","wwww") 
    saida_detalhada_1 =criar_html_saida_detalhada("aaaa", "aa","asf","wwww") 

    
    relatorio_html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Exemplo PDF</title>
    <style>
    {styles.style}
    </style>
</head>

<body>
    {header['html']}
    <div class="container-content">
    {resumo['html']}
    {resumo_testes['html']}
    {resumo_testes_0['html']}
    {saida_detalhada['html']}
    {saida_detalhada_1['html']}
    </div>
</body>
</html>
    """
    # print(relatorio_html)

    HTML(string=relatorio_html).write_pdf(f'relatorio_{nome_ferramenta}.pdf')
    with open("relatorio.html", "w") as file:
        file.write(relatorio_html)
    print("PDF gerado com sucesso: saida_dinamica.pdf")

def criar_html_saida_detalhada(nome_teste, descricao_saida, request, response):
    link_saida_detalhada = slugify(nome_teste)
    print("criar_html_requisisao: ", link_saida_detalhada)
    html = f"""
      <div id={link_saida_detalhada} clas="saida-detalhada">
        <h1 id="{nome_teste}">{nome_teste}</h1>
        <p><b>Saida esperada: </b>{descricao_saida}</p>
        <div class="reques-e-reponse">
          <div class="request">{request}</div>
          <div class="reponse">{response}</div>
        </div>

      </div>
    """
    return {'html':html}
    ...

def criar_html_header(nome_ferramenta, autor, caminho_img_header):
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%B/%Y")
    return {'html':f"""
    <header id="header-pg-resumo">
      <div class="titulo">
        <img src="{caminho_img_header}" alt="assesso logo" />
        <p>Relatorio - {nome_ferramenta}</p>
      </div>
      <div class="autor-data">
        <div>
        <b>Autor:</b> {autor}</div>
        <div id="data"><b>{data_formatada.replace(data_formatada[3:], data_formatada[3:].capitalize())}</b></div>
    </header>
            """}


def criar_html_resumo_teste(nome_teste, metricas):

    html_metricas = f"""
        <div class="container-teste">

          <h2>{nome_teste}</h2>

          <div class="metricas-container">
    """
    quantidade_de_erros = 0
    link_saida_detalhada = slugify(nome_teste)

    for i in metricas:
        tmp = criar_html_metrica(  i['metrica'],i['esperado'], i['recebido'])
        html_metricas += tmp['html']
        quantidade_de_erros += 0 if tmp['resultatos_estao_iguais'] else 1 


    if quantidade_de_erros !=0:
        ...
        html_metricas += f"""
    </div>
            <p class="teste-reprovado"><b>Reprovado</b></p>
        """
    else:
        html_metricas += f"""
    </div>
            <p class="teste-aprovado" ><b>Aprovado</b></p>
        """

            # <a href="#{nome_teste}">Ver saida detelhada</a>
    html_metricas += f"""
            <a href="#{link_saida_detalhada}">Ver saida detelhada</a>
        </div>
    """

    
    return {"html":html_metricas}

def criar_html_metrica(metrica, resultado_esperado, resultado_recebido):
    resultatos_estao_iguais = resultado_esperado == resultado_recebido
    # classe_metrica = "metrica" if not resultatos_estao_iguais   else " metrica metrica-reporvada" 
    classe_metrica = "" if  resultatos_estao_iguais   else " metrica-reporvada" 

    html = f"""
        <div class= "metrica-container" >
            <div class= {classe_metrica}>
                <h3>{metrica}</h3>
                <p class="resultado-esperado">Valor esperado: "{resultado_esperado}"</p>
                <p class="resultado-esperado">Valor recebido: "{resultado_recebido}"</p>
            </div>
        </div>
    """
    return {"html":html, "resultatos_estao_iguais":resultatos_estao_iguais}


def criar_html_resumo(resumo):
    return { "html": f"""
<h1>Resumo</h1>
<p>{resumo}</p>
            """}
