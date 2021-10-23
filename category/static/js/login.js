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
    });
});

window.addEventListener('DOMContentLoaded', () => {
    new window.JustValidate('.login__form-signin', {
        rules: {
            email: {
                required: true,
                email: true,
                remote: {
                    url: CHECK_EMAIL_URL,
                    successAnswer: 'OK',
                    sendParam: 'email',
                    method: 'GET'
                }
            },
            password: {
                required: true
            }
        },
        messages: {
            email: {
                required: 'Это поле обязательно',
                email: 'Введите правильный email адрес'
            },
            password: {
                required: 'Это поле обязательно'
            }
        }
    });

    new window.JustValidate('.login__form-signup', {
        rules: {
            first_name: {
                required: true,

            },
            last_name: {
                required: true
            },
            email: {
                required: true,
                email: true,
                remote: {
                    url: CHECK_EMAIL_URL,
                    successAnswer: 'OK',
                    sendParam: 'email',
                    method: 'GET'
                }
            },
            password: {
                required: true,
                password: true
            },
            password_repeat: {
                required: true,
                function: (name, value) => {
                    let passwordInput = document.forms[2].elements[3]; // name="password"
                    console.log(passwordInput, value);
                    return passwordInput.value === value;
                }
            }
        },
        messages: {
            first_name: {
                required: 'Это поле обязательно'
            },
            last_name: {
                required: 'Это поле обязательно'
            },
            email: {
                required: 'Это поле обязательно',
                email: 'Введите правильный email адрес'
            },
            password: {
                required: 'Это поле обязательно',
                password: 'Пароль должен содержать заглавную букву и цифру'
            },
            password_repeat: {
                required: 'Это поле обязательно',
                function: 'Пароли должны совпадать'
            }
        }
    })
})