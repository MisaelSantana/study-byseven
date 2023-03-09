<?php

class Pessoa{
    
    protected $nome;
    const ESPECIE = "Humano";

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
