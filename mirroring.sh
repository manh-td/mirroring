#!/bin/bash

# Step 1: Define the old and new repository URLs
OLD_REPO_URL=$1 # Replace with your old repo URL
echo "URL: $OLD_REPO_URL"
OLD_REPO_NAME=$(basename "$OLD_REPO_URL") # Extract repo name from URL
echo "OLD_REPO_NAME: $OLD_REPO_NAME"
NEW_REPO_URL="https://smu.manhtd:<github-token>@gitlab.com/smu.manhtd/$OLD_REPO_NAME.git" # Replace with your new repo URL

# Step 2: Clone the old repository as a bare clone
echo "CMD: git clone --bare $OLD_REPO_URL"
git clone --bare "$OLD_REPO_URL" $OLD_REPO_NAME

# Step 3: Navigate into the cloned bare repository directory
echo "CMD: cd "$OLD_REPO_NAME" || exit"
cd "$OLD_REPO_NAME" || exit

# Step 4: Mirror-push to the new repository
echo "CMD: git push --mirror $NEW_REPO_URL"
git push --mirror "$NEW_REPO_URL"

# Step 5: Navigate back to the previous directory
cd ..

# Step 6: Remove the temporary local repository
echo "Removing temporary files..."
rm -rf "$OLD_REPO_NAME"

echo "Repository successfully mirrored and temporary files removed."
