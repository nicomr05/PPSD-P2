#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>


typedef struct {
    char *ERROR;
    char *CONSOLE;
} colors;


char *formatKey(char *key){
    int keyLength = strlen(key);

    if ( !(1 <= keyLength <= 26) ){
        perror("Key must be between 1 and 26 characters long.");
    }

    for (int i; i < keyLength; i++){    // Hacer que strchr busque en el alfabeto y devuelva un puntero a un caracter que no esté en él
        if ( NULL ){
            perror("The character %c is not valid.\n", key[i]);
        }
    }
}


int main(int argc, char *argv[]){
    colors *bcolors = malloc(sizeof(colors));
    bcolors -> ERROR = "\033[31m";
    bcolors -> CONSOLE = "\033[33m";


    if (argc > 4) {
        printf("%sERROR%s : \n");
    }
    

    return 0;
}
