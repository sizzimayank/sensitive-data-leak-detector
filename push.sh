#!/usr/bin/env bash
set -e
REPO_NAME="sensitive-data-leak-detector"
echo "Initializing git repo..."
git init
git add .
git commit -m "Project 2: Sensitive Data Leak Detector — initial commit"
echo "Now create a GitHub repo named $REPO_NAME, then run:"
echo "git branch -M main"
echo "git remote add origin https://github.com/<your-username>/$REPO_NAME.git"
echo "git push -u origin main"
