# BlindChat

A Facebook Messenger bot that allows users to chat with other people on Facebook anonymously. It's more like Omegle for Messenger, with some differences rather than improvements.



You can find it live [***here***](https://m.me/blindchat.go).





### A Bit of Background

I started out building BlindChat just to try out the messenger platform of Facebook and try to build something usable out of it and learning in the process. It is more of an app rather than an AI chatbot. The outcome got a bit of traction, hence I improved certain parts of it. But most of the code may be in an unorganized condition since those are built for quick prototyping.





### Local Development / Setup Your Version of the App

BlindChat is currently hosted on Heroku and also uses their offered database. So the code and setup are written for it. If you don't want to use Heroku, you'll have to modify a few parts. If you are okay with Heroku, then you are just fine. It's better to have a bit of a knowledge setting up a messenger bot.



1. Clone the repository. Open terminal/cmd and run `git clone https://github.com/mayukh18/BlindChat.git/` and set up your local repository.

2. Create a messenger app on Facebook. Add and configure the webhook and note down the *Access Token* and *Verify Token*. Put them in **config.py** in their respective places.

3. Create an app on Heroku. Open up terminal/cmd and run `heroku create yourappname`. You'll find the app url as `https://yourappname.herokuapp.com/`. Put it on **config.py**. Do note that you'll first have to install the *heroku CLI toolbelt* if you don't have it.

4. Next run `pip install -r requirements.txt`. This will install the libraries onto your local environment.

5. Next run `heroku addons:add heroku-postgresql:hobby-dev`. [This](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) is the official guide from Heroku on setting up a postgres db there. You'll find it pretty helpful.

6. Next run these:

   ```
   heroku run python
   >> import os
   >> os.environ.get('DATABASE_URL')
   ```

7. The url that you get from the above commands, that's your *SQLALCHEMY_DATABASE_URI* in **config.py**. Put it there.

8. Next, to set up and migrate the models into your database, run

   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

9. You may find [this memo](https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/) helpful if you run into problems during set up. You *may* need to install PostgreSQL on your system if you run into some issues in the above step. Check [this](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) on the official guide.

10. Next, deploy to Heroku with `git push heroku master`. And voila!




###

### Directory Structure

1. DB_Wrappers: Contains the wrapper classes for the models in the database.
2. modules: Contains all the functionalities from starting a chat session to sending a message.
3. templates: Contains different message templates and webviews.






### Contributing

All contributions are welcome. Please discuss your ideas on the community first to avoid clash of others working on the same thing. A few issues are marked as beginner friendly which are suitable for beginners to try out.

Ask about issues if you are not sure on something. Cheers!
