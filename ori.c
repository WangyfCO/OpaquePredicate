#include <stdio.h>
#include<malloc.h>
#include <stdlib.h>
#include<string.h>
void foo() {
	printf("Foo\n");
}
int test(int symvar) {
	int j = symvar;
	if(j==7)
		foo();
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
