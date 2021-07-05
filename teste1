#include "clientes.c"
#include "alimento.c"
#include "viagens.c"
#include <windows.h>

//Gera 3 arquivos com relatorios de alimentos, viagens e clientes cadastrados
void relatorios(Viagem *viagens,Alimento *alimentos, Cliente *clientes,Marca *marcas){
	FILE *f = fopen("Relatorio de Alimentos.txt","w");
	Alimento *auxa = alimentos;
    int i = 0;
    if(vazia_alimentos(auxa)) fprintf(f,"Nao foram cadastrados alimentos\n");
	while(!vazia_alimentos(auxa)){
        fprintf(f,"ID = %d\n",auxa->id);
        fprintf(f,"Nome = %s\n",auxa->nome);
        fprintf(f,"Valor calorico = %.2f kcal\n",auxa->valorcal);
        fprintf(f,"Preco = R$ %.2f\n",auxa->preco);
        fprintf(f,"Marca = %s\n",auxa->marca);
        fprintf(f,"-----------------------\n\n");
        auxa = auxa->prox;
    }
    fclose(f);
	Viagem *auxv = viagens;
	f = fopen("Relatorio de Viagens.txt","w");
	if(vazia_viagens(auxv)) fprintf(f,"Nao foram cadastradas viagens\n");
	while(!vazia_viagens(auxv)){
		fprintf(f,"ID = %d\n",auxv->id);
      	fprintf(f,"Origem = (%.6lf,%.6lf)\n",auxv->latorigem,auxv->longorigem);
        fprintf(f,"Destino = (%.6lf,%.6lf)\n",auxv->latdestino,auxv->longdestino);
        fprintf(f,"Preco = R$ %.2f\n",auxv->preco);
        fprintf(f,"-----------------------\n\n");
        auxv = auxv->prox;
	}
	fclose(f);

	f = fopen("Relatorio de Clientes.txt","w");
	Cliente *auxc = clientes;
	if(vazia_cliente(auxc)) fprintf(f,"Nao foram cadastrados clientes\n");
	while(!vazia_cliente(auxc)){
        fprintf(f,"ID = %d\n",auxc->id);
       	fprintf(f,"Nome = %s\n",auxc->nome);
        fprintf(f,"Data de Nascimento = %s\n",auxc->nascimento);
        fprintf(f,"Quantidade de viagens realizadas pelo cliente = %d\n",auxc->numviagens);
        fprintf(f,"Historico de viagens realizadas\n");
        for(i = 0;i<auxc->numviagens;i++){
        	fprintf(f,"ID da viagem: %d\n",auxc->viagens[i]);
        }
        fprintf(f,"\nHistorico completo de pedidos: \n");
        for(i = 0;i<auxc->numpedidos;i++){
            fprintf(f,"ID do alimento = %d\n",auxc->pedidos[i]);
        }
        fprintf(f,"\nHistorico atual de pedidos: \n");
        for(i = 0;i<auxc->numpedidosatual;i++){
            fprintf(f,"ID do alimento = %d\n",auxc->pedidosatual[i]);
        }
        fprintf(f,"-----------------------\n\n");
        auxc = auxc->prox;
    }
    fclose(f);

    f = fopen("Relatorio Estatistico.txt","w");
    auxa = alimentos;
    auxc = clientes;
    auxv = viagens;
    Marca *auxm = NULL;
    marcas = auxm;
	while(!vazia_alimentos(auxa)){
		auxm = marcas;
		while(!vazia_marcas(auxm)){			
			if(strcmp(auxm->nome,auxa->marca) == 0){
				auxm->quantidade++;
			}
			auxm = auxm->prox;
		}
		if(vazia_marcas(auxm)){
			auxm = malloc(sizeof(Marca));
			auxm->prox = marcas;
			marcas = auxm;
			strcpy(auxm->nome,auxa->marca);
			auxm->quantidade = 1;
		}
		auxa = auxa->prox;
	}
	
	auxm = marcas;
	char marca[MAX];
    int moda = 0;
    fprintf(f,"Quantidade de alimentos por marca\n");
    while(!vazia_marcas(auxm)){
    	if(auxm->quantidade > moda) moda = auxm->quantidade;
    	strcpy(marca,auxm->nome);
    	auxm = auxm->prox;
    }
    fprintf(f,"Marca %s: %d alimento(s).\n",marca,moda);
    fprintf(f,"--------------------\n\n");
    fprintf(f,"Preco medio das viagens por cliente\n");
    float precomedio = 0;
    while(!vazia_cliente(auxc)){
    	auxv = viagens;
    	precomedio = 0;
    	while(!vazia_viagens(auxv)){
    		if(auxc->id == auxv->idcliente){
    			precomedio += auxv->preco;
    		}
    		auxv = auxv->prox;
    	}
    	fprintf(f,"ID %d: R$ %10.2f.\n",auxc->id,precomedio/auxc->numviagens);
    	auxc = auxc->prox;
    }

    fprintf(f,"-----------------------\n\n");
    fclose(f);
    f = fopen("Relatorio Metadados.txt","w");
    auxa = alimentos;
    auxm = marcas;
    fprintf(f,"Marca(s) mais comum(ns) de Alimentos\n");
    if(vazia_alimentos(auxa)) fprintf(f,"Nao foram cadastrados alimentos\n");
   	while(!vazia_marcas(auxm)){
    	if(auxm->quantidade == moda){
    		fprintf(f,"Marca %s com %d alimentos\n",auxm->nome,auxm->quantidade);
    	}
    	auxm = auxm->prox;
    }
    fclose(f);
    printf("Relatorios gerados com sucesso\n");
    system("pause");
}

//Menu de cadastro de viagens
Viagem* menu_viagens(Viagem *viagens,Cliente *clientes,IDViagens *idv){
	int resp,id;
	while(1){
		system("cls");
		printf("\tCadastro de Viagens\n");
		printf("1 - Inserir Viagem\n");
		printf("2 - Alterar Viagem\n");
		printf("3 - Consultar Viagem\n");
		printf("4 - Remover Viagem\n");
		printf("0 - Retornar ao menu principal\n");
		scanf("%d",&resp);
		switch(resp){
			case 0:
			system("cls");
			return viagens;

			case 1:
			system("cls");			
			viagens = inserir_viagem(viagens,idv,clientes);
			viagens = imprime_lista_viagens(viagens);	
			break;

			case 2:
			system("cls");
			viagens = alterar_viagem(viagens);
			viagens = imprime_lista_viagens(viagens);
			break;

			case 3:
			system("cls");
			viagens = consultar_viagem(viagens,clientes);
			viagens = imprime_lista_viagens(viagens);
			break;

			case 4:
			system("cls");
			viagens = remover_viagem(viagens,clientes,idv);
			viagens = imprime_lista_viagens(viagens);
			break;
		}
	}
	return viagens;
}

//Menu de cadastro de clientes
Cliente* menu_clientes(Cliente *clientes, Alimento* alimentos, IDClientes *idc){
	int resp;
	while(1){
		system("cls");
		printf("\tCadastro de Clientes\n");
		printf("1 - Inserir Cliente\n");
		printf("2 - Alterar Cliente\n");
		printf("3 - Consultar Cliente\n");
		printf("4 - Remover Cliente\n");
		printf("0 - Retornar ao menu principal\n");
		scanf("%d",&resp);
		switch(resp){
			case 0:
			system("cls");
			return clientes;
				
			case 1:
			system("cls");
			clientes = inserir_cliente(clientes,alimentos,idc);
			clientes = imprime_lista_clientes(clientes);
			break;
				
			case 2:
			system("cls");
			clientes = alterar_cliente(clientes,alimentos);
			clientes = imprime_lista_clientes(clientes);
			break;
				
			case 3:
			system("cls");
			clientes = consultar_cliente(clientes);
			clientes = imprime_lista_clientes(clientes);
			break;
				
			case 4:
			system("cls");
			clientes = remover_cliente(clientes,idc);
			printf("Cliente removido com sucesso\n");
			system("pause");
			clientes = imprime_lista_clientes(clientes);
			break;
		}
	}
	return clientes;
}

//Menu de cadaastro de alimentos
Alimento* menu_alimentos(Alimento* alimentos,IDAlimentos *ida,Marca *marcas){	
	int resp;
	while(1){
		system("cls");
		printf("\tCadastro de Alimentos\n");
		printf("1 - Inserir Alimento\n");
		printf("2 - Alterar Alimento\n");
		printf("3 - Consultar Alimento\n");
		printf("4 - Remover Alimento\n");
		printf("0 - Retornar ao menu principal\n");
		scanf("%d",&resp);
		switch(resp){
			case 0:
			system("cls");
			return alimentos;
				
			case 1:
			system("cls");
			alimentos = inserir_alimento(alimentos,ida,marcas);
			alimentos = imprime_lista_alimentos(alimentos);
			break;
				
			case 2:
			system("cls");
			alimentos = alterar_alimento(alimentos,marcas);
			alimentos = imprime_lista_alimentos(alimentos);
			break;
				
			case 3:
			system("cls");
			alimentos = consultar_alimento(alimentos);
			alimentos = imprime_lista_alimentos(alimentos);
			break;
				
			case 4:
			system("cls");
			alimentos = remover_alimento(alimentos,ida,marcas);
			printf("Produto removido com sucesso\n");
			system("pause");
			alimentos = imprime_lista_alimentos(alimentos);
			break;
		}
	}
	return alimentos;
}

//Desaloca ponteiros para liberar memória
void liberar_memoria(IDAlimentos *ida,IDClientes *idc,IDViagens *idv, Alimento *alimentos,Cliente *clientes,Viagem *viagens){
	free(ida);
	free(idc);
	free(idv);
	free(alimentos);
	free(clientes);
	free(viagens);
}

int main(){
	int resp;
	Alimento *alimentos = NULL;
	Cliente *clientes = NULL;
	Viagem *viagens = NULL;
	Marca *marcas = NULL;
	IDClientes *idc = inicializa_id_clientes(idc);
	IDAlimentos *ida = inicializa_id_alimentos(ida);
	IDViagens *idv = inicializa_id_viagens(idv);
	while(1){
		system("cls");
		printf("Sistema de controle de Clientes, Viagens e Alimentos\n");
		printf("1 - Cadastro de Alimentos\n");
		printf("2 - Cadastro de Clientes\n");
		printf("3 - Cadastro de Viagens\n");
		printf("4 - Geracao de Relatorios\n");
		printf("0 - Encerrar\n");
		scanf("%d",&resp);
		switch(resp){
			case 0:
			liberar_memoria(ida,idc,idv,alimentos,clientes,viagens);
			return 0;
			
			case 1:
			alimentos = menu_alimentos(alimentos,ida,marcas);
			break;
			
			case 2:
			clientes = menu_clientes(clientes,alimentos,idc);
			break;

			case 3:
			viagens = menu_viagens(viagens,clientes,idv);
			break;

			case 4:
			relatorios(viagens,alimentos,clientes,marcas);
			break;
		}
	}
	return 0;
}
