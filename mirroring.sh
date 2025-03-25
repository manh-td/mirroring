#!/bin/bash

# Step 1: Define the old repository URL and extract repo name
OLD_REPO_URL=$1 # Old repo URL passed as argument
echo "URL: $OLD_REPO_URL"

OLD_REPO_NAME=$(basename "$OLD_REPO_URL") # Extract repo name
echo "OLD_REPO_NAME: $OLD_REPO_NAME"

# Define GitHub username
GITHUB_USERNAME="your-mirror-to-username"
GITHUB_TOKEN="your-token-of-that-user"

NEW_REPO_URL="https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/${GITHUB_USERNAME}/${OLD_REPO_NAME}.git"

# Step 2: Authenticate with GitHub CLI (Make sure you're logged in)
if ! gh auth status &>/dev/null; then
    echo "🔴 GitHub CLI is not authenticated. Please run: gh auth login"
    exit 1
fi

# Step 3: Check if the new repository already exists
if gh repo view "${GITHUB_USERNAME}/${OLD_REPO_NAME}" &>/dev/null; then
    echo "✅ Repository '${OLD_REPO_NAME}' already exists on GitHub."
else
    # Step 4: Create a new GitHub repository
    echo "🛠️ Creating new repository: ${OLD_REPO_NAME}"
    gh repo create "${GITHUB_USERNAME}/${OLD_REPO_NAME}" --private --confirm
fi

# Step 5: Clone the old repository as a bare clone
echo "🔄 Cloning old repository: $OLD_REPO_URL"
git clone --bare "$OLD_REPO_URL" "$OLD_REPO_NAME"

# Step 6: Navigate into the cloned bare repository
cd "$OLD_REPO_NAME" || exit

# Step 7: Mirror-push to the new repository
echo "🚀 Pushing to new repository: ${NEW_REPO_URL}"
git push --mirror "$NEW_REPO_URL"

# Step 8: Navigate back to the previous directory
cd ..

# Step 9: Remove the temporary local repository
echo "🧹 Cleaning up temporary files..."
rm -rf "$OLD_REPO_NAME"

echo "✅ Repository successfully mirrored and temporary files removed."
