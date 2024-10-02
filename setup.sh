#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to prompt for user input
prompt() {
    read -p "$1: " input
    echo $input
}

# Create a messenger app on Facebook and configure the webhook
echo "Please create a messenger app on Facebook and configure the webhook."
ACCESS_TOKEN=$(prompt "Enter your Facebook App Access Token")
VERIFY_TOKEN=$(prompt "Enter your Facebook App Verify Token")

# Install the required libraries
echo "Installing required libraries..."
pip install -r requirements.txt

# Set up a local PostgreSQL database
echo "Setting up a local PostgreSQL database..."
DATABASE_URL=$(prompt "Enter your local PostgreSQL database URI (e.g., postgresql://username:password@localhost:5432/mydatabase)")

# Update .env file with the necessary tokens and URLs
echo "Updating .env file with the necessary tokens and URLs..."
cat <<EOT > .env
SQLALCHEMY_DATABASE_URI=$DATABASE_URL
ACCESS_TOKEN=$ACCESS_TOKEN
VERIFY_TOKEN=$VERIFY_TOKEN
APP_URL=http://localhost:5000
CHATMETRICS_TOKEN=$(prompt "Enter your Chatmetrics Token")
PAGE_ID=$(prompt "Enter your Facebook Page ID")
ADMIN_ID=$(prompt "Enter your Admin ID")
EOT

# Set up and migrate the models into the database
echo "Setting up and migrating the models into the database..."
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Local deployment
# echo "Starting the application locally..."
# FLASK_APP=manage.py flask run --host=0.0.0.0
# python manage.py runserver --host 0.0.0.0 --port 5000 &

# Instructions for manual deployment on your own server
echo "To deploy on your own server, follow these steps:"
echo "1. Ensure you have a PostgreSQL database set up and accessible from your server."
echo "2. Copy the .env file to your server and update the DATABASE_URL with your server's database URI."
echo "3. Install the required libraries on your server by running 'pip install -r requirements.txt'."
echo "4. Set up and migrate the models into the database by running 'python manage.py db init', 'python manage.py db migrate', and 'python manage.py db upgrade'."
echo "5. Start the application on your server by running 'python manage.py runserver --host 0.0.0.0 --port 5000'."

echo "Setup complete! Your app should be running locally. Follow the instructions above to deploy on your own server."