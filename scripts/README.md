This folder contains six files.
'bogus_argv_eval.py' means the angr solver program, and it can find the symbolic variable's value that direct to 'Bougs' path.
'bogus_argv.sh' is the shell script,it calls 'bogus_argv_eval.py' by specifing the size of symbolic variable.
'foo_argv_eval.py' means the angr solver program, and it can find the symbolic  variable's value that direct to 'Foos' path.
'foo_argv.sh' is the shell script,it calls 'foo_argv_eval.py' by specifing the size of symbolic variable.
'debogus.py' is the program of bogus control flow removal,which is written by [1].
'debogus_length.py' is the program of bogus control flow removal too, which is rescripted by me. It can specify the size of symbolic variable.
note:[1] https://github.com/bluesadi/debogus.
