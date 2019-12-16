#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int LeggiDati(char nome[14], int * n, int mat[10][10], int valori[40]) {
    FILE * file;
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

int risolvi(int n, int mat[10][10], int valori[40]){

    int i = 0, j = 0;
    int curMax = 0;
    int curVisibili = 0;

    for(i=0; i<n; i++){
            curVisibili = 0;
            curMax = 0;
        for(j=0; j<n; j++){
            if(mat[j][i] > curMax){
                curMax = mat[j][i];
                curVisibili++;
            }
        }
        if(curVisibili != valori[i]) return 0;
    }

    for(i = 0; i < n ; i++){
            curVisibili = 0;
            curMax = 0;
        for(j=0; j<n; j++){
            if(mat[i][n-j-1] > curMax){
                curMax = mat[i][n-j-1];
                curVisibili++;
            }
        }
        if(curVisibili != valori[i+n]) return 0;
    }

    for(i=0; i < n; i++){
            curVisibili = 0;
            curMax = 0;
        for(j=0; j<n; j++){

            if(mat[n-j-1][n-i-1] > curMax){
                curMax = mat[n-j-1][n-i-1];
                curVisibili++;
            }
        }
        if(curVisibili != valori[i+2*n]) return 0;
    }

    for(i = 0; i < n ; i++){
            curVisibili = 0;
            curMax = 0;
        for(j=0; j<n; j++){

            if(mat[n-i-1][j] > curMax){
                curMax = mat[n-i-1][j];
                curVisibili++;
            }
        }
        if(curVisibili != valori[i+3*n]) return 0;
    }

    return 1;

}

int verificaCorretto(int n, int mat[10][10]){

    int i, j;
    int numeri[10] = {0};

    /*Controllo righe*/
    for(i = 0; i<n; i++){

        for(j=0;j<n; j++){
            numeri[j] = 0;
        }

        for(j=0; j<n; j++){
            if(numeri[mat[i][j]-1]){
                return 0;
            }
            else {
                numeri[mat[i][j]-1] = 1;
            }
        }
    }

    /* Controllo colonne */
    for(i = 0; i<n; i++){

        for(j=0;j<n; j++){
            numeri[j] = 0;
        }

        for(j=0; j<n; j++){
            if(numeri[mat[j][i]-1]){
                return 0;
            }
            else {
                numeri[mat[j][i]-1] = 1;
            }
        }
    }

    return 1;

}
int main(){

/*   int i,j;
*/
    char nomeFile[14];
    int dim;
    int matrice[10][10];
    int valoriEsterni[40];

    scanf("%s", nomeFile);

    if(!LeggiDati(nomeFile, &dim, matrice, valoriEsterni)){
        return 0;
    }

    /*  Ciclo per stampare la matrice letta in input */
/*
   for(i = 0; i<dim; i++){
        for(j = 0; j<dim; j++){
            printf("%d ", matrice[i][j]);
        }
        printf("\n");
    }
    printf("\n");

*/
    printf("%d\n", verificaCorretto(dim, matrice) && risolvi(dim, matrice, valoriEsterni));


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
