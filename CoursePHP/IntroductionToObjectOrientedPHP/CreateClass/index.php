<?php

class Pessoa{
    public $nome;
    public $site;

    public function falarNome(){
        echo $this->nome;
    }
    public function falarsite(){
        echo $this->site;
    }
}

$uma_pessoa = new Pessoa;
$uma_pessoa->nome = "Misael"
$uma_pessoa->site = "www.MisaelSantana.com.br"

var_dump($uma_pessoa);

$uma_pessoa->falarNome();
$uma_pessoa->falarsite();
