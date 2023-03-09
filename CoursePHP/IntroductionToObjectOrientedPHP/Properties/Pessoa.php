<?php

class Pessoa{
    //public
    //private
    //protected
    
    private $nome;

    public function setNome($novoNome){
        $this->nome = $novoNome;
    }
    public function getNome(){
        return $this->nome;
    }
}
