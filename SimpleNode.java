/* Generated By:JJTree: Do not edit this line. SimpleNode.java Version 4.3 */
/* JavaCCOptions:MULTI=false,NODE_USES_PARSER=false,VISITOR=false,TRACK_TOKENS=false,NODE_PREFIX=AST,NODE_EXTENDS=,NODE_FACTORY=,SUPPORT_CLASS_VISIBILITY_PUBLIC=true */
public
class SimpleNode implements Node {

  protected Node parent;
  protected Node[] children;
  protected int id;
  protected Object value;
  protected MyPascal parser;

  public SimpleNode(int i) {
    id = i;
  }

  public SimpleNode(MyPascal p, int i) {
    this(i);
    parser = p;
  }

  public void jjtOpen() {
  }

  public void jjtClose() {
  }

  public void jjtSetParent(Node n) { parent = n; }
  public Node jjtGetParent() { return parent; }

  public void jjtAddChild(Node n, int i) {
    if (children == null) {
      children = new Node[i + 1];
    } else if (i >= children.length) {
      Node c[] = new Node[i + 1];
      System.arraycopy(children, 0, c, 0, children.length);
      children = c;
    }
    children[i] = n;
  }

  public Node jjtGetChild(int i) {
    return children[i];
  }

  public int jjtGetNumChildren() {
    return (children == null) ? 0 : children.length;
  }

  public void jjtSetValue(Object value) { this.value = value; }
  public Object jjtGetValue() { return value; }


  public String toString() {
    if(value != null){
      return MyPascalTreeConstants.jjtNodeName[id] + " ['" +  value + "']";
    }
    else{
      return MyPascalTreeConstants.jjtNodeName[id];
    }
  }

  public String toString(String prefix) { return prefix + toString(); }


  public void dump(String prefix) {
    dumpAux(prefix, "|" + prefix);
  }

  public void dumpAux(String prefix, String fixPrefix){
    System.out.println(toString(prefix));
    if (children != null) {
      for (int i = 0; i < children.length; ++i) {
        SimpleNode n = (SimpleNode)children[i];
        if (n != null) {
          n.dumpAux(prefix + fixPrefix, fixPrefix);
        }
      }
    }
  }
}

/* JavaCC - OriginalChecksum=d93e7359c2a614a7314297db45aa7491 (do not edit this line) */