<?php
if (!in_array($_SERVER['REMOTE_ADDR'], array('185.71.65.92', '185.71.65.189', '149.202.17.210'))) return;

if (isset($_POST['m_operation_id']) && isset($_POST['m_sign']))
{
	$m_key = 'EJ6kSB#3&Fxs';

	$arHash = array(
		$_POST['m_operation_id'],
		$_POST['m_operation_ps'],
		$_POST['m_operation_date'],
		$_POST['m_operation_pay_date'],
		$_POST['m_shop'],
		$_POST['m_orderid'],
		$_POST['m_amount'],
		$_POST['m_curr'],
		$_POST['m_desc'],
		$_POST['m_status']
	);

	if (isset($_POST['m_params']))
	{
		$arHash[] = $_POST['m_params'];
	}

	$arHash[] = $m_key;

	$sign_hash = strtoupper(hash('sha256', implode(':', $arHash)));

	if ($_POST['m_sign'] == $sign_hash && $_POST['m_status'] == 'success')
	{
		include "includes/db.php";
		$amount = $_POST['m_amount'];
		$user_id = $_POST['m_orderid'];
		$sql = "SELECT * FROM `accounts` WHERE `user_id` = '$user_id' LIMIT 1";
		$query = $conn->query($sql);
		if($query->num_rows > 0){
			$user_row = $query->fetch_array();
			$balance = $user_row['balance'];
			$balance += $amount;
			$update = "UPDATE `accounts` SET `balance` = '$balance' WHERE `user_id` = '$user_id' LIMIT 1";
			$conn->query($update);
			$update_deposit = "UPDATE `deposit` SET `status` = 1 WHERE `user_id` = '$user_id' LIMIT 1";
			$conn->query($update_deposit);
			$get_referal = "SELECT * FROM `referals` WHERE `referal_id` = '$user_id' LIMIT 1";
			$get_referal_sql = $conn->query($get_referal);
			if($get_referal_sql->num_rows > 0){
				$fetch_referal = $get_referal_sql->fetch_array();
				$referal_user = $fetch_referal['user_id'];
				$referal_earning = $fetch_referal['earnings'];
				$referal_bonus = round(($amount / 100) * 10);
				$referal_earning += $referal_bonus;
				$referal_account = "SELECT * FROM `accounts` WHERE `user_id` = '$referal_user' LIMIT 1";
				$referal_sql = $conn->query($referal_account);
				if($referal_sql->num_rows > 0){
					$referal_account_fetch = $referal_sql->fetch_array();
					$referal_account_balance = $referal_account_fetch['balance'];
					$referal_account_balance += $referal_bonus;
					$update_give_bonus = "UPDATE `accounts` SET `balance` = '$referal_account_balance' WHERE `user_id` = '$referal_user' LIMIT 1";
					$conn->query($update_give_bonus);
					$update_referals_tables = "UPDATE `referals` SET `earnings` = '$referal_earning' WHERE `referal_id` = '$user_id' LIMIT 1";
					$conn->query($update_referals_tables);
				}
			}
		}
		ob_end_clean();
	}

	ob_end_clean(); exit($_POST['m_orderid'].'|error');
}
?>