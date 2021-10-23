const CHECK_EMAIL_URL = 'http://localhost:8000/check-email/';

window.addEventListener('DOMContentLoaded', () => {
    // Work with shopping cart
    let shopcart = document.querySelector('.nav__shopcart');
    if (parseInt(shopcart.attributes["data-count"].value) === 0 && !shopcart.classList.contains('.hidden_after')) {
      shopcart.classList.toggle('hidden_after');
    }

  // Work with search
  $(".search__advice").hide();
  $("#search").keyup((event) => {
    switch(event.keyCode) {
      case 13:
      case 27:
      case 38:
      case 40:
      break;

      default:
        $.ajax({
          url: 'http://localhost:8000/search-advice/',
          type: 'GET',
          dataType: 'json',
          data: $("#search").serialize()
        })
        .done(function(response) {
          let products = response.products;
          if (products) {
            $(".search__advice").empty();
            $(".search__advice").show();
            for (let i in products) {
              $(".search__advice").append(`<div class='advice__item' id=${i}>`+products[i].name+"</div>");
            }
          } else {
            $(".search__advice").empty();
            $(".search__advice").show();
            $(".search__advice").append(`<div class='advice__not'>Результаты не найдены</div>`);
          }
        })
        .fail(function() {
          console.log("error");
        })
        .always(function() {
          console.log("complete");
        });
    }
  })

  $(document).on('click', '.advice__item', e => {
    console.log('тут');
    $('#search').val($('.advice__item').text());
  })

  $(document).on('click', e => {
    if (e.target.className != '.search__advice' && e.target.className != 'search__input') {
      $('.search__advice').fadeOut(100);
    }
  })

  $(document).on('click', '#search', e => {
    if ($('.search__advice').children('.advice__item')) {
      $('.search__advice').show();
    }
  })
});
