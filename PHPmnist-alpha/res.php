<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
	</head>
  	<body>
		<?php

			//一時ファイルができているか（アップロードされているか）チェック
			if(is_uploaded_file($_FILES['up_file']['tmp_name'])){

				//一時ファイルを保存ファイルにコピーできたか
				if(move_uploaded_file($_FILES['up_file']['tmp_name'],"./".$_FILES['up_file']['name'])){

					//正常
					$arg = $_FILES['up_file']['name'];
					echo "uploaded!<br/>";

					echo "<img src=$arg> <br/>";

					$cmd = "python3 ./tf-test.py $arg 2>&1 &"; 
					$res = exec($cmd, $output);

					$counter = 0;
					foreach ($output as $line) {
						if ($counter < 6){
							// てきとうわーにんぐかいひ
							$counter += 1;
							continue;
						}
						echo "$line\n";
					}
					//exec("rm -f $arg");
				}else{

					//コピーに失敗（だいたい、ディレクトリがないか、パーミッションエラー）
					echo "error while saving.";
				}

			}else{

				//そもそもファイルが来ていない。
				echo "file not uploaded.";

			}
		?>
	<button onclick="location.href='./index.php'">戻る</button>
	</body>
<html>