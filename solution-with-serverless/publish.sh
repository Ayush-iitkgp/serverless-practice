#!/bin/bash

set -e

echo "Building..."

docker build \
-t test:latest .

ECR_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URI
# $(aws ecr get-login-password)
IMAGE_REPO_URI=$ECR_URI/$APPLICATION_NAME-$ENVIRONMENT_NAME:latest
echo "${IMAGE_REPO_URI}"
docker tag test:latest $IMAGE_REPO_URI
aws ecr describe-repositories --repository-names $APPLICATION_NAME-$ENVIRONMENT_NAME || aws ecr create-repository --repository-name $APPLICATION_NAME-$ENVIRONMENT_NAME
docker push $IMAGE_REPO_URI

echo "IMAGE_REPO_URI=$IMAGE_REPO_URI" >> .env
