echo 'angr to solve' $1

execut(){
	echo '(angr) wyf@node3:' $3'$ python3 ../bogus_argv_eval.py ' $1 $2
	python3 ../bogus_argv_eval.py $1 $2
}

path=$(pwd)
execut $1 1 $path
execut $1 2 $path
execut $1 3 $path
execut $1 4 $path

echo 'angr finish!'
