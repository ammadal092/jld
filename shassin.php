<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Pilih Folder</title>
</head>
<body>
<?php
$baseFolder = '漢字/';

if (isset($_GET['kanji'])) {
    $input = $_GET['kanji'];
    $chars = preg_split('//u', $input, -1, PREG_SPLIT_NO_EMPTY); // pisah per karakter UTF-8

    $foundFolders = [];

    // Cari folder yang cocok
    foreach ($chars as $char) {
        $folderPath = $baseFolder . $char;
        if (is_dir($folderPath)) {
            $foundFolders[] = $char;
        }
    }

    // Jika input hanya 1 karakter atau user pilih salah satu folder
    if (mb_strlen($input, 'UTF-8') === 1) {
        $selected = $input;
        $files = glob($baseFolder . $selected . '/*.jpg');
        echo "<h2>Menampilkan gambar dari folder: $selected</h2>";
        if (!empty($files)) {
            echo "<img src='" . $files[0] . "' alt='Gambar' style='width:500px;'>";
        } else {
            echo "<p style='color:red;'>Tidak ada file .jpg ditemukan.</p>";
        }

        // Link kembali ke daftar folder jika berasal dari input multi-kanji
        if (isset($_GET['source'])) {
            $originalInput = $_GET['source'];
            echo "<br><br><a href='?kanji=" . urlencode($originalInput) . "'>🔄 Kembali ke Daftar Folder</a>";
        }

    } elseif (count($foundFolders) > 1) {
        echo "<h2>Pilih Folder yang Diinginkan</h2>";
        echo "<ul>";
        foreach ($foundFolders as $char) {
            // Kirim juga sumber input aslinya (untuk bisa undo)
            echo "<li><a href='?kanji=" . urlencode($char) . "&source=" . urlencode($input) . "'>📂 Folder: $char</a></li>";
        }
        echo "</ul>";
    } elseif (count($foundFolders) === 1) {
        // Hanya satu folder cocok, langsung tampilkan
        $selected = $foundFolders[0];
        $files = glob($baseFolder . $selected . '/*.jpg');
        echo "<h2>Menampilkan gambar dari folder: $selected</h2>";
        if (!empty($files)) {
            echo "<img src='" . $files[0] . "' alt='Gambar' style='width:500px;'>";
        } else {
            echo "<p style='color:red;'>Tidak ada file .jpg ditemukan.</p>";
        }
    } else {
        echo "<p style='color:red;'>Tidak ada folder cocok dengan karakter yang dimasukkan.</p>";
    }
}
?>

<br><br>
<a href="form.html">🔙 Kembali ke Form</a>
</body>
</html>
