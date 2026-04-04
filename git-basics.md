# 🧰 Git Basics — Everything You Actually Need

> No fluff. Just the commands you'll use 90% of the time.

---

## What is Git?

Git is a tool that tracks changes in your code. Think of it like "Ctrl+Z for your entire project, forever."

GitHub is just Git + the internet. Your code lives online, others can see it, and you can collaborate.

---

## The Core Workflow

```
Your Computer                     GitHub
    │                               │
    │──── git clone ───────────────>│  (download the repo)
    │                               │
    │  (make changes)               │
    │                               │
    │──── git add . ────────────>   │  (stage changes)
    │──── git commit -m "msg" ──>   │  (save snapshot)
    │──── git push ─────────────>   │  (upload to GitHub)
```

---

## Commands You'll Use Daily

### Setup (one time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

### Clone a repo
```bash
git clone https://github.com/username/repo-name.git
```

### Check status (use this constantly)
```bash
git status
```

### Create a new branch
```bash
git checkout -b your-branch-name
```

### Stage and commit changes
```bash
git add .                          # stage everything
git add specific-file.py           # stage one file
git commit -m "feat: add two sum"  # commit with message
```

### Push your branch
```bash
git push origin your-branch-name
```

### Update your local copy
```bash
git pull origin main
```

---

## Common Mistakes & Fixes

### "I committed to main by accident"
```bash
git checkout -b new-branch-name    # create new branch with your commits
git checkout main
git reset --hard HEAD~1            # undo last commit on main
```

### "My branch is behind main"
```bash
git checkout main
git pull upstream main
git checkout your-branch
git rebase main
```

### "I have merge conflicts"
Open the conflicting file. Look for:
```
<<<<<<< HEAD
your changes
=======
their changes
>>>>>>> main
```
Delete the markers, keep what's correct, save the file, then:
```bash
git add .
git commit -m "fix: resolve merge conflict"
```

---

## Commit Message Cheatsheet

```
feat:     → new feature or solution
fix:      → bug fix
docs:     → documentation
chore:    → cleanup, formatting
refactor: → code improvement (no new feature)
test:     → adding tests
```

---

*That's honestly 95% of what you need. The rest you'll pick up as you go.*
