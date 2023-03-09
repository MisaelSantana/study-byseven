<?php

require "Pessoa.php"

$pessoa = new Pessoa;

$pessoa = new Pessoa("Misael");
echo $pessoa->getNome();
