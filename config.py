import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Facebook (+ Wit)
ACCESS_TOKEN = 'EAAEeqJxZBTtcBAG7PvMamwI68HZAdS562yR82eEtQIseUwJ5olIJ9rueBXSCxBvMZA575gYEZAL0yVEBE3ZC4AoI0bqWGhsKu6zeY740NFmoDePbeCHS7xClsVYY1fAVFKRbes17xlZA4SYJnsSjDEGIEUCjUu46f4b3TRxGZBypPwrnEHIsudL'
VERIFY_TOKEN = 'blind'



