**Hello Welcome to the Barker Quantitative Trading Club.
If you have access to this repo you are a very lucky person.**

If you are wanting to help development please read through this file to know what to do to prep your 
machine so you can get started

Step 1
--
If you do not have git setup so that you can interact with github please set it up with the commands below in terminal. It is recommended to follow this method.
> Enter command: 
    > ssh-keygen -t ed25519 -C "your_email@example.com" (replace your_email@example.com with your email)
> Press enter for all prompts
> Enter command:
    > pbcopy < ~/.ssh/id_ed25519.pub (you should be able to paste the key now)
> Go to [this](link https://github.com/settings/keys) webpage to setup an ssh key
    > click "New SSH Key"
    > Add whatever title you would like
    > Paste the key that was saved into the Key box and then click "Add SSH Key"
> Now verify your connection by entering the command:
    > ssh -T git@github.com
    > You may be asked if you are sure you want to continue to connect. Follow the prompts to continue.
    > This should print "Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access."

Step 2
--
Clone Repostiory onto your machine.
If you do not know how to clone yet please follow the command below or use the link to learn how to clone.
> Command:
    > git clone git@github.com:Barker-Quantitative-Trading/Backend.git
> [How to clone repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

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


