directory="$HOME/my_web/Machine-Learning-Andrew-Ng/docs"
if [ -d "$directory" ]
then
    rm -r $directory
fi

make html
touch ./docs/nojekyll
http-server -o ./docs/html/
