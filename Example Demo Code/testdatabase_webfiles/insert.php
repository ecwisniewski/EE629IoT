<!-- https://www.siteground.com/tutorials/php-mysql/display-table-data/ -->
<?php
$username = "pi";
$password = "password"; // not a real password
$database = "test";

$mysqli = new mysqli("localhost",$username, $password, $database);

// Properly escape values

$field1 = $mysqli->real_escape_string($_POST['field1']);
$field2 = $mysqli->real_escape_string($_POST['field2']);

$query = "INSERT INTO testtable (col1, col2) VALUES ('{$field1}','{$field2}')";

$mysqli->query($query);
$mysqli->close();

header("Location: http://192.168.1.15/printtable.php"); // Local IP
exit();

?>
