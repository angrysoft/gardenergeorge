<?php
    require "scripts/mailer.php";
    function checkCaptcha() {
        $secret = "6LcQcRMUAAAAAImTTo8Hi-HCv_U8J-K3-Zq2oto0";
        $verifyResponse = file_get_contents('https://www.google.com/recaptcha/api/siteverify?secret='.$secret.'&response='.$_POST['g-recaptcha-response']);
        $responseData = json_decode($verifyResponse);
        if($responseData->success) {
            return 1;
        } else {
            return 0;
        }
    }

if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if ($_POST["g-recaptcha-response"]) {
            if (checkCaptcha()) {
                $m = new Mailer;
                $m->setMsg($_POST);
                $ret = $m->sendEmail();
                if ( $ret == 'ok') {
                    header("Location: /freequote.html");
                } else {
                    echo "Error sending message : " . $ret;
                }

            }
    }
}
?>
