style = """
@page {
        size: A4; /* Change from the default size of A4 */
        margin: 20mm 0mm; /* Set margin on each page */
      }
        @page :first {
            margin: 0cm 0cm 10mm 0cm; /* Margin for the first page */
        }

body {
  --vermelho-assesso: #cc0002;
  padding: 0px;
  margin: 0px;
    font-size:12px;
  font-family: Arial, Helvetica, sans-serif;
}

h1 {
  color: var(--vermelho-assesso);
  font-size: 44px;
}

h2 {
  margin-top: 10px;
}

#header-pg-resumo {
  background-color: var(--vermelho-assesso);
  color: #fff;
}
#header-pg-resumo .titulo {
  padding: 12px;
  display: flex;
  flex-direction: row;
  align-items: center;
  border-bottom: 1px solid #fff;
}
#header-pg-resumo .titulo p {
  margin-left: 40px;
  font-size: 30px;
}
#header-pg-resumo .autor-data {
  padding: 6px 12px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
#header-pg-resumo .autor-data {
  font-size: 20px;
}

.container-content {
  padding: 24px 50px;
}

.teste-aprovado,
.teste-reprovado {
  margin: 20px 0px;
  text-align: center;
  color: white;
  padding: 10px;
}

.teste-aprovado {
  background-color: green;
}
.teste-reprovado {
  background-color: red;
}
.metrica-reporvada {
  color: red;
  font-weight: bold;
}

.metricas-container{
    display: flex;
    justify-content: space-between;
    flex-direction:row;
flex-wrap: wrap;
}

.metrica-container{
    min-width: 30%;
    margin-right: 20px
}

.container-teste{
    display:flex;
    flex-direction:column; 
}

.resultado-esperado {
    font-family: "Courier New", Courier, "Lucida Console";
    line-height: 0.8;
}

.metrica {
  margin-bottom: 10px;
}

.reques-e-reponse {
  display: flex;
  flex-direction: row;
  color: #888888;
}

.request {
  width: 100%;
  padding: 10px;
}
.reponse {
  border-left: 1px solid #000;
  width: 100%;
  padding: 10px;
}
"""
