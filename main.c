#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int LeggiDati(FILE * file, char nome[14], int * n, int mat[10][10], int valori[40]) {
    int i, j;

    file = fopen(nome, "rb");
    if(file == NULL){
        printf("Non sono riuscito ad aprire il file\n\n");
        return 0;
    }
    fread(n, sizeof(int), 1, file);

    for(i = 0; i< *n; i++){
        for(j = 0; j< *n; j++){
            fread(&( mat[i][j] ), sizeof(int), 1, file);
        }
    }

    for(i = 0; i < 4*(*n); i++){
        fread(&(valori[i]), sizeof(int), 1, file);
    }

    fclose(file);
     return 1;
}

int main(){

/*    int i,j;  */

    FILE * infile = NULL;
    char nomeFile[14];
    int dim;
    int matrice[10][10];
    int valoriEsterni[40];

    scanf("%s", nomeFile);

    if(!LeggiDati(infile, nomeFile, &dim, matrice, valoriEsterni)){
        return 0;
    }

    /*          RISOLVI             */


    /*  Ciclo per stampare la matrice letta in input */
/*
    for(i = 0; i<dim; i++){
        for(j = 0; j<dim; j++){
            printf("%d ", matrice[i][j]);
        }
        printf("\n");
    }
*/

    /* Cicli per stampare le righe esterne lette */


 /*
    for(i = 0; i<dim*4; i++){
        printf("%c%d", valoriEsterni[i], i%dim==0?'\n':' ');
    }
*/


/*    risolvi(dim, matrice, valoriEsterni)
*/
    return 0;

}
