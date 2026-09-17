
<?php
$nameErr = $passwordErr = "";
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
  if (empty($_POST["username"])) {
    $nameErr = "Username is required";
  }

  if (empty($_POST["password"])) {
    $passwordErr = "Password is required";
  }

  

}
?>

<html>
  <body>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
      <div>
        <label for="username"><strong>Username</strong></label><br>
        <input type="text" id="username" name="username">
        <span class="error">* <?php echo $nameErr;?></span>
      </div>

      <div>
        <label for="password"><strong>Password</strong></label><br>
        <input type="password" id="password" name="password">
        <span class="error">* <?php echo $passwordErr;?></span>
      </div>
      </div>

      <button type="submit">Submit</button>
    </form>

    <div>
        <a href="register.php">Register for new account</a>
    </div>
  </body>
</html>