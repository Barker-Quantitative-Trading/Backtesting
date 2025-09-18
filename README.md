# Barker Quantitative Trading Club

**Hello Welcome to the Barker Quantitative Trading Club.
If you have access to this repo you are a very lucky person.**

Follow these steps to prep your machine and start contributing.

---

## Quick Setup (TL;DR)

1. Clone the repo (see below)
2. Create a Python virtual environment
3. Run the setup script: <br>
   #### Windows
   ```bash
   bash setup_windows.sh
   ```

   #### Linux
   ```bash
   bash setup_ubuntu.sh
   ```
4. Happy coding 🎉


## Detailed Setup

### Step 1 — Git Setup

If you don’t already have Git configured to interact with GitHub, follow the instructions down below or here:
👉 [Set up Git](https://docs.github.com/en/get-started/git-basics/set-up-git)
*(Recommended: use the HTTPS method.)*

<details>
  <summary>Git HTTPS Setup</summary>
  
  1. Make sure Git is installed:  
     - `git --version`  

  2. Configure your Git username and email:  
     - `git config --global user.name "Your Name"`  
     - `git config --global user.email "your_email@example.com"`  

  3. If prompted, log in with your GitHub username and password or use a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) instead of a password.  
</details>



<details>
  <summary>Git SSH Setup</summary>
  
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


### Step 2 — Clone the Repository

If you do not know how to clone yet please follow the command below or use the link to learn how to clone.

<details>
  <summary>Cloning</summary>
  
  > Clone by HTTPS: <br> 
     `git clone https://github.com/Barker-Quantitative-Trading/Backend.git`  

  > Clone by ssh: <br>
   `git clone git@github.com:Barker-Quantitative-Trading/Backend.git`
  
  [How to clone repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

</details>

### Step 3 — Create a Python Virtual Environment

Run:

```bash
python3 -m venv .venv
```

*(You can name the environment `env`, `.env`, `venv`, etc.)*

### Step 4 — Activate the Environment

#### Run:

Windows
```bash
source .venv/Scripts/activate
```

Linux
```bash
source .venv/bin/activate
```

*(Adjust the name if you used something other than `.venv`.)*

### Step 5 — Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

### Step 6 — Run the docker containers

Run:
```bash
cd docker
docker compose up -d
```

### Step 7 — Start Coding!

You’re all set. Read the contributing guide below.

---
Learn How to contribute by reading this document [Contributing Guidelines](./docs/CONTRIBUTING.md) or going to this link https://barker-quantitative-trading.github.io/Backend/ and reading the contribution section.
