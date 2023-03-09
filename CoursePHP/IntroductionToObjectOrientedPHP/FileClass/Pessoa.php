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