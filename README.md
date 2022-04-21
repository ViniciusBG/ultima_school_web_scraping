# ultima_school_web_scraping

Aula para prototipagem de um scraper usando o Selenium.

O Notebook utilizado para a parte de APIs pode ser encontrado no seguinte [link](https://colab.research.google.com/drive/1iS43Oj7Uiu77nvMzw1sV6uciOSWD1K9O?usp=sharing)

O Notebook que criamos durante a aula está [aqui](https://github.com/ViniciusBG/ultima_school_web_scraping/blob/main/scraping_linkedin.ipynb)

## Para rodar o script completo (chamando via terminal):
- Certifique-se de que todas as dependências estão isntaladas (estão no requirements.txt)
- Abra uma janela do terminal **na pasta em que os scripts se encontram**
- Rode o seguinte comando:
```python app.py -l <local_da_vaga> -j <titulo_da_vaga>```

Por exemplo, se você quer procurar por vagas de cientista de dados em São Paulo, o comando será o seguinte:\
```python app.py -l "São Paulo" -j "Cientista de dados"```

