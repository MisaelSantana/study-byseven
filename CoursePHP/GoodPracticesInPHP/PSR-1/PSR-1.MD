# Tags:
-> Arquivos em PHP DEVEM usar somente as tags <?php e <?=
-> Proibido usar:
    -> short open tags (<?);
    -> tags ASP (<%);
    -> tags de script (<script language="PHP">)


# Codificação de arquivos PHP:
-> DEVEM usar somente a codificação UTF-8 sem BOM(Byte Order Mark).


# Arquivos PHP DEVERIAM:
-> Declarar símbolos:
    -> Classes, funções e constantes.
-> Causar efeitos colaterais:
    -> echo/include

-> Mas NÃO DEVERIAM fazer ambos.


# Nome das classes e namespaces:
-> DEVEM ser declarados em StudlyCaps:
    -> Ex: PrimeiraClasse {

    }


# Constantes:
-> DEVEM ser declaradas com letras maísculas e serem separadas por
   underlines:
    -> Ex: UMA_CONSTANTE


# Nome de métodos:
-> DEVEM ser declarados em camelCase:
    -> Ex: meuMetodo()
