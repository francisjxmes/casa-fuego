$(document).ready(function () {
  $('.tab-link').click(function (e) {
    e.preventDefault();

    const target = $(this).data('tab');

    // Hide all sections
    $('.menu-section').hide();

    // Remove active class from all tabs
    $('.tab-link').removeClass('active');

    // Show the selected tab and mark it active
    $('#' + target).fadeIn(200);
    $(this).addClass('active');
  });

  // Side panel 
  $('.menu-toggle').click(function() {
    $('.side-panel').css('right', '0');
    $('.overlay').fadeIn();
  });

  $('.close-btn, .overlay').click(function() {
    $('.side-panel').css('right', '-250px');
    $('.overlay').fadeOut();
  });

  // Search filtering
  $('#menu-search').on('keyup', function() {
    let searchText = $(this).val().toLowerCase();

    $('.item-container').each(function(){
      let itemText = $(this).text().toLowerCase();

      if (itemText.includes(searchText)) {
        $(this).show();
      } else {
        $(this).hide();
      }
    });
  });

  // Form validation
  $('.booking-form').on('submit', function (e) {
    let valid = true;

    $('#name, #party-size, #date, #time').each(function () {
      if ($(this).val().trim() === "") {
        valid = false;
        $(this).css('border', "2px solid red");
      } else {
        $(this).css('border', "");
      }
    });

    if (!valid) {
      e.preventDefault();
      alert("Please fill in all fields.");
    }
  });

});