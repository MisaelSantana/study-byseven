<?php

require "Pessoa.php";
require "Programador.php";

$programador = new Programador("Misael", "PHP");

echo $programador->getNome();
