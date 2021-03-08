


function create() {
    cd /Users/jc/AutoProject
    source .env
    python create.py $1 # 建立資料夾
    python remove.py $1
    cd $FILEPATH$1 # 前往該資料夾
    touch README.md
    git init
    git add README.md
    git commit -m "Initial Commit"
    git remote add origin https://github.com/Cheng511/$1.git
    git push --set-upstream origin master
    code .
}