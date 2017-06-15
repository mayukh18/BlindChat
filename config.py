import os
basedir = os.path.abspath(os.path.dirname(__file__))

heroku_postgres = 'postgres://odfrnfyazxqqvb:16780da00e53f4c016919c59eccc443887a84f489c57d5ccd744ebdfc8cca33f@ec2-54-221-255-153.compute-1.amazonaws.com:5432/d8q1oi2ons93ei'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = heroku_postgres

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook (+ Wit)
ACCESS_TOKEN = 'EAABZCQJwUs0MBAKlepUHqykzb4UZClhMcJTga11ik7ucikFfEZBdG7vLxa3kbjTuIeD0oiob7ZASHDHlzqDrFRDLY5Lb4Oktb8cp7S6ZAeDQ3YHIXpMMZCCYs59tW1VmXP4tIHuWKN0ZBhgV9i3ZA00QFeIacKLmGfWrUXMqmLOIZAnz6DRbfW75A'
VERIFY_TOKEN = 'blind'



