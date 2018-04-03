<?php
    include "scripts/photos.php";

    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        $dir = $_GET["dir"];

        $ph = new Photos;
        switch ($dir) {
            case "lawncare":
                $photos = $ph->getPhotosFromDir('media/lawncare');
            break;

            case 'gardenmaintenance':
                $photos = $ph->getPhotosFromDir('media/gardenmaintenance');
            break;
        }
        echo join(";",$photos);
    }
?>
