<html>

<link rel="stylesheet" type="text/css" href="style.css">
<body>

 <?php 
 $data = file_get_contents ('data.json');
 $json = json_decode($data,true);  ?>         

<?php for($i=0;$i<41;$i++){  ?>
<div><?php  print_r($json[0]['trends'][$i]['name']);    ?>
<?php  echo nl2br ("\n");   ?>
<?php  print_r($json[0]['trends'][$i]['url']);   ?>
<p> <?php  echo nl2br ("\n");} ?> </p>

</div>


</body>


</html>