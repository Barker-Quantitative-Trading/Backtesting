# Barker Quantitative Trading Club

**Welcome!**
If you have access to this repo, you’re one of the lucky few 🚀.
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

If you don’t already have Git configured to interact with GitHub, follow the instructions here:
👉 [Set up Git](https://docs.github.com/en/get-started/git-basics/set-up-git)
*(Recommended: use the HTTPS method.)*

### Step 2 — Clone the Repository

Clone this repository onto your machine.
👉 [How to clone repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

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

You’re all set. Happy coding! 🚀🚀
