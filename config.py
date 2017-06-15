import os
basedir = os.path.abspath(os.path.dirname(__file__))

heroku_postgres = 'postgres://odfrnfyazxqqvb:16780da00e53f4c016919c59eccc443887a84f489c57d5ccd744ebdfc8cca33f@ec2-54-221-255-153.compute-1.amazonaws.com:5432/d8q1oi2ons93ei'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = heroku_postgres

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook (+ Wit)
ACCESS_TOKEN = 'EAAa5mZB0BiPEBAKc8eYx01AXMbzKiZCpgyjq7frKFd9DSwCTrvbKPkmgf3yD9HE6nO4aGcMoyAr5sZAAyOZAMUtP9vIQxyIeFtgVEo2WFpBWXSZB1F26CwHn7W5qZCmNpNljL8bcx3P9dOcbkkpUuMsgDMLuMSVCGbJVFK3KsBQrbOqM3DnIqe'
VERIFY_TOKEN = 'blind'



