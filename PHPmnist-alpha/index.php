<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="ja">
<head>
<meta http-equiv="Content-Type" 
        content="text/html; charset=Shift_Jis">
<title>PHP入門</title>
</head>

<body>
<p>今日は、<?php echo date("Y/m/d"); ?> です。</p>


<form method="post" action="res.php" enctype="multipart/form-data">
ファイル:<input type="file" name="up_file">
<input type="submit" value="upload">
</form>
</body>
</html>