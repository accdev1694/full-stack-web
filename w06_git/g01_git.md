# Git

## What is git?

- Git is a command-line application that helps us to version-control or our work, keeping track of changes we make to code.

- we can easily refference chnages made to our code at different points in time

- helps us to synchronize code between different people

- You push your changes to the github server and pull other people's changes from github servers

- Test changes to your code on a seperate branch before merging to your main code on your local computer

- Revert back to previous versions of your code

## GitHub

- A server website for hosting or storing our code

- create a new Github account on github

- to create a new repository, go to github.com/new

- give the Repo a Name, Description, make Public or Private, Initialize with a ReadMe and add a Licence

- Go ahead a create a repo, check out the instructions

### Cloning a Repository

- on the newly created repository, select 'clone' and get the url of the repository using the 'https' link or 'ssh' if you are familiar with that option

- on your command-line, type 'git clone' and paste the url to that repository

- 'cd' (change directory) or enter the repository you just cloned by typing 'cd [repository name]

- all the content of the repo gets downloaded into your computer

- begin to make your changes

### Working inside a Repository

- type 'ls' in your command-line to see whats inside your repo, right now, no surprise that its empty as we are yet to create any files in there.

- create a new file on the terminal by using 'touch hello.html' to create a new file titled 'hello.html'.

- create a boiller plate code of your html file.

- To save your changes, this is called commiting.

##### Git Add

- To stage your changes, 'git add hello.html' to add a specific file, or 'git add .' to save all your changes.

- you may want to save only a specific file, whilst you are working on other files. just use git add [file name].

##### Git Commit

- to commit changes, " 'git commit -m 'commit message' ", and type in a specific message of what exactly was the change that was made.

##### Git add and commit shortcut

- to git add and git add at the same time use 'git commit -am "commit message" '

##### Git Push

- to update or push your changes up to github, use 'git push'.

##### Git Status

- use 'git status' to see exactly what is going on inside your repository.

- if you check your repo on github you will see that your commits have reflected. You have one branch by default after cloning you repo. That default branch is called 'master' or 'main'.

##### Origin/Main vs Branch/Main

- Origin main is your git repository, where your repo originated from

- Branch main is your local cloned codebase on your computer

##### Git Pull

- you 'git pull' to pull down the existing code state from the repository, unto your branch/main or local branch on your computer.

- this may be changes other participants have made to the codebase, you do this in order to have the latest version, before you then begin to make your own changes.


### Merge Conflicts

- a git conflict happens when both origin and branch makes changes to the same part of the code, git doesnt know what to do when merging those two files and would depend on you to decide on which changes to keep or to combine them.

##### Common cases of merge conflicts

- if you have uncommited changes on your branch to which you are trying to pull into from origin.
