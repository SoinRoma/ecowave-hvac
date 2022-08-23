'use strict';

const menu_fixed = document.querySelector('.main_menu_area');
const topOfNav = menu_fixed.offsetTop;

function fixed_nav() {
    if (window.scrollY >= topOfNav || window.scrollY === topOfNav) {
        document.body.classList.add('fixed-scroll-nav');
    } else {
        document.body.classList.remove('fixed-scroll-nav');
    }
}

window.addEventListener('scroll', fixed_nav);


$(document).on('ready', function () {

    $(document).on('click', '.main_menu_area button.navbar-toggles', function () {
        $('.main_menu_area .collapse_responsive').toggleClass('collapse_active');
        $('.main_menu_area button.navbar-toggles').toggleClass('navbar_close');
    });

    $(document).on('click', '.main_menu_area .navbar-nav li > span.responsive_menu:not(:only-child)', function (e) {
        $(this).siblings('.dropdown-menu').toggle();
        $('.dropdown-menu').not($(this).siblings()).hide();
        e.stopPropagation();
    });


    $('.counter').counterUp({
        delay: 10,
        time: 3000
    });


    $('.header_slider_area').owlCarousel({
        items: 1,
        autoHeight: true,
        autoplay: false,
        loop: true,
        nav: false,
        dots: true,
        slideSpeed: 300,
        animateIn: 'slideInLeft',
        animateOut: 'fadeOutRight',
        autoplayTimeout: 7000,
    });


    $('.clients_logo').owlCarousel({
        autoplay: true,
        loop: true,
        nav: false,
        autoplayTimeout: 9000,
        dots: true,
        responsive: {
            0: {
                items: 1,
            },
            600: {
                items: 2,
            },
            1000: {
                items: 3,
            }
        }
    });

});

