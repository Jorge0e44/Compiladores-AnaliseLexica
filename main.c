#include "clientes.c"
#include "alimento.c"
#include <windows.h>

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
Alimento* menu_alimentos(Alimento* alimentos,IDAlimentos *ida){	
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
			alimentos = inserir_alimento(alimentos,ida);
			alimentos = imprime_lista_alimentos(alimentos);
			break;
				
			case 2:
			system("cls");
			alimentos = alterar_alimento(alimentos);
			alimentos = imprime_lista_alimentos(alimentos);
			break;
				
			case 3:
			system("cls");
			alimentos = consultar_alimento(alimentos);
			alimentos = imprime_lista_alimentos(alimentos);
			break;
				
			case 4:
			system("cls");
			alimentos = remover_alimento(alimentos,ida);
			printf("Produto removido com sucesso\n");
			system("pause");
			alimentos = imprime_lista_alimentos(alimentos);
			break;
		}
	}
	return alimentos;
}

//Desaloca ponteiros para liberar memória
void liberar_memoria(IDAlimentos *ida,IDClientes *idc,Alimento *alim,Cliente *cli){
	free(ida);
	free(idc);
	free(alim);
	free(cli);
}

int main(){
	int resp;
	Alimento *alimentos = NULL;
	Cliente *clientes = NULL;
	IDClientes *idc = inicializa_id_clientes(idc);
	IDAlimentos *ida = inicializa_id_alimentos(ida);
	while(1){
		system("cls");
		printf("Sistema de controle de Clientes e Alimentos\n");
		printf("1 - Cadastro de Alimentos\n");
		printf("2 - Cadastro de Clientes\n");
		printf("0 - Encerrar\n");
		scanf("%d",&resp);
		switch(resp){
			case 0:
			liberar_memoria(ida,idc,alimentos,clientes);
			return 0;
			
			case 1:
			alimentos = menu_alimentos(alimentos,ida);
			break;
			
			case 2:
			clientes = menu_clientes(clientes,alimentos,idc);
			break;
		}
	}
	return 0;
}
