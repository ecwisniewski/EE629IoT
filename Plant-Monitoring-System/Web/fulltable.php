<html>
  <head>
    <meta charset="utf-8">
    <title>Plant Monitoring System</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon"/>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Codystar&family=Nunito+Sans&family=Nunito&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">  
  </head>
  <body>
    <?php
      $username = "pi";
      $password = "password"; // not real password
      $database = "database";
    ?>
    <!-- Title Div -->
    <div class="title">
      <img class="plant" src="images/plant.png" alt="plant image">
      <h1 class="plant">Plant Monitoring System (EE629-Spring 2021)</h1>
      <img class="plant" src="images/plant.png" alt="plant image">
    </div>
    <hr align="left">
    <!-- Database -->
    <div class="full-data">
      <h2>Plant Data Full Info</h2>
      <?php
        $mysqli = new mysqli("localhost", $username, $password, $database);
        $query = "SELECT * FROM testtable order by tdate desc, ttime desc limit 60";
        echo '<table style="width:1000px">
              <tr>
                <td><b>Date</b></td>
                <td><b>Time</b></td>
                <td><b>Moisture</b></td>
                <td><b>Light</b></td>
                <td><b>Temperature</b></td>
                <td><b>Humidity</b></td>
              </tr>';

          if ($result=$mysqli->query($query)) {
            while($row = $result->fetch_assoc()) {

              echo '<tr>
                      <td>' . $row["tdate"] . '</td>
                      <td>' . $row["ttime"] . '</td>
                      <td>' . $row["moisture"] . '</td>
                      <td>' . $row["light"] . '</td>
                      <td>' . $row["temperature"] . 'F</td>
                      <td>' . $row["humidity"] . '%</td>
                    </tr>';
            }

            $result->free();
          }

          echo '</table>';
        ?>
      </div>
    </div>
  </body>
</html>
