# Flask App Deployment to EC2 with GitHub Actions

This project demonstrates how to deploy a Flask application to an AWS EC2 instance using Docker and GitHub Actions for CI/CD. The app is containerized, pushed to GitHub Container Registry (GHCR), and then deployed to an EC2 instance.

## 📋 Overview

- **Application**: A simple Flask app running in a Docker container.
- **CI/CD Pipeline**: GitHub Actions automates the build, push, and deployment process.
- **Deployment Target**: AWS EC2 instance running Ubuntu.
- **Container Registry**: GitHub Container Registry (GHCR).

The pipeline triggers on every push to the `main` branch, builds a Docker image, pushes it to GHCR, and deploys it to EC2.

## 📦 Prerequisites

Before setting up the project, ensure you have the following:

- **AWS EC2 Instance**:
  - An Ubuntu-based EC2 instance with port 80 open (for HTTP access).
  - SSH access enabled (port 22).
  - Security group configured to allow inbound traffic on ports 80 and 22.

- **GitHub Repository**:
  - A GitHub repository with your Flask app code.
  - A `Dockerfile` in the root directory to build the app.

- **GitHub Secrets**:
  - `AWS_HOST`: The public IP or DNS of your EC2 instance.
  - `AWS_KEY`: The private SSH key (in PEM format) to access your EC2 instance.
  - `GHCR_TOKEN`: A GitHub Personal Access Token (PAT) with `read:packages` and `write:packages` scopes to access GHCR.

## 🛠️ Setup Instructions

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```
   git clone https://github.com/VoQuocTrunglaz/flask_app.git
   cd flask_app
   ```

2. **Configure GitHub Secrets**:
   - Go to your GitHub repository > **Settings** > **Secrets and variables** > **Actions**.
   - Add the following secrets:
     - `AWS_HOST`: Your EC2 instance's public IP or DNS.
     - `AWS_KEY`: Your EC2 private SSH key (copy the entire PEM file content).
     - `GHCR_TOKEN`: Your GitHub PAT with package read/write permissions.

3. **Set Up the EC2 Instance**:
   - Launch an Ubuntu EC2 instance on AWS.
   - Create a Key Pair (if you don’t have one): To access the EC2 instance via SSH, you need a key pair. If you don’t already have one, create it as follows:
        - Go to the EC2 dashboard in AWS.
        - Click on **Key Pairs** in the left sidebar.
        - Click on **Create Key Pair**.
        - Choose a name and select the file format (PEM for Linux/Mac, PPK for Windows).
        - Download the key pair file and keep it safe.
    - Configure the security group to allow inbound traffic on:
        - Port 22 (SSH) for GitHub Actions to connect.
        - Port 80 (HTTP) to access the Flask app.
4. **Add the GitHub Actions Workflow**:
   - The `.github/workflows/ci-cd.yml` file in this repository defines the CI/CD pipeline.
   - It builds the Docker image, pushes it to GHCR, and deploys it to EC2.
   - Ensure this file is in your repository’s `.github/workflows/` directory.

5. **Push to Trigger Deployment**:
   - Commit and push your changes to the `main` branch:
     ```
     git add .
     git commit -m "Initial commit"
     git push origin main
     ```
   - This will trigger the GitHub Actions workflow.

## 🚀 Usage

- **Access the App**:
  After the workflow completes, your Flask app will be running on the EC2 instance.
  - Open a browser and navigate to `http://<EC2_PUBLIC_IP>` (e.g., `http://ec2-xxx-xxx-xxx-xxx.compute-1.amazonaws.com`).
  - You should see the Flask app’s homepage.

- **Monitor the Workflow**:
  - Go to your GitHub repository > **Actions** tab to view the workflow logs.
  - Check for any errors during the build, push, or deployment steps.

## ⚠️ Troubleshooting

- **SSH Connection Issues**:
  - Ensure the `AWS_HOST` and `AWS_KEY` secrets are correct.
  - Verify that port 22 is open on your EC2 instance’s security group.
  - Check the SSH key permissions (`chmod 600` on the key file).

- **Docker Image Push Fails**:
  - Verify that the `GHCR_TOKEN` has the correct permissions.
  - Ensure you’re logged in to GHCR correctly in the workflow.

- **App Not Accessible**:
  - Confirm that port 80 is open on your EC2 instance.
  - Check the container logs on EC2:
    ```
    ssh -i <your-key.pem> ubuntu@<EC2_PUBLIC_IP>
    docker logs my-app
    ```