import os
#basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = os.environ('DATABASE_URL')

#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook (+ Wit)
ACCESS_TOKEN = 'EAALec5ZCxX0kBAFTFqHyq5FlYzpUh1a3mLatb13f7IEopbVx04x8bmhmZBTIFXP1C6qJAZCZCLwXEcRvdqfLaI9ewX46kZABNVcgB2t54wiE1PgvZAnt0v4uMwY4egNZA8YsfMkYdo7IOcoSZBMQVphnwe8yxDePAZA80eRZAUyKl48Q18U89T8xLX'
VERIFY_TOKEN = 'blind'



