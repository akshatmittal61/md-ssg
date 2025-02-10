#!/bin/bash

# Define variables
IMAGE_NAME="my-mkdocs"
DOCKERFILE_PATH="."
CONTAINER_NAME="mkdocs-container"

GITIGNORE_EXCLUDES=$(cat .gitignore)
EXCLUDES_LIST=$(cat .excluded)

# Combine all exclusions
EXCLUDE_LIST="$GITIGNORE_EXCLUDES $EXCLUDES_LIST"

rm -rf site/ || true

# Check if the Docker image exists
if sudo docker image inspect $IMAGE_NAME > /dev/null 2>&1; then
    echo "Docker image '$IMAGE_NAME' exists. Removing it..."
    sudo docker rmi -f $IMAGE_NAME
else
    echo "Docker image '$IMAGE_NAME' does not exist. Skipping removal."
fi

echo "🚀 Building the Docker image..."
sudo docker build --build-arg EXCLUDE_FOLDERS="$EXCLUDE_LIST" -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Failed to build the Docker image. Exiting."
    exit 1
fi

mkdir -p site/

echo "📦 Running the MkDocs container..."
sudo docker run --name $CONTAINER_NAME --rm -v "$(pwd)/site:/app/site" $IMAGE_NAME

# Check if the container ran successfully
if [ $? -eq 0 ]; then
    echo "Docker container ran successfully. Check the 'site/' directory for the output."
else
    echo "Docker container failed to run. Check for errors."
    exit 1
fi

# echo "🧹 Cleaning up..."
sudo docker rmi $IMAGE_NAME

echo "✅ Done! Your generated site is available in the 'site/' folder."
