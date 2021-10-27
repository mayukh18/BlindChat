# BlindChat

A Facebook messenger bot that allows users to chat with other people on Facebook anonymously.

You can find it live [***here***](https://m.me/blindchat.go).


#### NOTE: The app and the project is not maintained anymore. PRs will be unattended.


### A bit of a background

I started out building BlindChat just to try out the messenger platform of Facebook and to try to build something usable out of it while learning in the process. It is more of an app rather than an AI chatbot. The outcome got a bit of traction and hence I improved certain parts of it, however, most of the code may be in an unorganized condition since those are built for quick prototyping.





### Local development / Setup your version of the app

BlindChat is currently hosted on [Heroku](https://www.heroku.com/) and uses their offered database. Thus, the code and setup are written for it. If you don't want to use Heroku, you'll have to modify the code in a few places but if you are okay with Heroku, then you are just fine. It helps to have a bit of knowledge setting up a messenger bot.



1. Clone the repository by opening up your terminal/cmd and running the following command to set up your local repository:
   ```
   git clone https://github.com/mayukh18/BlindChat.git/
   ```

2. Create a messenger app on Facebook. Add and configure the webhook and be certain to note down both the *Access Token* and *Verify Token*. 

3. Install the *Heroku CLI toolbelt* if you don't already have it. Then create an app on Heroku by opening up your terminal/cmd and running the following command:
   ```
   heroku create yourappname
   ```
 
4. Run the following command to install the required libraries to your local environment:
   ```
   pip install -r requirements.txt
   ```

5. Run the following command to set up a Postgres database with Heroku:
   ```
   heroku addons:add heroku-postgresql:hobby-dev
   ```
- For more information, refer to the [official guide from Heroku](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) on setting up a Postgres database. You'll find it pretty helpful.

6. Next run the following lines:
   ```
   heroku run python
   >> import os
   >> os.environ.get('DATABASE_URL')
   ```
- The URL returned from running the above commands is your *SQLALCHEMY_DATABASE_URI*.

7. Open the **config.py** file and replace `'YOUR_FACEBOOK_APP_ACCESS_TOKEN'` and `'FACEBOOK_APP_VERIFY_TOKEN'` with the respective tokens from Step 2, replace `'APP_URL'` with your Heroku app URL `https://yourappname.herokuapp.com/` and finally, replace `'YOUR_DATABASE_URI'` with your database URI from step 6..

8. Next, to set up and migrate the models into your database, run
   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

9. Lastly, deploy to Heroku with the following command, and Voila!
   ```
   git push heroku master
   ```
   
**Note:**
- You may find [this memo](https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/) helpful if you run into problems while setting this up.
- You *may* need to install PostgreSQL on your system if you run into some issues in the above step. Check [this](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-windows) on the official guide.



### Directory structure

- DB_Wrappers: Contains the wrapper classes for the models in the database.
- modules: Contains all the functionalities from starting a chat session to sending a message.
- templates: Contains different message templates and webviews.



### Contributing

All contributions are welcome. Please discuss your ideas on the community first to avoid clash of others working on the same thing. A few issues are marked as "beginner friendly" which are suitable for beginners to try out.

Ask in Issues if you are not sure on something. Cheers!
