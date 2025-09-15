**Hello Welcome to the Barker Quantitative Trading Club.
If you have access to this repo you are a very lucky person.**

If you are wanting to help development please read through this file to know what to do to prep your 
machine so you can get started

Step 1
--
If you do not have git setup so that you can interact with github please set it up with the commands below in terminal. It is recommended to follow this method.
## Setup Guide

<details>
  1. Enter command:
     - `ssh-keygen -t ed25519 -C "your_email@example.com"`
     - Press enter for all prompts

  2. Copy your public key:
     - `pbcopy < ~/.ssh/id_ed25519.pub`

  3. Add SSH key to GitHub:
     - Go to [this page](https://github.com/settings/keys)
     - Click **"New SSH Key"**
     - Paste the copied key and save

  4. Verify your connection:
     - `ssh -T git@github.com`
</details>

Step 2
--
Clone Repostiory onto your machine.
If you do not know how to clone yet please follow the command below or use the link to learn how to clone.
> - Command:
        - git clone git@github.com:Barker-Quantitative-Trading/Backend.git
> - [How to clone repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

Step 3
--
Create a python virtual enviroment
> python3 -m venv env <sub> (env is the name of the environment. You can change this to .env, .venv, or venv) </sub>

Step 4
--
Start the environment
> source env/bin/activate <sub> (If you changed the name of the enviornment in the previous step reflect it in this command.) </sub>

Step 5
--
Use the command below to install all necessary libraries
> pip install -r requirements.txt

Step 6
--
Happy Coding! :rocket: :rocket:


