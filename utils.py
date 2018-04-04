import os
import smtplib
import re
import json
import urllib.request
import urllib.parse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from unicodedata import normalize
from time import gmtime
from shutil import move

class SendEmail:
    """Class SendEmail"""

    def __init__(self, srvAddr, user, password, port=25, encryption=''):
        """Constructor for SendEmail"""
        self.encryption = encryption
        self.msg = MIMEMultipart()
        self.txtMsg = ''
        self.htmlMsg = ''
        self.user = user
        self.password = password
        self.srvAddr = srvAddr
        self.port = port
        self.server = smtplib.SMTP()
        self.server.set_debuglevel(0)

    def addHtmlContent(self, m):
        """addMsg"""
        self.htmlMsg = MIMEText(m, 'html')

    def addTextContent(self, m):
        """addTextContent"""
        self.txtMsg = MIMEText(m, 'plain')

    def addSubject(self, s):
        """"""
        self.msg['Subject'] = s

    def addAddrFrom(self, a):
        """addAddrFrom"""
        self.msg['from'] = a

    def addAddrReplyTo(self, a):
        """addAddrFrom"""
        self.msg['reply-to'] = a

    def addAddrTo(self, a):
        """addAddrTo"""
        if type(a) == list:
            self.msg['to'] = ','.join(a)
        else:
            self.msg['to'] = a

    def addImgAtch(self, filename):
        """addAtchement"""
        if not os.path.exists(filename):
            return
        with open(filename, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
            self.msg.attach(img)

    def send(self):
        """send"""
        if self.htmlMsg:
            self.msg.attach(self.htmlMsg)
        elif self.txtMsg:
            self.msg.attach(self.txtMsg)

        if not self.msg['to'] and not self.msg['from']:
            raise Exception('sender')
        try:
            self.server.connect(self.srvAddr, self.port)
            if self.encryption.lower() == 'tls':
                self.server.ehlo()
                self.server.starttls()
                self.server.ehlo()
            self.server.login(self.user, self.password)
        except:
            raise Exception('login')
        try:
            ret = self.server.send_message(self.msg)
        except:
            raise Exception('sendmail')
        self.server.quit()
        return ret


def dictToString(d):
    """dictToString"""
    ret = ''
    for x in d:
        if x == 'g-recaptcha-response':
            continue
        ret += '{0:<20}: {1}\n'.format(x, d[x])
    return ret


class FilesManager:
    allowPath = {'files': 'static/graphic/files',
                 'news': 'static/graphic/news',
                 'sponsors': 'static/graphic/sponsors',
                 'wolontariusze': 'static/graphic/wolontariusze',
                 'zespol': 'static/graphic/zespol',
                 'albums': 'static/graphic/albums',
                 'tmp': '/tmp'}

    def __init__(self):
        pass

    def getFileList(self, path):
        if path not in self.allowPath:
            raise Exception('Path not allowed')

        files = list()
        for fn in os.listdir(self.allowPath[path]):
            if fn.startswith('.gitkeep'):
                continue
            fileGmtime = gmtime(os.path.getmtime(os.path.join(self.allowPath[path], fn)))
            fileTime = '{day}.{month}.{year} {h}:{min}:{sec}'.format(day=fileGmtime.tm_mday,
                                                                     month=fileGmtime.tm_mon,
                                                                     year=fileGmtime.tm_year,
                                                                     h=fileGmtime.tm_hour,
                                                                     min=fileGmtime.tm_min,
                                                                     sec=fileGmtime.tm_sec)
            files.append({'name': fn,
                          'url': os.path.join('/', self.allowPath[path], fn),
                          'date': fileTime})
        return files

    def saveFilesList(self, filesList, filePath, override=False):
        """saveFile zapisuje liste plików"""
        for f in filesList:
            self.saveFile(filePath, f, override=override)
        return 'ok'

    def saveFile(self, path, fileObj, override=False):
        """saveFile"""
        if path not in self.allowPath:
            raise Exception('Path not allowed')

        fname = self.secureFilename(fileObj.filename)
        if fname.find('.') < 0:
            raise Exception('File type not allowed : {}'.format(fname))

        prefix, suffix = fname.rsplit('.', 1)
        if not self.allowedFileExt(suffix):
            raise Exception('File type not allowed : {}'.format(fname))

        filePath = os.path.join(self.allowPath['tmp'], fname)
        fileObj.save(filePath)
        if path == 'news' or path == 'sponsor':
            if self.imageThumbnail(filePath, 250):
                filePath = os.path.join(self.allowPath['tmp'],
                                        '{}_thumb.{}'.format(prefix, suffix))
        thumbName = '{}_thumb.{}'.format(prefix, suffix)
        if not override:
            destFilePath = self.getFileName(self.allowPath[path], thumbName)
        else:
            destFilePath = os.path.join(self.allowPath[path], thumbName)
        move(filePath, destFilePath)
        return destFilePath

    def imageThumbnail(self, filePath, width):
        prefix, suffix = filePath.rsplit('.', 1)
        ret = os.system('convert -thumbnail {width} {imgIn} {imgOut}_thumb.{ext}'.format(
                        width=width,
                        imgIn=filePath,
                        imgOut=prefix,
                        ext=suffix))
        if not ret:
            return True
        else:
            return False

    def allowedFileExt(self, ext):
        if ext.lower() in ['jpg', 'jpeg', 'png', 'webm', 'gif']:
            return True
        else:
            return False

    def deleteFilesList(self, filesList, path):
        """deleteFile arg: fileListDict {path: fileName}"""
        # TODO mozna dodać zwracanie słownika ze statusem czy plik został usuniety czy nie
        for fileName in filesList:
            self.deleteFile(fileName, path)
        return 'ok'

    def deleteFile(self, fileName, path):
        """deleteFile"""
        if path not in self.allowPath:
            raise Exception('Path not allowed')
        filePath = os.path.join(self.allowPath[path], self.secureFilename(fileName))
        if os.path.exists(filePath):
            os.remove(filePath)
            return True
        else:
            return False

    @staticmethod
    def secureFilename(fileName):
        """secureFilename"""
        _windows_device_files = ('CON', 'AUX', 'COM1', 'COM2', 'COM3', 'COM4', 'LPT1', 'LPT2', 'LPT3', 'PRN', 'NUL')
        allowChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
        fileName = normalize('NFKD', fileName).encode('ascii', 'ignore')
        fileName = fileName.decode('ascii')
        newFileName = ''
        for c in fileName:
            if c in allowChar:
                newFileName += c
        newFileName = newFileName.strip('._')
        if os.name == 'nt' and newFileName and newFileName.split('.')[0].upper() in _windows_device_files:
            newFileName = '_' + newFileName

        return newFileName

    @staticmethod
    def getFileName(path, fName):
        """getFileName"""
        i = 1
        fileName = FilesManager.secureFilename(fName)
        while os.path.exists(os.path.join(path, fileName)):
            if fileName.find('.') > 0:
                prefix, suffix = fileName.rsplit('.', 1)
            else:
                prefix = fileName
                suffix = 'junk'
            m = re.search("(_.*$)", prefix)
            if m:
                prefix = prefix.replace(m.group(0), '')
            fileName = '{0}_{1}.{2}'.format(prefix, i, suffix)
            i += 1
        return os.path.join(path, fileName)


def verifyCaptcha(secret, gresponse):
    """verifyCaptcha"""
    if not gresponse:
        return False
    data = urllib.parse.urlencode({'secret': secret,
                                   'response': gresponse})
    url = 'https://www.google.com/recaptcha/api/siteverify'
    ret = False
    try:
        with urllib.request.urlopen(url, data=data.encode('ascii')) as resp:
            if resp.getcode() == 200:
                answer = json.loads(resp.read().decode())
                if type(answer['success']) == bool:
                    ret = answer['success']
                elif (answer['success']) == 'true':
                    ret = True
    except urllib.error.HTTPError as err:
        print(err.msg)

    return ret


def secureLinkName(linkName):
    """secureFilename"""
    allowChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
    linkName = normalize('NFKC', linkName)
    linkName = '_'.join(linkName.split())
    pl = {'ę': 'e',
          'ó': 'o',
          'ą': 'a',
          'ś': 's',
          'ł': 'l',
          'ż': 'z',
          'ź': 'z',
          'ć': 'c',
          'ń': 'n',
          'ø': 'o'}
    newLinkName = ''

    for c in linkName:
        c = c.lower()
        if c in pl:
            c = pl.get(c)
        if c in allowChar:
            newLinkName += c
    return newLinkName


def getPlaceDetails(placeId, apiKey):
    """Google place details"""

    data = urllib.parse.urlencode({'placeid': placeId,
                                   'key': apiKey})
    print(data)
    url = 'https://maps.googleapis.com/maps/api/place/details/json'
    ret = None
    try:
        with urllib.request.urlopen(url, data=data.encode('ascii')) as resp:
            if resp.getcode() == 200:
                answer = json.loads(resp.read().decode())
                print(answer)
                if answer.get('status') == 'OK':
                    ret = answer.get('reviews')
    except urllib.error.HTTPError as err:
        print(err.msg)

    return ret