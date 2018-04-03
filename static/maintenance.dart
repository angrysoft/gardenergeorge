import 'dart:html';
import '/home/seba/workspace/angryCss/lib/slider.dart';

void main() {
    Slider sl = new Slider('main-slider');
    String url = '/getphotos.php?dir=gardenmaintenance';
    HttpRequest http = new HttpRequest();
    http.onReadyStateChange.listen((Event e) {
    if (http.readyState == HttpRequest.DONE &&
        (http.status == 200 || http.status == 0)) {
      var ret = http.responseText;
      if ( ret.isNotEmpty && ret.indexOf(';') >= 0) {
        for (String img in ret.split(";")) {
            sl.addImage(img);
        }
        sl.animationNameNext = 'slideInRight';
        sl.animationNamePrev = 'slideInLeft';
        sl.run();
      }
    }
    });
    http.open('GET', url, async: true);
    http.send();

    Slider maintenance = new Slider('maintenance-slider');
    maintenance.addImage('/media/offer/maintenance_01.jpg');
    maintenance.addImage('/media/offer/maintenance_02.jpg');
    maintenance.animationNameNext = 'flipInX';
    maintenance.animationNamePrev = 'slideInLeft';
    maintenance.run();

    Slider restoring = new Slider('restoring-slider');
    restoring.addImage('/media/offer/restoring_01.jpg');
    restoring.addImage('/media/offer/restoring_02.jpg');
    restoring.addImage('/media/offer/restoring_03.jpg');
    restoring.animationNameNext = 'flipInY';
    restoring.animationNamePrev = 'slideInLeft';
    restoring.run();

    Slider hedging = new Slider('hedging-slider');
    hedging.addImage('/media/offer/hedging_01.jpg');
    hedging.addImage('/media/offer/hedging_02.jpg');
    hedging.addImage('/media/offer/hedging_03.jpg');
    hedging.animationNameNext = 'flipInX';
    hedging.animationNamePrev = 'slideInLeft';
    hedging.run();

    Slider turfing = new Slider('turfing-slider');
    turfing.addImage('/media/offer/turfing_01.jpg');
    turfing.addImage('/media/offer/turfing_02.jpg');
    turfing.addImage('/media/offer/turfing_03.jpg');
    turfing.animationNameNext = 'flipInY';
    turfing.animationNamePrev = 'slideInLeft';
    turfing.run();

    Slider planting = new Slider('planting-slider');
    planting.addImage('/media/offer/planting_01.jpg');
    planting.addImage('/media/offer/planting_02.jpg');
    planting.animationNameNext = 'flipInX';
    planting.animationNamePrev = 'slideInLeft';
    planting.run();

    Slider landscapeing = new Slider('landscapeing-slider');
    landscapeing.addImage('/media/offer/landscapeing_01.jpg');
    landscapeing.addImage('/media/offer/landscapeing_02.jpg');
    landscapeing.addImage('/media/offer/landscapeing_03.jpg');
    landscapeing.animationNameNext = 'flipInY';
    landscapeing.animationNamePrev = 'slideInLeft';
    landscapeing.run();

    Slider powerwashing = new Slider('powerwashing-slider');
    powerwashing.addImage('/media/offer/powerwashing_01.jpg');
    powerwashing.addImage('/media/offer/powerwashing_02.jpg');
    powerwashing.addImage('/media/offer/powerwashing_03.jpg');
    powerwashing.addImage('/media/offer/powerwashing_04.jpg');
    powerwashing.addImage('/media/offer/powerwashing_05.jpg');
    powerwashing.animationNameNext = 'flipInX';
    powerwashing.animationNamePrev = 'slideInLeft';
    powerwashing.run();

}
