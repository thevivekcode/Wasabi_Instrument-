# Trace Size
# Program Name
# Program Arguments

wasm-objdump -d $2.wasm > $2.objdump.txt
python extractBaseAddress.py $2.objdump.txt
cp log-all.js master.js
sed -i '1ivar trace_size='${1}';' master.js
echo "<html><body></body></html>" > $2.html
path=$(echo $2| awk -F/ '{$NF=""}1' | tr -s '[:blank:]' '/')
filename=$(echo $2|awk -F/ '{print $NF}')
awk '{gsub(/<\/body\>/,"\ \ \n\n<\/body\>")}1' $2.html >$2.bak
mv $2.bak $2.html
mv master.js ${path}
wasabi $2.wasm ${path}out
mv $2.wasm $2.orig.wasm
cp ${path}out/* ${path}
arg=$(echo $2 | awk '{gsub(/\//,"\\/",$0)}1')
sed -i '/<body>/a <script async src="'${filename}'.js"></script>' $2.html
sed -i '/<script async src="'${filename}'.js"><\/script>/a <script src="'${filename}'.wasabi.js"></script>' $2.html
sed -i '/<script src="'${filename}'.wasabi.js"><\/script>/a <script src="master.js"></script>' $2.html
python PythonX86Mapper.py $1 $2
rm -r ${path}out
rm $2.wasabi.js $2.objdump.pickle $2.objdump.txt $2.html $2.wasm
mv $2.orig.wasm $2.wasm
mv $2.gz .
rm ${path}master.js
