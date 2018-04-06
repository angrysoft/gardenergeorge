import 'dart:html';
import 'dart:convert';
import '/home/seba/workspace/angryCss/lib/slider.dart';

void main() {
    Slider sl = new Slider('main-slider');
    String url = '/photos/lawncare';
    HttpRequest.getString(url)
    .then((String photos) {
      if (photos.isNotEmpty) {
        List<String> urls = JSON.decode(photos);
        for (String img in urls) {
            sl.addImage(img);
        }
        sl.animationNameNext = 'slideInRight';
        sl.animationNamePrev = 'slideInLeft';
        sl.run();
      }
    })
    .catchError((Error error) {
      print(error.toString());
    });

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
