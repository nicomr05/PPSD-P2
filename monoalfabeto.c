#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>


typedef struct {
    char *ERROR;
    char *CONSOLE;
} colors;


char *formatKey(char key[]){
    int keyLength = strlen(key);
    char alphabet[] = "ABCDEFGHIJKLMNOPQRTSUVWXYZ";

    if ( !(1 <= keyLength <= 26) ){
        perror("Key must be between 1 and 26 characters long.");
        return 1;
    }

    for (char *keyPointer = key; keyPointer != '\0'; keyPointer++){    // Hacer que strchr busque en el alfabeto y devuelva un puntero a un caracter que no esté en él
        char *letter= strchr(key, keyPointer);

        if ( toupper(letter) == NULL ){
            perror("The character %c is not valid.\n", key[keyPointer]);
            return 1;
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
