# DockerNS - Docker Image Selector and Runner

## Overview

`dockerns.py` is a Python script that allows you to list all Docker images on your system, select one, and then run a container from the selected image. The script provides a simple command-line interface for managing Docker images and containers.

## Features

- **List Docker Images**: Displays all Docker images with their repository, tag, and ID.
- **Select Docker Image**: Prompts the user to select an image by number.
- **Run Container**: Starts a container from the selected image and opens a shell (`/bin/sh`) inside it.

## Prerequisites

- Python 3.x
- Docker installed and configured
- `sudo` privileges for running Docker commands

## Installation

1. **Clone the Repository** (if applicable):
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

Save the Script: Save the dockerns.py script to your desired location.
Usage
Make the Script Executable (optional):


chmod +x dockerns.py
Run the Script:

python dockerns.py
The script will list all Docker images.
You will be prompted to select an image by entering the corresponding number.
The script will then run a container from the selected image and open a shell (/bin/sh) inside it.
Managing Git Remotes
Viewing Remote URLs
To view the configured remote URLs for your Git repository:

git remote -v
This command will show you the fetch and push URLs for each remote. For example:

origin    https://github.com/Jkudjo/dockerns.git (fetch)
origin    https://github.com/Jkudjo/dockerns.git (push)
Adding Additional Remotes
To add a new remote, such as a Bitbucket remote:

git remote add bitbucket https://bitbucket.org/username/repository.git
Replace username with your Bitbucket username and repository with the name of your Bitbucket repository.

Updating Remote URLs
To update an existing remote URL:

git remote set-url origin https://new-url-for-your-repo.git
Replace origin with the name of the remote you want to update and https://new-url-for-your-repo.git with the new URL.

Pulling from and Pushing to Specific Remotes
Pull from GitHub:

git pull origin main
Pull from Bitbucket:

git pull bitbucket main
Push to GitHub:

git push origin main
Push to Bitbucket:

git push bitbucket main
Replace main with the branch name you are working with if it is different.

Example
$ python dockerns.py
Listing images...
1. ubuntu:latest 1234567890ab
2. nginx:latest 234567890abc
3. mysql:5.7 34567890abcd
Select an image by number: 2
Selected image: nginx:latest
Running container from image: nginx:latest
Troubleshooting
Docker Not Running: Ensure Docker is running and you have the necessary permissions.
Permission Denied: Make sure you have sudo privileges to run Docker commands.
Invalid Input: Ensure you enter a valid number when selecting an image.
License
This script is licensed under the MIT License.

Contributing
Feel free to submit issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.