$(function() {
    $('.login__btn').click(function () {
        $('.login__form-signin').toggleClass('login__form-signin_left');
        $('.login__form-signup').toggleClass('login__form-signup_left');
        $('.login__frame').toggleClass('login__frame_long');
        
        if(document.querySelector('.login__signin_active')) {
            $(".login__signin_active").toggleClass("login__signin_active").toggleClass('login__signin_inactive');
            $(".login__signup_inactive").toggleClass("login__signup_inactive").toggleClass("login__signup_active");
        } else {
            $(".login__signin_inactive").toggleClass("login__signin_inactive").toggleClass("login__signin_active");
            $(".login__signup_active").toggleClass("login__signup_active").toggleClass('login__signup_inactive');
        }
    })
});