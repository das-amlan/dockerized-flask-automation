# CI/CD Workflow for Dockerized Flask App Using GitHub Actions
This project provides a comprehensive guide on utilizing GitHub Actions to automate workflows, including building, testing, and deploying applications, with a focus on integrating CI/CD pipelines.

## Workflow Overview

1. **Flask App**: The main application developed using the Flask framework.
2. **Unit Test**: Automated tests are run to ensure the application behaves as expected.
3. **Build and Test**: 
   - The CI (Continuous Integration) process builds the Docker image and runs the unit tests.
   - If the tests pass, the Docker image is prepared for deployment.
4. **Deploy**: 
   - The CD (Continuous Deployment) process deploys the Docker image to Docker Hub using secret keys for authentication.

## Prerequisites

- Docker
- GitHub account