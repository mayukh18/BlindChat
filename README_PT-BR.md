# BlindChat

Um facebook messenger bot que permite aos usuários conversar com outras pessoas no facebook anonimamente. É mais como o Omegle para Messenger, com algumas diferenças em vez de melhorias.



Você pode encontrá-lo ao vivo [***Aqui***](https://m.me/blindchat.go)





### Um pouco do densenvolvimento

Eu comecei a construir o BlindChat apenas para experimentar a plataforma do messenger do facebook e tentar construir algo utilizável e aprendendo no processo. É mais um aplicativo do que um chatbot da IA. O resultado foi um pouco de tração e, portanto, eu melhorei algumas partes dele. Mas a maior parte do código pode estar em uma condição não organizada, uma vez que eles são criados para uma rápida criação de protótipos.





### Configuração do ambiente local / Configuração da versão do aplicativo

O BlindChat está atualmente hospedado no heroku e também usa o banco de dados oferecido. Então o código e a configuração foram escritos para isso. Se você não quiser usar o heroku, terá que modificar alguns lugares. Se você está bem com heroku, então você está no caminho certo. É melhor ter um pouco de conhecimento para configurar um mensageiro.



1. Clone o repositório. Abra o terminal/cmd e execute `git clone https://github.com/mayukh18/BlindChat.git/` e configure seu repositório local.

2. Crie um aplicativo de mensageiro no facebook. Adicione e configure o webhook e anote o *Token de Acesso* and *Token de Verificação*. Coloque-os em **config.py** em seus respectivos lugares.

3. Crie um aplicativo no heroku. Abra o terminal/cmd e execute `heroku create yourappname`. Você encontrará o URL do aplicativo como `https://yourappname.herokuapp.com/`. Put it on **config.py**. Note que você primeiro terá que instalar o *heroku CLI toolbelt* se não o tiver.

4. Próxima execução `pip install -r requirements.txt`. Isso instalará as bibliotecas em seu ambiente local.

5. Próxima execução `heroku addons:add heroku-postgresql:hobby-dev`. [Isto](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) é o guia oficial do heroku sobre a criação de um postgres db lá. Você vai achar muito útil.

6. Em seguida, execute estes:

   ```
   heroku run python
   >> import os
   >> os.environ.get('DATABASE_URL')
   ```

7. O URL que você obtém dos comandos acima, é o seu *SQLALCHEMY_DATABASE_URI* no **config.py**. Coloque isso lá.

8. Em seguida, para configurar e migrar os modelos para o banco de dados, execute:

   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

9. Você pode achar [esta documentação](https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/) útil se você tiver problemas durante a configuração. Você *pode* precisar instalar o PostgreSQL em seu sistema se tiver alguns problemas na etapa acima. Verifique [isto](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) no guia oficial.

10. Em seguida, implante para o heroku com `git push heroku master`. E pronto!




###

### Estrutura de diretórios

1. DB_Wrappers: Contém as classes de wrapper para os modelos no banco de dados.
2. modules: Contém todas as funcionalidades, desde iniciar uma sessão de chat até enviar uma mensagem.
3. templates: Contém modelos de mensagens e webviews diferentes.






### Contribuições

Todas as contribuições são bem vindas. Por favor, discuta suas idéias sobre a comunidade primeiro para evitar o choque de outras pessoas trabalhando na mesma coisa. Algumas questões são marcadas como amigáveis para iniciantes, adequadas para quem está iniciando no ramo.

Faça perguntas se você não tiver certeza de alguma coisa. Felicidades!
