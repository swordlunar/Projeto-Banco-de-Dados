#include <stdio.h>
#include <stdlib.h>
#include "Agenda.h"

FILE *in,*out;
Lista *agenda;
Lista *inicio;

int main(){
	char nome[40],detalhe[40];
	agenda = NULL;
	inicio = NULL;
	in = fopen("agenda.txt","r");
	out = fopen("agenda.txt","a");
	
	inicio=leitura(in,inicio,agenda);
	exibir(in,inicio,agenda);
	
	printf("\nDigite o nome de algum contato da lista para obter seus dados:\n");
	scanf("%s",nome);
	busca_nome(in,inicio,nome);
	
	printf("\nDigite o detalhe que deseja procurar na lista (rua,bairro,cidade):\n");
	scanf("%s",detalhe);
	busca_detalhe(in,inicio,detalhe);
	
	inicio=insere_novo(out,inicio,agenda);
	
	printf("Digite o nome de um contato para edita-lo:");
	scanf("%s",nome);
	editar_contato(in,inicio,nome);
	
	fclose(in);
	fclose(out);
	system("pause");
	return 0;
	
}
