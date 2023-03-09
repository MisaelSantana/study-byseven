<?php

class Programador extends Pessoa{
    public $linguagem;
    
    public function __construct($tmpnome, $tmpLinguaguem)
    {
        $this->nome = $tmpnome;
        $this->linguagem = $tmpLinguaguem;
    }
}
