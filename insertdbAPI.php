<?php
$dbhost = '127.0.0.1';
$dbuser = 'root';
$dbpass = '*******';
$dbname = 'crawler_data';
$mysqli = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
//mysqli 預設編號為latin-1，建立資料庫已指定utf8編碼，所以要指定連線時所用編碼
$mysqli->query("SET NAMES utf8");

echo "start to upload"."\n";
echo "------------------------------------------"."\n";
$filename = "WeatherList.txt";
$str = "";
//判斷是否有該檔案
if (file_exists($filename)) {
	$file = fopen($filename, "r");
    if ($file != null) {
        //當檔案未執行到最後一筆，迴圈繼續執行(fgets一次抓一行)
        while (!feof($file)) {
            $str .= fgets($file);
        }
        fclose($file);
	}
}
else{
	echo 'There is no file'."\n";
}
$str = explode("{",$str);
foreach ($str as $key => &$value) {
    //去除最後一個字元 '}'
    $value = substr($value,0,-1);
    if(!$value) continue;
    //再以,分隔
    $colum = explode(",",$value);
    //去除多餘的"並分割出每個縣市的資訊
    $city = explode(":",str_replace('"',"",$colum[0]));
    $date = explode(":",str_replace('"',"",$colum[1]));
    $day = explode(":",str_replace('"',"",$colum[2]));
    $night = explode(":",str_replace('"',"",$colum[3]));
    //把每筆資料insert到DB
    $sql = "INSERT INTO weather (city, date, day, night) VALUES (?, ?, ?, ?)";
    $stmt = $mysqli->prepare($sql);
    $stmt->bind_param('ssss',$city[1],$date[1],$day[1],$night[1]);
    $stmt->execute();
}
?>
