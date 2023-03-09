# Objetivo da PSR-2:
-> Visa facilitar o entendimneto quando se está lendo um código de autores diferentes.
-> Apresenta uma série de regras sobre como formatar códigos PHP.


# Última linha:
-> Todos os arquivos PHP DEVEM terminar com uma única linha em branco.


# Tag fechamento ?>:
-> Não se deve usar a tag de fechamento em arquivos de PHP puros.


# Limite suave de 120 caracteres por linha:
-> Linhas NÃO DEVERIAM possuir mais de 80 caracteres;
-> O limite de caracteres em uma linha DEVE ser de 120 caracteres.


# Espaços:
-> Linhas que não estão em branco, NÃO DEVEM ter espaços após o conteúdo da mesma.


# Linhas em branco PODEM:
-> Linhas em branco PODEM ser adicionadas caso você ache que vá facilitar a 
interpretação do código.


# Declarações:
-> NÃO DEVE haver mais de uma declaração por linha.


# Identação:
-> Códigos PHP DEVEM ser identados com 4 espaços ao invés de TAB.


# Palavras chave:
-> Palavras chaves DEVEM ser escritas com letras minúsculas:
    -> true;
    -> false;
    -> null.


# Namespaces:
-> Quando um namespace for definido, DEVE haver uma linha em branco após;
-> Declarações "use" DEVEM estar após a declaração do namespace.


# Extends e implements:
-> As palavras-chave "extends" e "implements" DEVEM ser declaradas sempre na 
mesma linha do nome da classe.


# Visibilidade:
-> A visibilidade DEVE ser declarada em todos os métodos
    -> public;
    -> protected;
    -> private


# Métodos:
-> NÃO DEVE existir um espaço em branco após o nome de um método;
-> Chave de abertura do método DEVE ficar na linha de baixo;
-> Chave de fechamento DEVE ficar logo após o corpo do método;
-> NÃO DEVE haver um espaço em branco após o parêntese de abertura.


# Argumentos:
-> Espaço após cada argumento;
-> Similar a escrita;
-> Podem ser declarados em múltiplas linhas.


# Abstract, final e static
-> Quando presentes, abstract e final DEVEM preceder a declaração de visibilidade;
-> Static DEVE vir após.


# Condicionais:
-> A palavra-chave "elseif" DEVE ser usada no lugar de "else if"


# Switch:
-> "case" deve estar identada em switch;
-> "break" identando em case;
-> Comentário no "break".
    switch {
        case:
            break;
            // no break;
    }


# Iteradores:
-> for:
for ($i = 0; $i < 10; $i++) {
    // for body
}

-> foreach:
foreach ($iterable as $key => $value) {
    // foreach body
}

-> while:
while ($expr) {
    //structure body
}

-> do while
do {
    // structure body
} while ($expr);


# Exceções:
-> Ex: "try":
try {
    // try body
} catch (FirstExceptionType $e) {
    // catch body
} catch (OtherExceptionType $e) {
    // catch body
}
