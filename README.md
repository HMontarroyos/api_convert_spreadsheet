<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br>

<a href="#API Convert Spreadsheet">API Convert Spreadsheet</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#Tecnologias-Utilizadas">Tecnologias Utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#Como-Instalar-o-Projeto">Como Instalar o Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#Como-usar">Como usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#Deploy-da-aplicação">Deploy da aplicação</a>

<br>

## <strong>API Convert Spreadsheet</strong>

<br>

<br>

<img width="958" alt="api_convert" src="https://github.com/HMontarroyos/api_convert_spreadsheet/assets/60220406/f3d3bd0a-adb2-4ca7-8edf-cb5da473f3b6">

<br/>
<br/>
<br/>

Essa API foi desenvolvida em Python através do FastAPI, com o proposito, de receber planilhas de custos de clientes no formato XLSX, e após isso conferir se bate com as propriedades esperadas pelo modelo, caso confirma ela converte esses dados em uma espécie de JSON e devolve isso como resposta.

<br/>
<br/>

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>

### <strong>Tecnologias Utilizadas</strong>

<br>

[![Python][Python]][Python-url]
[![Fast_API][Fast_API]][Fast_API-url]
[![Uvicorn][Uvicorn]][Uvicorn-url]
[![Pandas][Pandas]][Pandas-url]
[![Pydantic][Pydantic]][Pydantic-url]
[![Httpx][Httpx]][Httpx-url]
[![Pytest][Pytest]][Pytest-url]
[![Docker][Docker]][Docker-url]

<br>

### <strong>Utilitários</strong>

 [![Postman][Postman]][Postman-url]

<br>

<p align="right">(<a href="#readme-top">de volta ao topo</a>)</p>

### <strong>Como Instalar o Projeto</strong>

<br>

Após clonar o projeto use o seguinte comando.

```sh
pip install -r requirements.txt
```

Após baixar todas as Dependências do Projeto dentro da pasta Raiz, inicie o Servidor com o Comando:

```sh
 python src/main.py
```

### <strong>Como usar</strong>

<br>

Feito todo os passos acima o seu servidor  vai estar  rodando na <i>porta 4005</i>.

#### Endpoints 

Para Fazer as chamadas dos endpoints da API seria necessario ter algum cliente servidor no meu caso eu usei o <i>Postman</i> mas qualquer um já serviria.

<i>Estou usando a porta 4005 para rodar minha aplicação.</i>


### POST 

http://localhost:4005/spreadsheet/

<br/>
Essa  rota é onde você vai enviar seu arquivo <i>.xlsx</i> e ele vai fazer essa conversão para o JSON e e lhe devolver esse JSON como resposta.

</br>
</br>

#### Testes 

Caso queira rodar os testes para vê se está tudo correto pode executar o seguinte comando 

```sh
python -m pytest
```
que o PyTest vai executar os tests que foram criados para ele.

<br>

### 🚀 Let's code! 🚀

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/HMontarroyos/api_convert_spreadsheet.svg?style=for-the-badge
[contributors-url]: https://github.com/HMontarroyos/api_convert_spreadsheet/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HMontarroyos/api_convert_spreadsheet.svg?style=for-the-badge
[forks-url]: https://github.com/HMontarroyos/api_convert_spreadsheet/fork
[stars-shield]: https://img.shields.io/github/stars/HMontarroyos/api_convert_spreadsheet.svg?style=for-the-badge
[stars-url]: https://github.com/HMontarroyos/api_convert_spreadsheet/stargazers
[issues-shield]: https://img.shields.io/github/issues/HMontarroyos/api_convert_spreadsheet.svg?style=for-the-badge
[issues-url]: https://github.com/HMontarroyos/api_convert_spreadsheet/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/hebertmontarroyos-developer/

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Fast_API]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[Fast_API-url]: https://fastapi.tiangolo.com/
[Uvicorn]: https://img.shields.io/badge/uvicorn-6A5FBB?style=for-the-badge
[Uvicorn-url]: https://www.uvicorn.org/
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Pydantic]:https://img.shields.io/badge/Pydantic-%233F4F75.svg?style=for-the-badge
[Pydantic-url]: https://docs.pydantic.dev/latest/
[Httpx]: https://img.shields.io/badge/Httpx-%230C55A5.svg?style=for-the-badge
[Httpx-url]: https://www.python-httpx.org/
[Pytest]: https://img.shields.io/badge/PyTest-%2300599C.svg?style=for-the-badge
[Pytest-url]: https://docs.pytest.org/en/7.4.x/




[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Postman]: https://img.shields.io/badge/Postman-gray?style=for-the-badge&logo=postman
[Postman-url]: https://www.postman.com/

