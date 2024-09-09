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

- on your command-line, type:
```bash
git clone [paste url to repo]
```


- 'cd' (change directory) or enter the repository you just cloned by typing:
```bash
cd [repository name]
```

- all the content of the repo gets downloaded into your computer

- begin to make your changes

### Working inside a Repository

- type:
```bash
ls
```
in your command-line to see whats inside your repo, right now, no surprise that its empty as we are yet to create any files in there.

- create a new file on the terminal
```bash
touch hello.html
```
to create a new file titled 'hello.html'.

- create a boiller plate code of your html file.

- To save your changes, this is called commiting.

##### Git Add

- To stage your changes:
```bash
git add hello.html
``` 
to add a specific file, or 'git add .' to save all your changes.

- you may want to save only a specific file, whilst you are working on other files. just use:
```bash
git add [file name]
```

##### Git Commit

- to commit changes:
```bash
git commit -m [commit message]
```
 and type in a specific message of what exactly was the change that was made.

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

- to pull down the existing code state from the repository:
```bash
git pull
``` 
unto your branch/main or local branch on your computer.

- this may be changes other participants have made to the codebase, you do this in order to have the latest version, before you then begin to make your own changes.


### Merge Conflicts

- a git conflict happens when both origin and branch makes changes to the same part of the code, git doesnt know what to do when merging those two files and would depend on you to decide on which changes to keep or to combine them.

##### Common cases of merge conflicts

- if you have uncommited changes on your branch to which you are trying to pull into from origin.

- in your branch, if you have created a feature branch aside your main/branch, and made some changes to that feature branch, which you are then trying to merge with the main/branch, if on the main branch, you have also made changes to the same lines, then you will encounter a conflict and then decide what to keep or merge.

- if you have made changes to your origin, which you have not updated to your branch,  and you try to push up your own changes from branch to origin, then you wil necounter an error

- when resolving conflicts, everything between 
<<<<< Head
and
=====
are your changes, while everything between
=====
and
\>>>>> hash
are the remote changes on your github repo

- the hash is automatically generated everytime you make a commit and its used to refacture errors

- get rid of the markers and decide if you want to keep the remote changes, or the local changes or merge them

## Git Log

```bash
git log
```
is used to keep track of all the chnages youve made in detail


## Git reset

- Reverts to an older state of the repo:

```bash
git reset --hard commit [insert hash] 
```
to revert to a particular state

- to reset your local to your remote state on github:
```bash
git reset --hard origin/main
```

## Feature Branches

- you can create a branch for each feature in order to keep changes of each feature and switch to fix bugs

- you can switch between main branch and feature branches. this is known as the HEAD. the HEAD can be on a feature branch or on the main branch.

- you can then merge the feature back to the branch once satisfied.

- to see  what branch i am currently on, or where my HEAD is currently pointing:
 ```bash
git branch
```
this displays a list of all existing branches and also places a star in front of your current branch

- if i want to checkout an existing branch, or point HEAD to face an existing branch:
```bash
git checkout [branch name]
```

- if i want to checkout a new branch or create a new branch:
```bash
git checkout -b [new branch name]
```

- while you are on the new branch, make whatever changes you wil, and then add and commit those changes

- then switch to branch/main:
```bash
git checkout main
```
- while on branch/main, if you have made changes, then commit them before you can merge both changes,
 from feature/branch to main/branch:
 ```bash
 git merge [feature branch name]
 ```

 - if you have made changes to both feature and main/branches, on different lines, then git will attempt to automatically resolve those changes, otherwise you would be prompted to resolve them yourself.


 ## Forking a Repository

 - You fork open-source repository in order to make contributions.

 - on github you 'fork' or make a copy, make your changes or contributions or your on local branch and then make a pull request, which, if approved, is then added to the codebase on Github

 ## Github Pages

- Helps to quickly deploy websites

- to create a new github page. Go to github.com/new to create a new repository and give it a name: yourusername.github.io which is a convensional way of naming github pages. then finish creating the repository

- this initializes this repo as a github page

- clone the repository to your computer and make changes, commit them and push as usual

- this then creates a new web page which you can view from setting - github pages in github




