<html>
  <head>
    <meta charset="utf-8">
    <title>Plant Monitoring System</title>
    <link rel="icon" href="favicon.ico" type="image/x-icon"/>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Codystar&family=Nunito+Sans&family=Nunito&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">  </head>
  <body>
    <!-- PHP to connect MySQL
        Get info from the latest row -->
    <?php
      // Threshold Values
      $light_thresh_1 = 7;
      $light_thresh_2 = 12;
      $moisture_thresh_1 = 50;
      $moisture_thresh_2 = 62;

      $username = "pi";
      $password = "password"; // not real password
      $database = "test";

      $mysqli = new mysqli("localhost", $username, $password, $database);
      $query = "SELECT * FROM testtable order by tdate desc, ttime desc limit 1";
      if ($result=$mysqli->query($query)) {
        $lastrow = $result->fetch_assoc();
        $dispmoisture = $lastrow["moisture"];
        $displight = $lastrow["light"];
        $disptempurature = $lastrow["temperature"];
        $disphumidity = $lastrow["humidity"];
        $result->free();
      }
    ?>

    <!-- Title Div -->
    <div class="title">
      <img class="plant" src="images/plant.png" alt="plant image">
      <h1 class="plant">Plant Monitoring System (EE629-Spring 2021)</h1>
      <img class="plant" src="images/plant.png" alt="plant image">
    </div>
    <hr align="left">
    <!-- Monitor - Contains Icons and (Small) Database Table -->
    <div class="monitor">
      <div class="visual">
        <div class="sunlight">
          <h2>Brightness</h2>
          <!-- Display icon dependant on brightness-->
          <?php
            if($displight >$light_thresh_2) {
              echo '<img src="images/brightday3.png" alt="brightness indicator image">';
            }
            elseif($displight > $light_thresh_1) {
              echo '<img src="images/brightday2.png" alt="brightness indicator image">';
            }
            else {
              echo '<img src="images/brightday1.png" alt="brightness indicator image">';
            }
          ?>
        </div>
        <div class="water">
            <h2>Moisture</h2>
            <!-- Display icon dependant on moisture-->
            <?php
              if($dispmoisture >$moisture_thresh_2) {
                echo '<img src="images/water3.png" alt="water indicator image">';
              }
              elseif($dispmoisture > $moisture_thresh_1) {
                echo '<img src="images/water2.png" alt="water indicator image">';
              }
              else {
                echo '<img src="images/water1.png" alt="water indicator image">';
              }
            ?>
        </div>
        <br>
        <div class="temphum">
          <h2>Temperature and Humidity</h2>
          <img src="images/temp.png" alt="temp indicator image">
          <div class="temphuminfo">
            <!-- Print Temperature and Humidity-->
            <?php
              echo '<p>'. $disptempurature . ' F<br />' . $disphumidity . ' %</p>'
            ?>
          </div>
        </div>
      </div>

      <!-- Data -->
      <div class="data">
        <h2>Plant Data Info</h2>
        <!-- Display Small table from MySQL database-->
        <?php
          $mysqli = new mysqli("localhost", $username, $password, $database);
          $query = "SELECT * FROM testtable order by tdate desc, ttime desc limit 20";
          echo '<table>
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
      <hr class="margin20" align="left">
      <!-- Display Graphs from Images -->
      <div>
         <img class="graph" src="images/moisture.png" alt="graph moisture data">
         <img class="graph" src="images/light.png" alt="graph moisture data">
      </div>
      <div>
        <img class="graph" src="images/temperature.png" alt="graph moisture data">
        <img class="graph" src="images/humidity.png" alt="graph moisture data">
     </div>
    </div>
  </body>
</html>
