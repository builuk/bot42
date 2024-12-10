#!/bin/bash


cd /path/to/your/project

git pull

pip install -r requirements.txt

sudo systemctl restart your-app.service

echo "Deployment completed successfully."
