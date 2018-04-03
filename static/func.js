function currentYPosition() {
    // Firefox, Chrome, Opera, Safari
    if (self.pageYOffset) return self.pageYOffset;
    // Internet Explorer 6 - standards mode
    if (document.documentElement && document.documentElement.scrollTop)
        return document.documentElement.scrollTop;
    // Internet Explorer 6, 7 and 8
    if (document.body.scrollTop) return document.body.scrollTop;
    return 0;
}

function elmYPosition(eID) {
    var elm = document.getElementById(eID);
    var y = elm.offsetTop;
    var node = elm;
    while (node.offsetParent && node.offsetParent != document.body) {
        node = node.offsetParent;
        y += node.offsetTop;
    } return y;
}

function smoothScroll(eID) {
    var startY = currentYPosition();
    var stopY = elmYPosition(eID);
    var distance = stopY > startY ? stopY - startY : startY - stopY;
    // 
    stopY -= 50;
    if (distance < 100) {
        scrollTo(0, stopY); return;
    }
    var speed = Math.round(distance / 100);
    if (speed >= 20) speed = 20;
    var step = Math.round(distance / 25);
    var leapY = stopY > startY ? startY + step : startY - step;
    var timer = 0;
    if (stopY > startY) {
        for ( var i=startY; i<stopY; i+=step ) {
            setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
            leapY += step; if (leapY > stopY) leapY = stopY; timer++;
        } return;
    }
    for ( var i=startY; i>stopY; i-=step ) {
        setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
        leapY -= step; if (leapY < stopY) leapY = stopY; timer++;
    }
}
 
function toHref(e) {
    var str = e.target.href;
    var idx = str.lastIndexOf('#');
    if (idx >= 0) {
      var h = str.substring(idx+1);
      if ( h.length > 0 ) {
        //console.log(h);
        smoothScroll(h);
      }  
    }
}

function toTop() {
  smoothScroll('top');
}

function listen() {
  var lnk = document.querySelectorAll('.navbar a:not(.menu)');
  var lnkLen = lnk.length;
  for (var i=0; i < lnkLen; i++) {
    
    lnk[i].addEventListener('click', toHref);
  }
  var goup = document.querySelector('.go-top img');
  goup.addEventListener('click', toTop);
}

function onPageScroll() {
  var pos = currentYPosition();
  var upbtn = document.querySelector('.go-top');
  //console.log(pos);
  if (pos > 200) {
    upbtn.style.opacity = "0.9";
  } else {
    upbtn.style.opacity = "0.0";
  }
  if (pos >  2925) {
    upbtn.style.bottom = "135px";
  } else {
    upbtn.style.bottom = "10px";
  }
}

function bindScroll() {
  document.addEventListener('scroll', onPageScroll); 
}

addLoadListener(listen);
addLoadListener(bindScroll);