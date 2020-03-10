$('.header__nav__item__link--icon').on('click', function(){
    $('.login-container').css('display', 'block')
    $('.login-container').addClass('open')
})
$('.close').on('click', function(){
    $('.login-container').css('display', 'none')
    $('.login-container').removeClass('open')
})
/* on click sign up */
$('.login-nav li:nth-child(2) > a').on('click', function(){
    $('.login-nav > li:nth-child(1)').removeClass('active')
    $('.login-nav > li:nth-child(2)').addClass('active')
    $('.reg').css('display', 'block')
    $('.login__submit').text('Sign Up')
    $('.login__submit').css('margin-top', '2rem');
})
$('.login-nav li:nth-child(1) > a').on('click', function(){
    $('.login-nav > li:nth-child(2)').removeClass('active')
    $('.login-nav > li:nth-child(1)').addClass('active')
    $('.reg').css('display', 'none')
    $('.login__submit').text('Sign In')
    $('.login__submit').css('margin-top', '4rem');
})