/*
	Directive by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			wide:      [ '1281px',  '1680px' ],
			normal:    [ '981px',   '1280px' ],
			narrow:    [ '841px',   '980px'  ],
			narrower:  [ '737px',   '840px'  ],
			mobile:    [ '481px',   '736px'  ],
			mobilep:   [ null,      '480px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

})(jQuery);

// Type write efect
var TxtType = function(el, toRotate, period) {
	this.toRotate = toRotate;
	this.el = el;
	this.loopNum = 0;
	this.period = parseInt(period, 10) || 2000;
	this.txt = '';
	this.tick();
	this.isDeleting = false;
};

TxtType.prototype.tick = function() {
	var i = this.loopNum % this.toRotate.length;
	var fullTxt = this.toRotate[i];

	if (this.isDeleting) {
	this.txt = fullTxt.substring(0, this.txt.length - 1);
	} else {
	this.txt = fullTxt.substring(0, this.txt.length + 1);
	}

	this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

	var that = this;
	var delta = 200 - Math.random() * 100;

	if (this.isDeleting) { delta /= 2; }

	if (!this.isDeleting && this.txt === fullTxt) {
	delta = this.period;
	this.isDeleting = true;
	} else if (this.isDeleting && this.txt === '') {
	this.isDeleting = false;
	this.loopNum++;
	delta = 500;
	}

	setTimeout(function() {
	that.tick();
	}, delta);
};

window.onload = function() {
	var elements = document.getElementsByClassName('typewrite');
	for (var i=0; i<elements.length; i++) {
		var toRotate = elements[i].getAttribute('data-type');
		var period = elements[i].getAttribute('data-period');
		if (toRotate) {
		  new TxtType(elements[i], JSON.parse(toRotate), period);
		}
	}
	// INJECT CSS
	var css = document.createElement("style");
	css.type = "text/css";
	css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
	document.body.appendChild(css);
};
