# OpaquePredicate without size constraints
The 'scripts' folder includes angr script and the 'testfiles' include the usercase that symbolic executed by scripts in 'scripts'.
We will introduce our algorithm by constructing opaque predicate without size constraints.
Because symboic execution tools such as angr can't solve the problem of symbolic memory, we define array a=[0,1,2,3,4,5,6,7,8,9] and nest variable nest_var=a[a[sym_var % 9 + 1]]. We should know that 'sym_var' is the variable that input by users. 
Then we construct type I opaque predicate, which is 'nest_var != sym_var % 9 + 1'. If symbolic execution can't solve this, it will recognize this opaque predicate as normal predicate. We construct type II opaque predicate, which is  'nest_var != sym_var%9 && sym_var==7', based on existing sentence 'sym_var==7'. If symbolic execution fails to know that 'nest_var != sym_var%9' is always true if sym_var is 7. Therefore, we can say that opaque predicate cant resist symbolic execution.

By the way, 'without size constraints' means the query results will not change by the size of symbolic variable. No matter what the size of symbolic variable, symbolic execution solver can't get the correct value. 
