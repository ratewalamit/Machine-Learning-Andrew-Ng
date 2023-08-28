directory="$HOME/my_web/Machine-Learning-Andrew-Ng/docs"
if [ -d "$directory" ]
then
    rm -r $directory
fi
#create website
make html
touch ./docs/.nojekyll
touch ./docs/index.html
echo '<meta http-equiv="refresh" content="0; url=./html/index.html" />' > ./docs/index.html
#Run local server
http-server -o ./docs/
