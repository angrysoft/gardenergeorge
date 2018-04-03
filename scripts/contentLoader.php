<?php
    function loadHtml($name) {
        switch ($name) {
            case "menu":
                getFile("menu.html");
            break;
            case "footer":
                getFile("footer.html");
            break;
        }
    }

    function getFile($fname) {
        $fileName = "templates/" . basename($fname);
        $file = fopen($fileName, "r") or die ("file not found $fileName");
        echo fread($file, filesize($fileName));
        fclose($file);
    }
?>
