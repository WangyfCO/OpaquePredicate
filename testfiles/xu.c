#include <stdio.h>
#include<malloc.h>
#include <stdlib.h>
#include<string.h>
void bogus() {
	printf("Bogus\n");
}
void foo() {
	printf("Foo\n");
}
int test(int symvar) {
	int j = symvar;
	int l1_ary[]={1,2,3,4,5,6,7};
	int l2_ary[]={j,1,2,3,4,5,6,7};
	int i=l2_ary[l1_ary[j %7]];
	if(i== j) 
		bogus();
	if(i ==1 && j==7)
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
