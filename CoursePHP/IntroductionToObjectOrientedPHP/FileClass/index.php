<?php

require "Pessoa.php"

$uma_pessoa = new Pessoa;
$uma_pessoa->nome = "Misael"
$uma_pessoa->site = "www.MisaelSantana.com.br"

var_dump($uma_pessoa);

$uma_pessoa->falarNome();
$uma_pessoa->falarSite();
