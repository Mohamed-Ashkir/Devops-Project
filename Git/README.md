Git doesn’t only store code it is the  foundation of how modern teams collaborate, build, test, ship, and even recover when someone breaks production at 2 am for example. 

# Version control

It is a systems that tracks changes to your code over time; this helps you undo your mistakes, see what changed and collaborate with other teams. 

# CVS & SVN vs GIT

Concurrent Versions systems (CVS) and Apache Subversion (SVN) are older and centralized version control systems that software development teams used to track changes to code and collaborate on projects. Cons - single server everyone used and if it went down, game over. 

GIT- created 2005 by Linus Torvalds, he wrote his own version control system that made sure every developer has a full copy of the repo with the entire history. It’s fast, works offline and it built for the chaos of real-world collaboration. 

# Core concepts

- Repository- it is a digital project folder where you store code, file and the entire history of the project
- Commit- **saved snapshot of your project's files** at a specific point in time.
- Branch - **separate, safe workspace** where you can change your code without affecting the main project.
- Staging area- **a temporary prep zone where you choose exactly which code changes are ready to be saved in your next commit**.
- Index- file that hold the staging area info

# .git directory

!image.png

- The .git directory- The hidden brain of the project that stores all history, settings and tracking data. Without it, git forgets everything and you won’t no history, no tracking code and no safety net for your project.
- refs/ store info about branches and tags
- objects/ knows every commit
- config- holds project specific settings
- HEAD- pointer that tells git which branch or commit you are currently looking at
- index- staging area

# Common commands

**Setup & Creation**

- **`git init`:** Creates a new, blank `.git` folder to start tracking your project.
- **`git config`:** Sets up your identity like your name and email address.
- **`git clone`:** Downloads an existing project from GitHub onto your computer.

**The Saving Workflow**

- **`git add`:** Moves your new changes into the staging prep zone.
- **`git commit`:** Saves your staged changes permanently as a timeline snapshot.

**Checking Your Work**

- **`git status`:** Shows which files are changed, staged, or untracked right now.
- **`git diff`:** Shows the exact line-by-line differences of what you changed.
- **`git log`:** Displays the history list of all your past saves (commits).

**Managing Files & Undoing**

- **`git rm`:** Deletes files from your project and stops tracking them.
- **`git mv`:** Renames or moves a file to a new folder.
- **`git restore`:** Erases your recent edits and resets a file back to its last saved state.
- **`git help <command>`:** Opens up the built-in manual to explain how a command works.

# Branching

Branching lets you work on multiple things without messing up your main project 

Basic commands

- Git branch: used to list and create branches
- Git checkout -b <branch>: used to create & switch (note: this is an older sytanx )
- git switch -c <branch>: modern version used to create and switch
- git switch <branch>: switch branches safely
- Git branch -d <branch>: delete branch

USED FOR- isolate work and manage collaboration without breaking live application 

 
# Merging

Merging is taking work from a branch and putting it back into the main project

Common commands

- git merge <branch>: used to merge a specific branch and put into your current branch
- fast-forward merge: just moves the branch pointer forward. No new commit is created.
- Recursive merge: combining two timelines together that two or more people made different changes at the same time.

# Rebase

Git rebase rewrites history by moving your feature branch’s commit to the very top of the branch which then creates completely flat line (linear).  Pros your history is clean and readable and cons dangerous when used on shared/public branches. 

# Git stash & Pop

git stash is used to temporary save uncommitted changes- basically it puts your half-finished work in a safe place 

Git pop- used to pull the half-finished work back so you can start working on it

# Fork & Pull request

Fork: a copy of someone else’s repo

Pull request(pr): a formal request asking the project owner to review your work and merge changes into their official project codebase
