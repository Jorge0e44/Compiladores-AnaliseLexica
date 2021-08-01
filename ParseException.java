/* Generated By:JavaCC: Do not edit this line. ParseException.java Version 5.0 */
/* JavaCCOptions:KEEP_LINE_COL=null */

public class ParseException extends Exception {

  private static final long serialVersionUID = 1L;

  /**
   * Este construtor é usado pelo método "generateParseException"
   * no analisador gerado. Chamar este construtor gera
   * um novo objeto deste tipo com os campos "currentToken",
   * Conjunto de "expectedTokenSequences" e "tokenImage".
   */
  public ParseException(Token currentTokenVal,
                        int[][] expectedTokenSequencesVal,
                        String[] tokenImageVal
                       )
  {
    super(initialise(currentTokenVal, expectedTokenSequencesVal, tokenImageVal));
    currentToken = currentTokenVal;
    expectedTokenSequences = expectedTokenSequencesVal;
    tokenImage = tokenImageVal;
  }

  public ParseException() {
    super();
  }

  /** Constructor with message. */
  public ParseException(String message) {
    super(message);
  }


  /**
   * Este é o último token consumido com sucesso. Se
   * este objeto foi criado devido a um erro de análise, o token
   * Seguindo este token será (portanto) o primeiro token de erro.
   */
  public Token currentToken;

  /**
   * Cada entrada nesta matriz é uma matriz de inteiros. Cada array
   * de inteiros representa uma sequência de tokens (por seu valor ordinal)
   *que é esperado neste ponto da análise.
   */
  public int[][] expectedTokenSequences;

  /**
   * Esta é uma referência à matriz "tokenImage" do
   * analisador no qual ocorreu o erro de análise. Esta matriz é
   * definido na interface gerada ... Constantes.
   */
  public String[] tokenImage;

  /**
   * Ele usa "currentToken" e "expectTokenSequences" para gerar uma
   * mensagem de erro e a retorna. Se este objeto foi criado
   * devido a um erro de análise, e você não o detecta (ele é lançado
   * do analisador) a mensagem de erro correta
   * é exibida.
   */
  private static String initialise(Token currentToken,
                           int[][] expectedTokenSequences,
                           String[] tokenImage) {
    String eol = System.getProperty("line.separator", "\n");
    StringBuffer expected = new StringBuffer();
    int maxSize = 0;
    for (int i = 0; i < expectedTokenSequences.length; i++) {
      if (maxSize < expectedTokenSequences[i].length) {
        maxSize = expectedTokenSequences[i].length;
      }
      for (int j = 0; j < expectedTokenSequences[i].length; j++) {
        expected.append(tokenImage[expectedTokenSequences[i][j]]).append(' ');
      }
      if (expectedTokenSequences[i][expectedTokenSequences[i].length - 1] != 0) {
        expected.append("...");
      }
      expected.append(eol).append("    ");
    }
    String retval = "Encontrado \"";
    Token tok = currentToken.next;
    for (int i = 0; i < maxSize; i++) {
      if (i != 0) retval += " ";
      if (tok.kind == 0) {
        retval += tokenImage[0];
        break;
      }
      retval += " " + tokenImage[tok.kind];
      retval += " \"";
      retval += add_escapes(tok.image);
      retval += " \"";
      tok = tok.next;
    }
    retval += "\" na linha " + currentToken.next.beginLine + ", coluna " + currentToken.next.beginColumn;
    retval += "." + eol;
    if (expectedTokenSequences.length == 1) {
      retval += "Era esperado:" + eol + "    ";
    } else {
      retval += "Era esperado um de:" + eol + "    ";
    }
    retval += expected.toString();
    return retval;
  }

  /**
   * The end of line string for this machine.
   */
  protected String eol = System.getProperty("line.separator", "\n");

  /**
   * Usado para converter caracteres brutos em sua versão de espaço
   * quando esta versão bruta não pode ser usada como parte de um ASCII
   * literal de string.
   */
  static String add_escapes(String str) {
      StringBuffer retval = new StringBuffer();
      char ch;
      for (int i = 0; i < str.length(); i++) {
        switch (str.charAt(i))
        {
           case 0 :
              continue;
           case '\b':
              retval.append("\\b");
              continue;
           case '\t':
              retval.append("\\t");
              continue;
           case '\n':
              retval.append("\\n");
              continue;
           case '\f':
              retval.append("\\f");
              continue;
           case '\r':
              retval.append("\\r");
              continue;
           case '\"':
              retval.append("\\\"");
              continue;
           case '\'':
              retval.append("\\\'");
              continue;
           case '\\':
              retval.append("\\\\");
              continue;
           default:
              if ((ch = str.charAt(i)) < 0x20 || ch > 0x7e) {
                 String s = "0000" + Integer.toString(ch, 16);
                 retval.append("\\u" + s.substring(s.length() - 4, s.length()));
              } else {
                 retval.append(ch);
              }
              continue;
        }
      }
      return retval.toString();
   }

}
/* JavaCC - OriginalChecksum=e25b01bc55ed9d08151448657bb75b17 (do not edit this line) */