import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Database setup
SQLALCHEMY_DATABASE_URI = 'YOUR_DATABASE_URI'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook
ACCESS_TOKEN = 'YOUR_FACEBOOK_APP_ACCESS_TOKEN'
VERIFY_TOKEN = 'FACEBOOK_APP_VERIFY_TOKEN'

# App url
APP_URL = 'APP_URL'

# For analytics purposes
CHATMETRICS_TOKEN = 'CHATMETRICS_TOKEN'

# For debugging
PAGE_ID = 'FACEBOOK_PAGE_PSID'
ADMIN_ID = "ADMIN_PSID"

