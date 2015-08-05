#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 80
#define BUFFER_SIZE 50

char errormess[50] = "Error\n";
char history[10][BUFFER_SIZE];
int count = 0;
int caught = 0;

void printHistory() {
    printf("%s\n","History...\n");
    int i;
    int j = 0;
    int historycount = count;
    if (historycount == 0)
        printf("No history");
    else {
        for (i = 0; i<10;i++) {
            printf("%d ", historycount);
            while (history[i][j] != '\n' && history[i][j] != '\0') {
                printf("%c", history[i][j]);
                j++;
            }
            printf("\n");
            j = 0;
            historycount--;
            if (historycount ==  0)
                break;
            }
        }
        return;
        printf("\n");
}
void setup(char inputBuffer[], char *args[],int *background) {
    int length, i, start, ct;
    ct = 0;
    length = read(STDIN_FILENO, inputBuffer, MAX_LINE);
    start = -1;
    if (caught == 1) {
        length = read(STDIN_FILENO, inputBuffer, MAX_LINE);
        caught = 0;
    }
    if ((strstr(inputBuffer, "history") == NULL) && (strstr(inputBuffer, "!") == NULL)){
        for (i = 9;i>0; i--){
            memset(history[i], 0, BUFFER_SIZE);
            strncpy(history[i], history[i-1], BUFFER_SIZE);
        }
    strcpy(history[0],inputBuffer);
    count++;
    }
    if (length == 0 || strstr(inputBuffer, "exit") != NULL)
        exit(0);
    else if (length < 0) {
        write(STDERR_FILENO, errormess, strlen(errormess));
        exit(-1);
    }
    for (i=0;i<length;i++) {
        switch (inputBuffer[i]) {
            case ' ':
            case '\t' :
                if(start != -1) {
                    args[ct] = &inputBuffer[start];
                    ct++;
                }
                inputBuffer[i] = '\0';
                start = -1;
                break;
            case '\n':
                if (start != -1) {
                    args[ct] = &inputBuffer[start];
                    ct++;
                }
                inputBuffer[i] = '\0';
                args[ct] = NULL;
                break;
            case '&':
                *background = 1;
                inputBuffer[i] = '\0';
                break;
            default:
                if (start == -1)
                    start = i;
                else if (inputBuffer[i] == '&') {
                    *background  = 1;
                    inputBuffer[i] = '\0';
                
            }
        }
    }
    args[ct] = NULL;
}
int main(void) {
    char inputBuffer[MAX_LINE];
    int background;
    char *args[MAX_LINE/2 +1];
    pid_t pid;
    int i;
    int should_run = 1;
    while (should_run) {
        background = 0;
        printf("\nosh> ");
        fflush(stdout);
        setup(inputBuffer,args,&background);
        pid = fork();
        if (pid < 0) {
            printf("Bad fork\n");
            exit (1);
        }
        else if (pid == 0) {
            if (strcmp(args[0], "!") == 0) {
                int n = atoi(&args[0][1]);
                n = count - n;
                if((strcmp(history[n], "") != 0) && n <= count) {
                    char *temp[MAX_LINE/2+1];
                    temp[0] = strtok(history[n], " \n");
                    int i = 0;
                    while (temp[i] != NULL){
                        temp[i+1]= strtok(NULL, " \n");
                        i++;
                    }
                    if (execvp(temp[0], temp) == -1) {
                        printf("Error bro. Check ya commands. And probably my code.\n");
                        
                    }
                }
                else {
                    printf("I've got nothing.");
                }
                exit(0);
            }
            else if (strcmp(args[0], "!!") == 0) {
                if (strcmp(history[0], "") !=0){
                    char *temp[MAX_LINE/2+1];   
                    temp[0] = strtok(history[0], " \n");
                    int i = 0;
                    while (temp[i] != NULL){
                        temp[i+1] = strtok(NULL, " \n");
                        i++;
                    }
                
                    if (execvp(temp[0], temp)==-1){
                        printf("Error while executing command\n");
                        
                    }
                }
            }
            else if (strcmp(args[0], "history") == 0) {
                printHistory();
                exit(0);
            }
            else if (execvp (args[0], args) == -1) {
                printf("Invalid command\n");
            }
        }
        if (background == 0) {
                wait(NULL);
        }
    }
    return 0;
}