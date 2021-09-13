#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int read_string(char * buf, int size) {
	int i;
	for (i = 0; i < size; i++)
	{
		int c = getc(stdin);
		if(c == EOF || c == 0 || c == 0xa ) return i;
		buf[i] = c;
	}
	return i;
}

void read_flag(char * buffer, int len) {
	FILE * file = fopen("flag.txt", "r");
	fgets(buffer, len, file);
	fclose(file);
}

int main() {
	setbuf(stdout, NULL);

	char password[64];
	char username[64];
	char flag[64];

	printf("Enter username:\n");
	username[read_string(username, 64)] = 0;

	printf("Enter password:\n");
	password[read_string(password, 64)] = 0;

	read_flag(&flag, 64);

	if(!strcmp(username, "admin")) {
		if(!strcmp(password, flag)) {
			printf("Logged in!\n");
			printf("The flag is: %s\n", flag);
		}
	} else {
		printf("Invalid user %s\n", username);
	}
	
  	return 0; 
}
