/* Generated By:JJTree: Do not edit this line. Node.java Version 4.3 */
/* JavaCCOptions:MULTI=false,NODE_USES_PARSER=false,VISITOR=false,TRACK_TOKENS=false,NODE_PREFIX=AST,NODE_EXTENDS=,NODE_FACTORY=,SUPPORT_CLASS_VISIBILITY_PUBLIC=true */

public
interface Node {

  /** Seu método é chamado após o nó ter se tornado o atual
    nó. 
	Indica que os nós filhos agora podem ser adicionados a ele. */
  public void jjtOpen();

  /** Este método é chamado depois que todos os nós filhos forem
    adicionados. */
  public void jjtClose();

  /** Este par de métodos é usado para informar o nó de seu
    pai. */
  public void jjtSetParent(Node n);
  public Node jjtGetParent();

  /** Este método diz ao nó para adicionar seu argumento ao do nó da lista dos filhos.  */
  public void jjtAddChild(Node n, int i);

  /** Este método retorna um nó filho. Os filhos são numerados
     de zero, da esquerda para a direita. */
  public Node jjtGetChild(int i);

  /** Retorne o número de filhos que o nó possui. */
  public int jjtGetNumChildren();
}
/* JavaCC - OriginalChecksum=a7d9d685ec867dd5f1d1a896975d7357 (do not edit this line) */
