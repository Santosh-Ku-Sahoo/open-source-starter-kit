# 🤝 Contributing to Open Source Starter Kit

Thank you for being here. Seriously. This is where your open source journey begins.

---

## 📋 Table of Contents

- [Before You Start](#before-you-start)
- [Setting Up Locally](#setting-up-locally)
- [Finding an Issue](#finding-an-issue)
- [Claiming an Issue](#claiming-an-issue)
- [File & Code Standards](#file--code-standards)
- [Raising a Pull Request](#raising-a-pull-request)
- [Review Process](#review-process)
- [Getting Unstuck](#getting-unstuck)

---

## Before You Start

1. **Star ⭐ this repo** — it helps others find it
2. **Read the README** — understand the structure
3. **Check existing PRs & issues** — don't duplicate work

---

## Setting Up Locally

```bash
# 1. Fork → then clone YOUR fork (not the original)
git clone https://github.com/YOUR_USERNAME/open-source-starter-kit.git

# 2. Navigate in
cd open-source-starter-kit

# 3. Add upstream remote (to stay updated with original repo)
git remote add upstream https://github.com/ORIGINAL_OWNER/open-source-starter-kit.git

# 4. Verify remotes
git remote -v
```

**Before starting any work, sync with upstream:**
```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## Finding an Issue

Go to the [Issues tab](../../issues) and filter by:

- `good first issue` → if it's your first time
- `help wanted` → maintainer needs someone on this
- `documentation` → great for non-coders too

> ⚠️ **Don't raise a PR without a linked issue.** If you want to add something new, open an issue first and discuss it.

---

## Claiming an Issue

Comment on the issue:
```
I'd like to work on this. ETA: 2-3 days.
```

Wait for a maintainer to assign it to you. **Don't start working until assigned** — someone else might be on it.

---

## File & Code Standards

### 📁 DSA Solutions
- One file per problem
- Filename: `problem_name.py` / `problem_name.js` / `ProblemName.java`
- Include at the top:
```python
# Problem: Two Sum
# Difficulty: Easy
# Approach: HashMap
# Time: O(n) | Space: O(n)
```
- Add 2-3 example test cases at the bottom

### 📁 Web Projects
- Self-contained folder with its own `README.md`
- Include: what it does, screenshot (if possible), how to run it

### 📁 Python Scripts
- Add a docstring at the top explaining what the script does
- Include `requirements.txt` if external libraries are used

### 📝 Documentation
- Clear headings
- No jargon without explanation
- Include examples wherever possible

---

## Raising a Pull Request

1. Push your branch
2. Go to GitHub → your fork → "Compare & pull request"
3. **Fill the PR template completely** — incomplete PRs will be closed
4. Link the issue: write `Closes #ISSUE_NUMBER` in the description
5. Add screenshots/output if relevant

### PR Title Format
```
feat: add binary search solution in Python
fix: correct off-by-one error in bubble sort
docs: add guide for setting up Git
```

---

## Review Process

- A maintainer will review within **3-5 days**
- You may be asked to make changes — that's normal, not rejection
- Once approved, your PR gets merged 🎉
- Your name goes in the contributors list automatically

---

## Getting Unstuck

Stuck on something? Don't ghost the issue.

- Comment on the issue explaining where you're stuck
- Check the `Documentation/guides/` folder
- Google the error message first
- Ask in the discussions tab

**No question is too basic here. This repo exists for beginners.**

---

*Happy contributing. Let's get those green squares. 🟩*
