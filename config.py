import os
basedir = os.path.abspath(os.path.dirname(__file__))

heroku_postgres = 'postgres://odfrnfyazxqqvb:16780da00e53f4c016919c59eccc443887a84f489c57d5ccd744ebdfc8cca33f@ec2-54-221-255-153.compute-1.amazonaws.com:5432/d8q1oi2ons93ei'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = heroku_postgres

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook (+ Wit)
ACCESS_TOKEN = 'EAAa5mZB0BiPEBAIAB9VxGwlDqWCZAxysh6i3mVd6avSAHjqOcyl7HE8BYZCNbtaOFGhlceE8XERGU1PxShRIJBeXEVuLMZAgZC9qenOBxgcuN2rnlUS3aDRw4HSFCuYIP5l30kJwYRZB24g1ZABQSgxcEWeBRyU3cTBhoYbxTSVQrcwlxNux1pF'
VERIFY_TOKEN = 'blind'

PAGE_ID = "320225391739538"
CHATMETRICS_TOKEN = "4b802f0db2aa4fd8c5f00355ee1d74f8fb4618fe"

ADMIN_ID = "1708022462556195"

