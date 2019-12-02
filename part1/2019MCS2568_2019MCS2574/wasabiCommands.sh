# optimization 1
# parent folder path2
# file path3
# output file name hello
# js file name5
# port
# browser

#The following commands are the same commands from the documentation of Wasabi
emcc -$1 -I ../utilities/ -I $2 ../utilities/polybench.c  --emrun -s WASM=1 -s ALLOW_MEMORY_GROWTH=1 ../$3 -o $4.html
wasabi $4.wasm ./${4}_out/
mv $4.wasm $4.orig.wasm
cp ./${4}_out/* .
#Whenever optimization flags -O3,-O2,-O1 are added, the html file created is unable to add the scripts called in sed command properly inside the body. So this awk 
#command is used to forcibly add script tags inside body by giving new lines before body tag
awk '{gsub(/<\/body\>/,"\ \ \n\n<\/body\>")}1' $4.html >$4.bak
mv $4.bak $4.html
sed -i '/<script async src='${4}'.js><\/script>/a <script src="'${4}'.wasabi.js"></script>' $4.html
sed -i '/<script async type="text\/javascript" src="'${4}'.js"><\/script>/a <script src="'${4}'.wasabi.js"></script>' $4.html
sed -i '/<script src="'${4}'.wasabi.js"><\/script>/a <script src="'${5}'"></script>' $4.html
