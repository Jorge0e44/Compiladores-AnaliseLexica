#include "alimento.h"
#include <string.h>

//Verifica se determinado alimento ainda consta no cadastro do sistema
int eh_pedido_atual(int id,Alimento *a){
    Alimento *aux = a;
    while(!vazia_alimentos(aux)){
        if(id == aux->id) return 1;
        aux = aux->prox;
    }
    return 0;
}

//Verifica se a lista de alimentos está vazia
int vazia_alimentos(Alimento *a){
	return (a == NULL);
}

//Insere um novo alimento na lista 
Alimento* inserir_alimento(Alimento* alimentos,IDAlimentos *ida){
	char resp;
	float verifica;
	int erro = 0;
	int tecla;
	Alimento* novo = malloc(sizeof(Alimento));
	printf("Deseja inserir um ID? S/N\n");
	fflush(stdin);
	scanf("%c",&resp);
	if((resp == 'S') || (resp == 's')){
		printf("Entre com o ID\n");
		fflush(stdin);
		int id;
		scanf("%d",&id);
		while(eh_id_disponivel(ida,id)){
			printf("ID nao disponivel\nDigite outro id:\n");
			scanf("%d",&id);
		}
		printf("ID do produto: %d\n",id);
		novo->id = id;
		ida->idlivres[id] = -1;		
	}
	else if((resp == 'N') || (resp == 'n')){
		ida = proxidalimentos(ida);
		novo->id = ida->id;
		printf("ID do alimento: %d\n",novo->id);
	}
	printf("Entre com o nome do alimento\n");
	fflush(stdin);
	scanf("%[^\n]",novo->nome);
	fflush(stdin);
	tecla = novo->nome[0];
	if(!eh_alfanumerico(tecla)) erro = 1;
	printf("Entre com o valor calorico (kcal)\n");
	fflush(stdin);
	scanf("%f",&novo->valorcal);
	verifica = novo->valorcal;
	if(verifica < 0) erro = 2;
	printf("Entre com o preco (R$)\n");
	fflush(stdin);
	scanf("%f",&novo->preco);
	verifica = novo->preco;
	if(verifica < 0) erro = 2;
	printf("Deseja inserir a marca? S/N\n");
	fflush(stdin);
	scanf("%c",&resp);
	if((resp == 'S') || (resp == 's')){
		printf("Entre com a marca\n");
		fflush(stdin);
		scanf("%[^\n]",novo->marca);
	}
	else strcpy(novo->marca,"N/A");
	if(erro != 0){
		FILE *f = fopen("log_alimentos.txt","w");
		fprintf(f,"ID %d não inserido por erro de validação %d\n",ida->id,erro);
		printf("Alimento não inserido por falha na inserção dos dados\n");
		ida->idlivres[ida->id] = 0;
		fclose(f);
		return alimentos;
	}
	else{		
		novo->prox = alimentos;
		return novo;
	}
}

//Remove um alimento da lista
Alimento* remover_alimento(Alimento *alimentos,IDAlimentos *ida){
    if(vazia_alimentos(alimentos)){
        printf("Lista vazia, nada a remover\n");
        return alimentos;
    }
    int id;
    printf("Entre com o id do alimento que deseja remover: ");
    fflush(stdin);
    scanf("%d",&id);
    fflush(stdin);
    Alimento *aux = alimentos->prox;
    Alimento *ant = alimentos;
    if(alimentos->id == id){
        free(alimentos);
        return aux;
    }
    while(!vazia_alimentos(aux)){
        if(aux->id == id){
           ant->prox = aux->prox;
           free(aux);
           break;
        }
        ant = aux;
        aux = aux->prox;
    }
    ida->idlivres[id] = 0;
    printf("Produto removido com sucesso\n");
    system("pause");
    return alimentos;
}

//Altera os dados de um alimento da lista
Alimento* alterar_alimento(Alimento *alimentos){
    Alimento *aux = alimentos;
    char resp;
    int id;
    printf("Entre com o id do alimento que deseja alterar: ");
    fflush(stdin);
    scanf("%d",&id);
    while(!vazia_alimentos(aux)){
        if(aux->id == id){
            printf("Deseja alterar o nome do alimento? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com o nome do alimento:\n");
                fflush(stdin);
                scanf("%[^\n]",aux->nome);
            }
            printf("Deseja alterar o valor calorico? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com o valor calorico:\n");
                fflush(stdin);               
                scanf("%f",&aux->valorcal);
            }
            printf("Deseja alterar o preco? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com o preco:\n");
                fflush(stdin);
                scanf("%d",&aux->preco);
            }
            printf("Deseja alterar a marca? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com a marca:\n");
                fflush(stdin);
                scanf("%[^\n]",aux->marca);
            }            
        }
        aux = aux->prox;
    }
    return alimentos;
}

//Imprime na tela todas as informações de um determinado alimento
Alimento* consultar_alimento(Alimento *alimentos){
    Alimento *aux = alimentos;
    int flag = 0;
    int id;
    printf("Entre com o id do alimento que deseja consultar: ");
    scanf("%d",&id);
    while(!vazia_alimentos(aux)){
        if(id == aux->id){
        	flag = -1;
            printf("ID = %d\n",aux->id);
           	printf("Nome = %s\n",aux->nome);
           	printf("Valor calorico = %.2f kcal\n",aux->valorcal);
           	printf("Preco = R$%.2f\n",aux->preco);
           	printf("Marca = %s\n",aux->marca);
        }
        aux = aux->prox;
    }
    if(flag != -1) printf("Produto nao encontrado\n");
    system("pause");
    return alimentos;
}

//Imprime na tela todas as informações de todos os alimentos
Alimento* imprime_lista_alimentos(Alimento *alimentos){
    Alimento *aux = alimentos;
    system("cls");
    printf("Lista de alimentos cadastrados\n");
    while(!vazia_alimentos(aux)){
        printf("ID = %d\n",aux->id);
        printf("Nome = %s\n",aux->nome);
        printf("Valor calorico = %.2f kcal\n",aux->valorcal);
        printf("Preco = R$%.2f\n",aux->preco);
        printf("Marca = %s\n",aux->marca);
        printf("-----------------------\n");
        aux = aux->prox;
    }
    system("pause");
    return alimentos;
}

//Inicia a lista de id, determinando parametros inciais
IDAlimentos* inicializa_id_alimentos(IDAlimentos* ida){
	ida = malloc(sizeof(IDAlimentos));
	ida->idlivres[0] = -1;
    for(int i=1;i<MAX;i++){
    	ida->idlivres[i] = 0;
    }
    return ida;
}

//Determina o próximo ID disponível para ser utilizado
IDAlimentos* proxidalimentos(IDAlimentos* ida){
    for(int i=1;i<MAX;i++){
    	if(ida->idlivres[i] == 0){
    		ida->id = i;
    		ida->idlivres[i] = -1;
    		break;
    	}
    }
    return ida;
}

//Verifica se o id está disponível para ser utilizado
int eh_id_disponivel(IDAlimentos* ida,int id){
	if(ida->idlivres[id] == -1) return 1;
	return 0;
}

//Verifica se um caracter é alfanumérico
int eh_alfanumerico(int caracter){
	if((caracter >= 48 && caracter <= 57) || (caracter >= 65 && caracter <= 90) || (caracter >= 97 && caracter <= 122)) return 1;
	return 0;
}