(function ($) {
	"use strict";

	/*------------------------------------
			Preloader
		--------------------------------------*/

	$(window).on('load', function () {
		// $('#preloader').delay(350).fadeOut('slow');
		// $('body').delay(350).css({ 'overflow': 'visible' });
		// -------------------- Site Preloader
		$('#ctn-preloader').fadeOut(); // will first fade out the loading animation
		$('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
		$('body').delay(350).css({ 'overflow': 'visible' });
	});




	/*------------------------------------
		Mobile Menu
	--------------------------------------*/

	$('#mobile-menu').meanmenu({
		meanMenuContainer: '.mobile-menu',
		meanScreenWidth: "991",
		meanExpand: '+',
		meanShowChildren: true,
		meanExpandableChildren: true,
		meanContract: "-",
		meanDisplay: "block"
	});

	$('#mobile-menu-active').metisMenu();

	$('#mobile-menu-active .has-dropdown > a').on('click', function (e) {
		e.preventDefault();
	});

	$(".hamburger-menu > a").on("click", function (e) {
		e.preventDefault();
		$(".slide-bar").toggleClass("show");
		$("body").addClass("on-side");
		$('.body-overlay').addClass('active');
		$(this).addClass('active');
	});

	$(".close-mobile-menu > a").on("click", function (e) {
		e.preventDefault();
		$(".slide-bar").removeClass("show");
		$("body").removeClass("on-side");
		$('.body-overlay').removeClass('active');
		$('.hamburger-menu > a').removeClass('active');
	});

	$('.body-overlay').on('click', function () {
		$(this).removeClass('active');
		$(".slide-bar").removeClass("show");
		$("body").removeClass("on-side");
		$('.hamburger-menu > a').removeClass('active');
	});



	//sticky-menu
	$(window).on('scroll', function () {
		var scroll = $(window).scrollTop();
		if (scroll < 200) {
			$(".main-header-area").removeClass("sticky-menu");
		} else {
			$(".main-header-area").addClass("sticky-menu");
		}
	});

	// Add .active class to current navigation based on URL
	var pgurl = window.location.href.substr(window.location.href.lastIndexOf("/") + 1);
	$(".navbar-nav > li  a").each(function () {
		if ($(this).attr("href") == pgurl || $(this).attr("href") == '')
			$(this).addClass("active");
		// $(this).parent("li").addClass("active");
	})


	//shopping-cart-bar
	$(".shopping-cart").on("click", function () {
		$(".cart-menu-right").addClass('cart-info');
	});
	$(".close-icon").click(function () {
		$(".cart-menu-right").removeClass('cart-info');

	});





	//brand-slider-one
	$('.brand-slider-one, .brand__slider__one').slick({
		dots: false,
		arrows: false,
		// nextArrow: $('.next_t1'),
		// prevArrow: $('.prev_t1'),
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 6,
		slidesToScroll: 1,

		responsive: [

			{
				breakpoint: 1200,
				settings: {
					slidesToShow: 5,
				}
			},

			{
				breakpoint: 980,
				settings: {
					slidesToShow: 4,
				}
			},
			{
				breakpoint: 767,
				settings: {
					slidesToShow: 3,
				}
			},
			{
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});


	//testimonial__slider
	$('.testimonial__slider').slick({
		dots: true,
		arrows: true,
		nextArrow: $('.next_t1'),
		prevArrow: $('.prev_t1'),
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 3,
		slidesToScroll: 1,

		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 1,
				}
			},
			{
				breakpoint: 991,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});


	//blog__slider__one
	$('.blog__slider__one').slick({
		dots: true,
		arrows: false,
		nextArrow: $('.next_f1'),
		prevArrow: $('.prev_f1'),
		margin: '15px',
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 2,
		slidesToScroll: 1,

		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				}
			},
			{
				breakpoint: 991,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});


	//testimonial__slider__two
	$('.testimonial__slider__two').slick({
		dots: true,
		arrows: false,
		nextArrow: $('.next_t1'),
		prevArrow: $('.prev_t1'),
		margin: '15px',
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 2,
		slidesToScroll: 1,

		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				}
			},

			{
				breakpoint: 770,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});


	//testimonial__slider__three
	$('.testimonial__slider__three').slick({
		dots: true,
		arrows: false,
		margin: '15',
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 3,
		slidesToScroll: 1,

		responsive: [
			{
				breakpoint: 1200,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 1,
				}
			},
			{
				breakpoint: 1100,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				}
			},

			{
				breakpoint: 770,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});

	//testimonial__slider__four
	$('.testimonial__slider__four').slick({
		dots: false,
		nextArrow: $('.next_t1'),
		prevArrow: $('.prev_t1'),
		margin: '15px',
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 2,
		slidesToScroll: 1,

		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				}
			},

			{
				breakpoint: 770,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});


	//hosting__marque__slider 
	$('.hosting__marque__slider ').slick({
		dots: false,
		arrows: false,
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 5,
		slidesToScroll: 1,

		responsive: [
			{
				breakpoint: 1600,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 1,
				}
			},
			{
				breakpoint: 1201,
				settings: {
					slidesToShow: 3,
					slidesToScroll: 1,
				}
			},

			{
				breakpoint: 770,
				settings: {
					slidesToShow: 2,
				}
			},

			{
				breakpoint: 575,
				settings: {
					slidesToShow: 1,
				}
			}
		]
	});


	//blog__classic__gallery 
	$('.blog__classic__gallery ').slick({
		dots: false,
		arrows: true,
		nextArrow: $('.next_t1'),
		prevArrow: $('.prev_t1'),
		infinite: true,
		loop: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 1,
		slidesToScroll: 1,
	});


	//testimonial__slider__content
	$('.testimonial__slider__content').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: true,
		nextArrow: $('.next_t1'),
		prevArrow: $('.prev_t1'),
		fade: true,
		infinite: true,
		asNavFor: '.testimonial__thumbs__slider'
	});
	$('.testimonial__thumbs__slider').slick({
		slidesToShow: 5,
		slidesToScroll: 1,
		asNavFor: '.testimonial__slider__content',
		autoplay: true,
		autoplaySpeed: 3000,
		dots: false,
		arrows: false,
		centerMode: true,
		focusOnSelect: true,
		centerPadding: 0,
		infinite: true,
		responsive: [
			{
				breakpoint: 1201,
				settings: {
					slidesToShow: 5,
					slidesToScroll: 1,
				}
			},

			{
				breakpoint: 980,
				settings: {
					slidesToShow: 3,
				}
			},

			{
				breakpoint: 767,
				settings: {
					slidesToShow: 3,
					centerMode: false
					// centerPadding: '100px'
				}
			}
		]
	});

	//product__item__slider
	$('.product__item__slider').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		fade: true,
		asNavFor: '.product__thumb__slider'
	});
	$('.product__thumb__slider').slick({
		slidesToShow: 4,
		slidesToScroll: 1,
		asNavFor: '.product__item__slider',
		autoplay: true,
		autoplaySpeed: 3000,
		dots: false,
		arrows: false,
		centerMode: false,
		focusOnSelect: true,
		responsive: [
			{
				breakpoint: 1201,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 1,
				}
			},

			{
				breakpoint: 980,
				settings: {
					slidesToShow: 3,
				}
			},

			{
				breakpoint: 767,
				settings: {
					slidesToShow: 3,
				}
			}
		]
	});



	// -------------------- price btn
	$(".price-btn").click(function () {

		var lable = $(".price-btn").text().trim();

		if (lable == "Monthly") {
			$(".price-btn").text("Yearly");
			$(".yearly-price").show();
			$(".monthly-price").hide();
		}
		else {
			$(".price-btn").text("Monthly");
			$(".monthly-price").show();
			$(".yearly-price").hide();
		}

	});

	$(function () {
		$('.chart').easyPieChart({
			animate: {
				duration: 1000,
				enabled: true
			},
			scaleLength: 0,
			size: 140,
			trackColor: 'rgba(255, 255, 255, 0.2)',
			barColor: '#FD008B',
			scaleColor: 'false',
			lineWidth: 7,
			trackWidth: 2,
			lineCap: 'round',
			rotate: 90,
		});
	});

	// ---------------- Data CSS Js
	$("[data-background").each(function () {
		$(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
	});

	$("[data-width]").each(function () {
		$(this).css("width", $(this).attr("data-width"));
	});

	$("[data-bg-color]").each(function () {
		$(this).css("background-color", $(this).attr("data-bg-color"));
	});


	// -------------------- Remove Placeholder When Focus Or Click
	$("input,textarea").each(function () {
		$(this).data('holder', $(this).attr('placeholder'));
		$(this).on('focusin', function () {
			$(this).attr('placeholder', '');
		});
		$(this).on('focusout', function () {
			$(this).attr('placeholder', $(this).data('holder'));
		});
	});


	/* magnificPopup video view */
	$('.popup-video').magnificPopup({
		type: 'iframe'
	});


	// isotop
	$('.grid').imagesLoaded(function () {
		// init Isotope
		var $grid = $('.grid').isotope({
			itemSelector: '.grid-item',
			percentPosition: true,
			masonry: {
				// use outer width of grid-sizer for columnWidth
				columnWidth: 0,
				gutter: 0
			}
		});
		// filter items on button click
		$('.portfolio-menu').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$grid.isotope({ filter: filterValue });
		});
	});

	//for menu active class
	$('.portfolio-menu button').on('click', function (event) {
		$(this).siblings('.active').removeClass('active');
		$(this).addClass('active');
		event.preventDefault();
	});

	var scrollToTopBtn = $('#scrollToTopBtn');

	$(window).scroll(function () {
		if ($(window).scrollTop() > 300) {
			scrollToTopBtn.addClass('show');
		} else {
			scrollToTopBtn.removeClass('show');
		}
	});

	scrollToTopBtn.on('click', function (e) {
		e.preventDefault();
		$('html, body').animate({ scrollTop: 0 }, '300');
	});



	/* Cart Plus Minus Js */
	$(".cart-plus-minus").append('<div class="dec qtybutton">-</div><div class="inc qtybutton">+</div>');
	$(".qtybutton").on("click", function () {
		var $button = $(this);
		var oldValue = $button.parent().find("input").val();
		if ($button.text() == "+") {
			var newVal = parseFloat(oldValue) + 1;
		} else {
			// Don't allow decrementing below zero
			if (oldValue > 0) {
				var newVal = parseFloat(oldValue) - 1;
			} else {
				newVal = 0;
			}
		}
		$button.parent().find("input").val(newVal);
	});

	//jquiry-price-slider
	$(function () {
		$("#slider-range").slider({
			range: true,
			min: 0,
			max: 500,
			values: [75, 300],
			slide: function (event, ui) {
				$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
			}
		});
		$("#amount").val("$" + $("#slider-range").slider("values", 0) +
			" - $" + $("#slider-range").slider("values", 1));
	});





	// wow animation - start
	// --------------------------------------------------
	function wowAnimation() {
		new WOW({
			offset: 100,
			mobile: true
		}).init()
	}
	wowAnimation();



	//jquiry-price-slider
	$(function () {
		$("#slider-range").slider({
			range: true,
			min: 0,
			max: 500,
			values: [75, 300],
			slide: function (event, ui) {
				$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
			}
		});
		$("#amount").val("$" + $("#slider-range").slider("values", 0) +
			" - $" + $("#slider-range").slider("values", 1));
	});

	//js-tilt

	$('.js-tilt').tilt({
		glare: true,
		maxGlare: .1,
	})


	//nice-select
	// $(document).ready(function () {
	// 	$('select').niceSelect();
	// });

	$('select').niceSelect();

	AOS.init();

	//counter
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});

	const lenis = new Lenis()

	lenis.on('scroll', () => {

	})

	function raf(time) {
		lenis.raf(time)
		requestAnimationFrame(raf)
	}

	requestAnimationFrame(raf)


})(jQuery);