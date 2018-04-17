import 'dart:html';
import '/home/seba/workspace/angryCss/lib/smoothscrollto.dart';
import '/home/seba/workspace/angryCss/lib/debounce.dart';

void onPageScroll() {
  var pos = window.scrollY;
  var upbtn = querySelector('.go-top');

  if (pos > 200) {
    upbtn.style.pointerEvents = 'auto';
    upbtn.style.opacity = "0.9";


  } else {
    upbtn.style.pointerEvents = 'none';
    upbtn.style.opacity = "0.0";
  }

}

void fixedMenu() {
	int pos = window.scrollY;
	Element navbar = querySelector('nav.navbar');
	if (pos > 300) {
	navbar.classes.remove('fadeIn');
    navbar.classes.add('fadeInDown');
    navbar.classes.add('fixed-menu');
  } else if (pos < 300) {
  	navbar.classes.remove('fadeInDown');
  	navbar.classes.add('fadeIn');
    navbar.classes.remove('fixed-menu');
  }
}

void menuOnClick() {
  Element nav = querySelector('nav.navbar');
  nav.classes.toggle('show-menu');
}

void main() {
  Location loc = window.location;
  String basePath = loc.pathname.split('/').last;
  if (basePath.isEmpty) {
    basePath = 'about';
  }
  String id = "#${basePath}-menu";
  LinkElement menuLink = querySelector(id);
  if (menuLink != null) {
    menuLink.classes.add('active');
    if (basePath == 'about') {
      menuLink.href = '#about';
    }
  }

  Debounce sc = new Debounce(onPageScroll, 250);
  Debounce fmenu = new Debounce(fixedMenu, 250);
  SmoothScrollTo scroll = new SmoothScrollTo();
  querySelector('.go-top img').onClick.listen((event) => scroll.click('#top'));
  window.onScroll.listen((event) {
  	sc.tick();
  	fmenu.tick();
  });
  // roll down menu in mobile layout
  querySelector('nav.navbar .menu').onClick.listen((Event e) => menuOnClick());
  List<Element> anchors = querySelectorAll('nav.navbar > div > a');
  anchors.forEach((el) {
    el.onClick.listen((Event e) {
      AnchorElement a = e.target;
    	if (a.hash.isNotEmpty) {
      		e.preventDefault();
      		scroll.click(a.hash);
      }
    });
  });
}
