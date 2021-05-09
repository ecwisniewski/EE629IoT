<html>
  <head>
    <meta charset="utf-8">
    <title>Plant Monitoring Data</title>
    <link rel="icon" href="favicon.ico"/>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Amaranth&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
</head>
  <body>
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
      $query = "SELECT * FROM testtable";
      $firstrow = $result->fetch_assoc();

      $dispmoisture = $firstrow["moisture"]
      $displight = $firstrow["light"]
      $disptempurature = first$row["temperature"]
      $disphumidity = $firstrow["humidity"]
    ?>

    <div class="title">

      <img class="plant" src="images/plant.png" alt="plant image">
      <h1 class="plant">Plant Monitoring System (EE629-Spring 2021)</h1>
      <img class="plant" src="images/plant.png" alt="plant image">
      </div>
      <hr>
      <div class="monitor">


      <div class="visual">
        <div class="sunlight">
          <h2>Brightness</h2>
          <?php
          if($displight >$light_thresh_2) {
            echo '<img src="images/brightday3.png" alt="brightness indicator image">';
          }
          else if($displight > $light_thresh_1) {
            echo '<img src="images/brightday2.png" alt="brightness indicator image">';

          }
          else {
            echo '<img src="images/brightday1.png" alt="brightness indicator image">';

          }
          ?>
        </div>

      <div class="water">
          <h2>Moisture</h2>
          <?php
          if($dispmoisture >$moisture_thresh_2) {
            echo '<img src="images/water3.png" alt="water indicator image">';
          }
          else if($dispmoisture > $moisture_thresh_1) {
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
            <?php
              echo '<p>
              '. $disptempurature . ' F<br />' . $disphumidity . '
               %</p>'
             ?>
          </div>
        </div>

      </div>
      <!--<hr>-->
      <div class="data">
        <h2>Plant Data Info</h2>


      <?php
      echo '<table>
              <tr>
                <td><b>Date</b></td>
                <td><b>Time</b></td>
                <td><b>Moisture</b></td>
                <td><b>Light</b></td>
                <td><b>Temperature</b></td>
                <td><b>Humidty</b></td>
              </tr>';
      if ($result = $mysqli->query($query)) {
         while ($row = $result->fetch_assoc()) {

              $date = $row["tdate"]
              $time = $row["ttime"]
              $moisture = $row["moisture"]
              $light = $row["light"]
              $tempurature = $row["temperature"]
              $humidity = $row["humidity"]
      	echo '<tr>
              <td>' . $date . '</td>
              <td>' . $time . '</td>
              <td>' . $moisture . '</td>
              <td>' . $light . '</td>
              <td>' . $tempurature . 'F</td>
              <td>' . $humidity . '%</td>
              </tr>';
          }
          $result->free();
      }
      echo '</table>';
    ?>
  </div>

  </div>
    <hr>
  </body>
</html>
