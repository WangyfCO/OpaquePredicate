#include <stdio.h>
#include<malloc.h>
#include <stdlib.h>
#include<string.h>
int Bogus(int m,int n ) {
	printf("Bogus,nest_var=%d,sym_var=%d\n",m,n);
	return (m+1)*n;
}
void Foo() {
	printf("Foo\n");
}
int test(int j) {
	int sym_var = j;
	int nest_var,a[10];
	a[0]=0;a[1]=1;a[2]=2;a[3]=3;a[4]=4;a[5]=5;a[6]=6;a[7]=7;a[8]=8;a[9]=9;
	nest_var = a[a[sym_var % 9 + 1]];
	if (nest_var != sym_var % 9 + 1){
		int res;
		res=Bogus(nest_var,sym_var);
		if(res>1)
			printf("win");
	}
	if(nest_var != sym_var%9 && sym_var==7)
		Foo();
	return 0;
}
int main(int argc, char** argv) {
	int k=0;
	for(int i=0;i<strlen(argv[1]);i++){
		printf("%c\n",argv[1][i]);
		int m=argv[1][i];
		k=k*256+m;
		
	}
	test(k);
}
