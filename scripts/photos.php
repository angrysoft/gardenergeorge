<?php
class Photos {

    function getPhotosFromDir($dir) {
        $ret = array();
        if (is_dir($dir)) {
            if ($dh = opendir($dir)){
                while (($file = readdir($dh)) !== false) {
                    if ($file[0] == '.') {
                        continue;
                    }

                    if ($this->isPhoto($file)) {
                        array_push($ret, "$dir/$file");
                    } else {
                        echo $file;
                    }

                }
                closedir($dh);
                return $ret;
            }
        }
    }

    function getExtension($filename) {
        if ($pos = strripos($filename, '.')) {
            return substr($filename, $pos + 1);
        }
    }

    function isPhoto($file) {
        $ext = $this->getExtension($file);
        switch (strtolower($ext)) {
            case "jpg":
                $ret = true;
            break;
            case "jpeg":
                $ret = true;
            break;
            case "png":
                $ret = true;
            break;
            default:
                $ret = false;
        }
        return $ret;
    }
}
?>
