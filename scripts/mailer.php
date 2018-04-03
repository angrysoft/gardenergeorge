<?php
    require 'scripts/class.phpmailer.php';
    require 'scripts/class.smtp.php';

    class Mailer {
        private $config;
        private $msg;

        function __construct() {
            $this->config = parse_ini_file('config/config.ini', true);
        }

        function printConfig() {
            foreach ($this->config["Email"] as $x => $val) {
                echo($x . ' = ' . $val) . PHP_EOL;
            }
        }

        function setMsg($m) {
            $this->msg = $m;
        }

        function getHtmlMsg() {
            $htmlHead = '<!DOCTYPE html>'
            . '<html lang="en_GB">'
            . '<head>'
            . '<meta charset="UTF-8">'
            . '<title>Message</title>'
            . '<style>tr:nth-child(even) {background-color: #f2f2f2}</style>'
            . '</head>'
            . '<body>'
            . '<table>';
            $htmlBody = '<tr><td>Name: </td><td>' . $this->msg["name"] . '</td></tr>'
            . '<tr><td>Email: </td><td>'. $this->msg["email"] . '</td></tr>'
            . '<tr><td>Address: </td><td>' . $this->msg["address"] . '</td></tr>'
            . '<tr><td>Phone: </td><td>' . $this->msg["phone"] . '</td></tr>';
            $about = array("search", "mouth", "advert", "social");
            $htmlBody .= '<tr><td>How did you hear about us?: </td><td>';
            foreach ( $about as $v) {
                if (array_key_exists($v, $this->msg)) {
                    switch ($v) {
                        case "search":
                            $m = "Google or other search";
                        break;
                        case "mouth":
                            $m = "Word of mouth";
                        break;
                        case "advert":
                            $m = "Advertisement";
                        break;
                        case "social":
                            $m = "Social media";
                        break;
                    }
                    $htmlBody .= $m . ', ';
                }
            }
            $htmlBody .= '</td></tr>';
            $htmlBody .= '<tr><td>Message: </td><td>' . nl2br($this->msg["msg"]) . '</td></tr>';
            if (array_key_exists("mailagree", $this->msg)) {
                $mailagree = "Yes";
            } else {
                $mailagree = "No";
            }
            $htmlBody .= '<tr><td>I consent to receiving messages: </td><td>' . $mailagree . '</td></tr>';
            $htmlEnd = '</table>'
            . '</body>'
            . '</html>';

            return $htmlHead . $htmlBody . $htmlEnd;
        }

        function getTextMsg() {
            $txt = 'Name: ' . $this->msg["name"] . PHP_EOL
            . 'Email: '. $this->msg["email"] . PHP_EOL
            . 'Address: ' . $this->msg["address"] . PHP_EOL
            . 'Phone: ' . $this->msg["phone"] . PHP_EOL;
            $about = array("search", "mouth", "advert", "social");
            $txt .= 'How did you hear about us?: ';
            foreach ( $about as $v) {
                if (array_key_exists($v, $this->msg)) {
                    switch ($v) {
                        case "search":
                            $m = "Google or other search";
                        break;
                        case "mouth":
                            $m = "Word of mouth";
                        break;
                        case "advert":
                            $m = "Advertisement";
                        break;
                        case "social":
                            $m = "Social media";
                        break;
                    }
                    $txt .= $m . ', ';
                }
            }
            $txt .= PHP_EOL;
            $txt .= 'Message: ' . $this->msg["msg"];
            if (array_key_exists("mailagree", $this->msg)) {
                $mailagree = "Yes";
            } else {
                $mailagree = "No";
            }
            $htmlBody .= 'I consent to receiving messages:' . $mailagree . PHP_EOL;

            return $txt;
        }

        function sendEmail() {
            $mail = new PHPMailer;
            $mail->isSMTP();
            $mail->Host = $this->config["Email"]["server"];
            $mail->SMTPAuth = true;
            $mail->Username = $this->config["Email"]["user"];
            $mail->Password = $this->config["Email"]["password"];
            $mail->SMTPSecure = $this->config["Email"]["encryption"];
            $mail->Port = $this->config["Email"]["port"];
            $mail->setFrom($this->config["Email"]["from"], 'Mailer');
            $mail->isHTML(true);

            $mail->addAddress($this->config["Email"]["sendto"]);

            $mail->Subject = 'Contact Message from Webpage';
            $mail->Body    = $this->getHtmlMsg();
            $mail->AltBody = $this->getTextMsg();

            if(!$mail->send()) {
                return $mail->ErrorInfo;
            } else {
                return 'ok';
            }
        }

    }

?>
