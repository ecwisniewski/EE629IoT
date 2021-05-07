<?php
$username = "pi";
$password = "password"; // not real password
$database = "test";
$mysqli = new mysqli("localhost", $username, $password, $database);
$query = "SELECT * FROM testtable";


echo "<b><center>Database Output</center></b><br><br>";
echo "<center>";
echo "<table><tr><td><b>Value1</b></td><td><b>Value2</b></td></tr>";
if ($result = $mysqli->query($query)) {
    while ($row = $result->fetch_assoc()) {
        $field1name = $row["col1"];
        $field2name = $row["col2"];

	echo "<tr><td>" . $field1name . "</td><td>" . $field2name . "</td></tr>";
    }
    $result->free();
}
echo "</table></center>";
?>
