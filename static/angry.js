function menuToggle() {
    var li = document.querySelector('nav.navbar');
    li.classList.toggle('show-menu');
}


function menuOnClick() {
    var m = document.querySelector('.navbar .menu');
    if (m) {
        m.addEventListener('click', menuToggle);
    }
    
}

function addLoadListener(fn) {
  //mozilla and friends
  if (typeof window.addEventListener != 'undefined') {
    window.addEventListener('load', fn, false);
  }
  //opera
  else if (typeof document.addEventListener != 'undefined') {
    document.addEventListener('load', fn, false);
  }
  //innernetz exploder
  else if (typeof window.attachEvent != 'undefined') {
    window.attachEvent('onload', fn);
  }
}

function showModal(id) {
	document.querySelector(id).classList.add('modal-show');
}
function hideModal(id) {
    document.querySelector(id).classList.remove('modal-show');
	
}

// Returns a function, that, as long as it continues to be invoked, will not
// be triggered. The function will be called after it stops being called for
// N milliseconds. If `immediate` is passed, trigger the function on the
// leading edge, instead of the trailing.
function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

//var myEfficientFn = debounce(function() {
	// All the taxing stuff you do
//}, 250);

//window.addEventListener('resize', myEfficientFn);

addLoadListener(menuOnClick);

