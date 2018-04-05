import 'dart:html';
import '/home/seba/workspace/angryCss/lib/slider.dart';

void main() {
    Slider sl = new Slider('main-slider');
    String url = '/photos/lawncare';
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

    Slider mowing = new Slider('mowing-slider');
    mowing.addImage('/media/offer/mowing_01.jpg');
    mowing.addImage('/media/offer/mowing_02.jpg');
    mowing.animationNameNext = 'flipInY';
    mowing.animationNamePrev = 'slideInLeft';
    mowing.run();

    Slider fertilization = new Slider('fertilization-slider');
    fertilization.addImage('/media/offer/fertilization_01.jpg');
    fertilization.addImage('/media/offer/fertilization_02.jpg');
    fertilization.animationNameNext = 'flipInX';
    fertilization.animationNamePrev = 'slideInLeft';
    fertilization.run();
    //broadleaf
    Slider broadleaf = new Slider('broadleaf-slider');
    broadleaf.addImage('/media/offer/broad_leaf_01.jpg');
    broadleaf.addImage('/media/offer/broad_leaf_01.jpg');
    broadleaf.animationNameNext = 'flipInY';
    broadleaf.animationNamePrev = 'slideInLeft';
    broadleaf.run();
    //aeration
    Slider aeration = new Slider('aeration-slider');
    aeration.addImage('/media/offer/aeration_01.jpg');
    aeration.addImage('/media/offer/aeration_02.jpg');
    aeration.addImage('/media/offer/aeration_03.jpg');
    aeration.addImage('/media/offer/aeration_04.jpg');
    aeration.animationNameNext = 'flipInX';
    aeration.animationNamePrev = 'slideInLeft';
    aeration.run();
    //overseeding
    Slider overseeding = new Slider('overseeding-slider');
    overseeding.addImage('/media/offer/overseeding_01.jpg');
    overseeding.addImage('/media/offer/overseeding_02.jpg');
    overseeding.animationNameNext = 'flipInY';
    overseeding.animationNamePrev = 'slideInLeft';
    overseeding.run();
}
