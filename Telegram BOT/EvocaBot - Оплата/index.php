<?php
include "includes/db.php";
if(isset($_GET['user_id']) && isset($_GET['amount']) && isset($_GET['username'])){
	$user_id = $conn->real_escape_string($_GET['user_id']);
	$get_amount = $conn->real_escape_string($_GET['amount']);
	$username = $conn->real_escape_string($_GET['username']);
	if(!is_numeric($user_id) || !is_numeric($get_amount)){
		echo 'Произошла ошибка!!';
		die();
	}
	if($_GET['amount'] < 100){
		echo 'Произошла ошибка!!';
		die();
	}
	$query = "SELECT * FROM `deposit` WHERE `user_id` = '$user_id' AND `status` = 0";
	$sql = $conn->query($query);
	if($sql->num->rows != 0){
		$delete = "DELETE FROM `deposit` WHERE `user_id` = '$user_id' AND `status` = 0";
		$sql_delete = $conn->query($delete);
	}
	$insert = "INSERT INTO `deposit` (user_id,cost,payment_system,status) VALUES ('$user_id','$get_amount','Payeer',0)";
	$conn->query($insert);
	$m_shop = '884074296'; 
	$m_orderid = $user_id;
	$m_amount = number_format($get_amount, 2, '.', '');
	$m_curr = 'RUB';
	$m_desc = base64_encode('Test');
	$m_key = 'EJ6kSB#3&Fxs';

	$arHash = array(
		$m_shop,
		$m_orderid,
		$m_amount,
		$m_curr,
		$m_desc
	);
	$arHash[] = $m_key;

	$sign = strtoupper(hash('sha256', implode(':', $arHash)));
}
else{
	echo 'Произошла ошибка!!';
	die();
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>EvocaBot - Пополнение Баланса</title>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<script type="text/javascript" src="js/script.js"></script>
</head>
<body>
	<div style="position: absolute; width: 100%; height: 100%; min-height: 100vh; top: 0%; left: 0%; background-image: url('img/wp.jpg'); background-size: cover; background-repeat: no-repeat;"></div>
	<div class="main_container">
	<div class="section_content">
		<img src="img/logo.png" width="320px"><br>
		<img src="img/man.png" style="position: absolute; margin-left: 5px; margin-top: 9px;" width="19px">
		<input type="text" class="input_price" placeholder="<?=$username?>" disabled="disabled"><br>
		<img src="img/ruble.png" style="position: absolute; margin-left: 5px; margin-top: 20px;" width="19px">
		<input type="text" class="input_price" placeholder="<?=$get_amount?>" disabled="disabled" style="margin-top: 10px;"><br>
		<form method="post" action="https://payeer.com/merchant/">
		<input type="hidden" name="m_shop" value="<?=$m_shop?>">
		<input type="hidden" name="m_orderid" value="<?=$m_orderid?>">
		<input type="hidden" name="m_amount" value="<?=$m_amount?>">
		<input type="hidden" name="m_curr" value="<?=$m_curr?>">
		<input type="hidden" name="m_desc" value="<?=$m_desc?>">
		<input type="hidden" name="m_sign" value="<?=$sign?>">
		<input type="submit" class="input_button" name="m_proccess" value="Перейти к пополнению"></button>
		</form>
	</div>
	</div>
	<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
</body>
</html>