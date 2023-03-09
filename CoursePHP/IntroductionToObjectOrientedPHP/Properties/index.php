<?php

require "Pessoa.php"

$uma_pessoa = new Pessoa;

$uma_pessoa->setNome("Misael");
echo $uma_pessoa->getNome();
