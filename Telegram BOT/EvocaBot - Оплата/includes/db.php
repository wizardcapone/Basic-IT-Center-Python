<?php
class ConnectDB {
	private $host;
	private $user;
	private $pass;
	private $db;
	function constructor($host, $user, $pass, $db){
		$this->host = $host;
		$this->user = $user;
		$this->pass = $pass;
		$this->db = $db;
	}
	function connect(){
		$connection = mysqli_connect($this->host,$this->user,$this->pass,$this->db);
		if (!$connection) {
		    echo "Ошибка: Невозможно установить соединение с MySQL." . PHP_EOL;
		    die();
		}
		return $connection;
	}
}
$request = new ConnectDB();
$request->constructor('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter');
$conn = $request->connect();
?>