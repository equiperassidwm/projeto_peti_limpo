$(document).ready(function() {
    var slideGroupsToShow = 1;
    var slideGroupWidth = $('.slide-group').outerWidth();
    var slideIndex = 0;
  
    function showSlides() {
      $('.slide-group').hide();
      $('.slide-group').slice(slideIndex, slideIndex + slideGroupsToShow).show();
    }
  
    function slideNext() {
      slideIndex = (slideIndex + slideGroupsToShow < $('.slide-group').length) ? slideIndex + slideGroupsToShow : 0;
      showSlides();
    }
  
    function slidePrev() {
      slideIndex = (slideIndex - slideGroupsToShow >= 0) ? slideIndex - slideGroupsToShow : $('.slide-group').length - slideGroupsToShow;
      showSlides();
    }
  
    var slideInterval = setInterval(slideNext, 3000); // Altera a cada 3 segundos
  
    $('.next').click(function() {
      clearInterval(slideInterval);
      slideNext();
      slideInterval = setInterval(slideNext, 3000);
    });
  
    $('.prev').click(function() {
      clearInterval(slideInterval);
      slidePrev();
      slideInterval = setInterval(slideNext, 3000);
    });
  
    showSlides(); // Mostra os slides inicialmente

    
  });
  
  