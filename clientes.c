#include <stdio.h>
#include <stdlib.h>
#include "clientes.h"
//#include "alimento.h"

//Verifica se a lista de clientes está vazia
int vazia_cliente(Cliente *c){
    return c == NULL;
}

//Insere um cliente novo na lista
Cliente* inserir_cliente(Cliente *clientes,Alimento *alimentos,IDClientes *idc){
    char resp;
    int pedido;
    int i,n,j = 0;
    int tecla,erro = 0,verifica;
    Cliente *novo = malloc(sizeof(Cliente));
    printf("Deseja inserir um ID? S/N\n");
    fflush(stdin);
    scanf("%c",&resp);
    if((resp == 'S') || (resp == 's')){
        printf("Entre com o ID\n");
        fflush(stdin);
        int id;
        scanf("%d",&id);
        while(eh_id_disponivelc(idc,id)){
            printf("ID %d nao disponivel\nDigite outro id:\n",id);
            scanf("%d",&id);
        }
        printf("ID do cliente: %d\n",id);
        novo->id = id;
        idc->idlivres[id] = -1;     
    }
    else if((resp == 'N') || (resp == 'n')){
        idc = proxidclientes(idc);
        novo->id = idc->id;
        printf("ID do cliente: %d\n",novo->id);
    }
    printf("Entre com o nome do cliente\n");
    fflush(stdin);
    scanf("%[^\n]",novo->nome);
    tecla = novo->nome[0];
    if(!eh_alfanumerico(tecla)) erro = 1;
    printf("Entre com a data de nascimento (DD/MM/AA)\n");
    fflush(stdin);
    scanf("%[^\n]",novo->nascimento);
    tecla = novo->nascimento[0];
    if(!eh_alfanumerico(tecla)) erro = 1;
    printf("Deseja inserir a quantidade de viagens? S/N\n");
    fflush(stdin);
    scanf("%c",&resp);
    if((resp == 'S') || (resp == 's')){
        printf("Entre com a quantidade de viagens\n");
        fflush(stdin);
        scanf("%d",&novo->numviagens);
        verifica = novo->numviagens;
        if(verifica < 0) erro = 2;
    }
    else novo->numviagens = 0;
    printf("Deseja inserir o historico de alimentos? S/N\n");
    fflush(stdin);
    scanf("%c",&resp);
    if((resp == 'S') || (resp == 's')){
        printf("Quantos IDs deseja inserir?\n");
        fflush(stdin);
        scanf("%d",&n);
        for(i=0;i<n;i++){
            printf("Entre com o ID do alimento\n");
            fflush(stdin);
            scanf("%d",&pedido);
            if(pedido < 0) erro = 2;
            novo->pedidos[i] = pedido;
            if(eh_pedido_atual(pedido,alimentos)){
                novo->pedidosatual[j] = pedido;
                j++;
            }
        }
    }
    else {
        i = 0;
        j = 0;
    }
    novo->numpedidos = i;
    novo->numpedidosatual = j;
    if(erro != 0){
        FILE *f = fopen("log_clientes.txt","w");
        fprintf(f,"ID %d não inserido por erro de validação %d\n",idc->id,erro);
        printf("Cliente não inserido por falha na inserção dos dados\n");
        idc->idlivres[idc->id] = 0;
        fclose(f);
        printf("%d",erro);
        system("pause");
        return clientes;
    }
    else{       
        novo->prox = clientes;
        return novo;
    }
}

//Remove um cliente da lista
Cliente* remover_cliente(Cliente *c,IDClientes *idc){
    if(vazia_cliente(c)){
        printf("Lista vazia, nada a remover\n");
        return c;
    }
    int id;
    printf("Entre com o id do cliente que deseja remover: ");
    fflush(stdin);
    scanf("%d",&id);
    Cliente *aux = c->prox;
    Cliente *ant = c;
    if(c->id == id){
        free(c);
        return aux;
    }
    while(!vazia_cliente(aux)){
        if(aux->id == id){
           ant->prox = aux->prox;
           free(aux);
           break;
        }
        ant = aux;
        aux = aux->prox;
    }
    idc->idlivres[id] = 0;
    return c;
}

//Altera os dados de um cliente da lista
Cliente* alterar_cliente(Cliente *c,Alimento *alim){
    Cliente *aux = c;
    char resp;
    int i,n,j = 0;
    int pedido;
    int id;
    printf("Entre com o id do cliente que deseja alterar: ");
    fflush(stdin);
    scanf("%d",&id);
    while(!vazia_cliente(aux)){
        if(aux->id == id){
            printf("Deseja alterar o nome do cliente? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com o nomoe do cliente:\n");
                fflush(stdin);
                scanf("%[^\n]",aux->nome);
            }
            printf("Deseja alterar a data de nascimento? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com a data de nascimento:\n");
                fflush(stdin);
                scanf("%[^\n]",aux->nascimento);
            }
            printf("Deseja alterar a quantidade de viagens? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                printf("Entre com o numero de viagens:\n");
                fflush(stdin);
                scanf("%d",&aux->numviagens);
            }
            printf("Deseja alterar o historico de pedidos? S/N\n");
            fflush(stdin);
            scanf("%c",&resp);
            if((resp == 'S') || (resp == 's')){
                j = 0;
                free(aux->pedidos);
                free(aux->pedidosatual);
                printf("Quantos IDs deseja inserir?\n");
                fflush(stdin);
                scanf("%d",&n);
                for(i = 0;i<n;i++){
                    printf("Entre com o ID do alimento:\n");
                    fflush(stdin);
                    scanf("%d",&pedido);
                    aux->pedidos[i] = pedido;
                    if(eh_pedido_atual(pedido,alim)){
                        aux->pedidosatual[j] = pedido;
                        j++;
                    }
                }
            }
            else {
                i = 0;
                j = 0;
            }
        }
        aux->numpedidos = i;
        aux->numpedidosatual = j;
        aux = aux->prox;
    }
    return c;
}

//Imprime na tela todos os dados de um determinado cliente
Cliente* consultar_cliente(Cliente *c){
    Cliente *aux = c;
    int i,j=0;
    int flag = 0;
    int id;
    printf("Entre com o id do cliente que deseja consultar: ");
    fflush(stdin);
    scanf("%d",&id);
    while(!vazia_cliente(aux)){
        if(id == aux->id){
            flag = -1;
            printf("ID = %d\n",aux->id);
            printf("Nome = %s\n",aux->nome);
            printf("Data de Nascimento = %s\n",aux->nascimento);
            printf("Quantidade de viagens realizadas pelo cliente = %d\n",aux->numviagens);
            printf("\nHistorico completo de pedidos: \n");
            printf("Numero de pedidos: %d\n",aux->numpedidos);
            for(i = 0;i<aux->numpedidos;i++){
                printf("ID do alimento = %d\n",aux->pedidos[i]);
            }
            printf("\nHistorico atual de pedidos: \n");
            printf("Numero de pedidos atuais: %d\n",aux->numpedidosatual);
            for(j = 0;j<aux->numpedidosatual;j++){
                printf("ID do alimento = %d\n",aux->pedidosatual[j]);
            }
        }
        aux = aux->prox;
    }
    if(flag != -1) printf("Produto nao encontrado");
    system("pause");
    return c;
}

//Imprime na tela todos os dados de todos os clientes
Cliente* imprime_lista_clientes(Cliente *c){
    Cliente *aux = c;
    int i,j=0;
    system("cls");
    printf("Lista de clientes cadastrados\n");
    while(!vazia_cliente(aux)){
        printf("ID = %d\n",aux->id);
        printf("Nome = %s\n",aux->nome);
        printf("Data de Nascimento = %s\n",aux->nascimento);
        printf("Quantidade de viagens realizadas pelo cliente = %d\n",aux->numviagens);
        printf("\nHistorico completo de pedidos: \n");
        for(i = 0;i<aux->numpedidos;i++){
            printf("ID do alimento = %d\n",aux->pedidos[i]);
        }
        printf("\nHistorico atual de pedidos: \n");
        for(i = 0;i<aux->numpedidosatual;i++){
            printf("ID do alimento = %d\n",aux->pedidosatual[j]);
        }
        printf("-----------------------\n");
        aux = aux->prox;
    }
    system("pause");
    return c;
}

//Inicia a lista de clientes, determinando parâmetros iniciais
IDClientes* inicializa_id_clientes(IDClientes* idc){
    idc = malloc(sizeof(IDClientes));
    idc->idlivres[0] = -1;
    for(int i=1;i<MAX;i++){
        idc->idlivres[i] = 0;
    }
    return idc;
}

//Determina o próximo ID disponível para clientes
IDClientes* proxidclientes(IDClientes* idc){
    for(int i=1;i<MAX;i++){
        if(idc->idlivres[i] == 0){
            idc->id = i;
            idc->idlivres[i] = -1;
            break;
        }
    }
    return idc;
}

//Verifica se um ID está disponível para ser utilizado
int eh_id_disponivelc(IDClientes* idc,int id){
    if(idc->idlivres[id] == -1) return 1;
    return 0;
}
