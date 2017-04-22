echo "Hello World! \a \n"
cd ..
cd speech

s=0  
i=1  
while [ "${i}" != "10" ]
do
	#split article to many part into folder name "1" or "2" ....，and cat every media in each folder into folder name "all"
	#finally cat all of media in folder "all"
	test -e ./${i} && cd ${i} || echo "Not exist"
	cat *.mp3 >> /Users/Wiz/Documents/project/t2v/speech/all/${i}.mp3
	pwd
	cd ..
	i=$(($i+1))
done

cd all
cat *.mp3 >> /Users/Wiz/Documents/project/t2v/speech/all.mp3

cd /Users/Wiz/Documents/project/t2v/code
python mail.py