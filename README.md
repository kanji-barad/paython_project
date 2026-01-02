git status
git add .
git commit -m "your message"
git push origin main
git push -u origin main

git commit -am "added" ==>both are one time add and coomit.

# Branch Command:-

main
 |
 |---- develop
 |       |
 |       |---- feature-1
 |       |---- feature-2
 |
 |---- hotfix

| Branch      | Purpose          |
| ----------- | ---------------- |
| `main`      | Production code  |
| `develop`   | Development code |
| `feature/*` | New features     |
| `hotfix/*`  | Bug fixes        |

# Branch Commands:-

git branch (check branch)
git branch -M main (to raname branch)
git checkout <-branch name-> (to navigate)
git checkout -b <-new branch name-> (to crate a new branch)
git branch -d <-branch name-> (to delete branch)
git push --set-upstream origin feture

# merging to branch code to 1:-

git diff <-branch name-> (to compare,commits,branches,files & more)
git merge <-branch name-> (using git) (to merge 2 branches)
# OR
Create a PR (using github)
