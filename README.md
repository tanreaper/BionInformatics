# Viral Host Classification tool for SARS-CoV-2 

This tool uses various Machine Learning Algorithms to identify different hosts for various coronavirus species using spike protein.

## Project Requirement
1. [Visual Studio Code](https://code.visualstudio.com/download)
2. [Python](https://www.python.org/downloads/)

## Setting up the project.

1. git clone https://github.com/tanreaper/BionInformatics.git
2. cd BionInformatics.
3. python3 ./app.py
4. It will start the basic flask development environment on http://127.0.0.1:5000/ or localhost:5000

## Setting up the git branches and working with it

1. The initial branch would be master branch
2. Create a new branch using **git checkout -b <yourname-dev> example: git checkout -b paul_dev**
3. Then run this command to track the git hub branch **git push --set-upstream origin <yourname-dev>**
4. The above command is run only once to set up the new branch
5. Any new changes must be staged **git add <filename>**
6. Then it is commited with **git commit -m "your commit message here"**
7. Then use **git push command** to push your changes from your local branch to remote branch
8. All the new changes pushed must be merged with pre-prod branch. 
9. Use **git checkout pre-prod** 
    



