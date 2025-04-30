#!/bin/bash

# Set default values
PROJECT_ID="uplifted-air-411914"  # Replace with your project ID
DOCKERHUB_USERNAME="malikakb"
REPO_NAME="demo-project"

# Ask for branch/tag to test
echo "Enter the Git branch or tag (e.g., v1.0, main):"
read TAG_NAME

# Run Cloud Build using the provided TAG_NAME
echo "Running Cloud Build for TAG_NAME=$TAG_NAME..."

# Run the Cloud Build
gcloud builds submit --config=cloudbuild.yaml --substitutions=_TAG_NAME="$TAG_NAME" --project="uplifted-air-411914" .

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "Build succeeded for TAG_NAME=$TAG_NAME!"
else
    echo "Build failed for TAG_NAME=$TAG_NAME. Check logs for details."
fi

# Optionally, run for additional tags or branches
echo "Do you want to test another branch/tag? (y/n)"
read CONTINUE

if [ "$CONTINUE" == "y" ]; then
    ./test_cloudbuild.sh  # Re-run the script if the user wants to test more
else
    echo "Exiting script."
    exit 0
fi

