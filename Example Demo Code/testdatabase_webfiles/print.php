<?php
$username = "pi";
$password = "password"; // not real password
$database = "test";
$mysqli = new mysqli("localhost", $username, $password, $database);
$query = "SELECT * FROM testtable";


echo "<b><center>Database Output</center></b><br><br>";
echo "<b>Col1 Col2</b><br>";
if ($result = $mysqli->query($query)) {
    while ($row = $result->fetch_assoc()) {
        $field1name = $row["col1"];
        $field2name = $row["col2"];

	echo "" . $field1name . " " . $field2name . "<br>";
    }
    $result->free();
}
?>
