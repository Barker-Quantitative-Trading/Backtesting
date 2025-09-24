# Contributing Guidelines

Thanks for your interest in contributing! 🎉  
Please follow these steps to keep our workflow clean and consistent.

---

1. **Clone the Repository** 
    - Clone the repository if you have not already.

2. **Create a new branch** 
    - Always create a new branch for your work (never work directly on main)
        - `git checkout -b feature/short-description`
        - feature/short-description is the name of the branch.
        - Generally you can create a new branch after each pull request and delete the old branch.

3. **Make changes** 
    - Write clean, well-documented code. 
    - If you are adding functionality, include tests. 
    - Run tests before committing. The command for running tests is `pytest` or clicking the run button in a test file.
    - All test files have to start with test.  Example: "test_feature.py"

4. **Commit and push** - 
    Make small, focused commits with clear messages.
    - git add .
    - git commit -m "Add feature: backtest strategy with momentum rules"
    - git push origin feature/short-description
    - It may say "To push the current branch and set the remote as upstream, use 
    git push --set-upstream origin feature_branch_name"
        - You need to do this when you first push.

5. **Submit a pull request(PR)** 
    - Go to the repository on GitHub.
    - Switch to your branch.
    - Click "New Pull Request".
    - Select your branch to merge into main.
    - In your PR description, explain: 
        - What your code does
        - Why the change is needed
        - How you tested it
    - Assign atleast one reviewer from this list
        - Ibrahim
        - Collin
        - Aneesha
        - Korben

6. **Merge into main** 
    - Review and fix all comments.
    - Ensure your branch is completely up to date with main to avoid any conflicts. To do this use command:
        - `git merge origin/main`
    - Once approved by a reviewer merge into main.

**Note** - 
    Be respectful and collaborative. Reviews and discussions are meant to improve the project, not criticize contributors.