<?php

class Pessoa{
    
    private $nome;

    public function __construct($tmpnome)
    {
            $this->nome = $tmpnome();
    }

    public function setNome($novoNome){
        $this->nome = $novoNome;
    }
    public function getNome(){
        return $this->nome;
    }
}
