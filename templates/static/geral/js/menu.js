$('.menu').click(function () {
    if ($('.itens-menu').hasClass('fechado')) {
      abrirMenu();
    } else {
      fecharMenu();
    }
  });

// menu.addEventListener('click', trocarIcone)

function abrirMenu(){
    $('.itens-menu').addClass('aberto').animate({ right: '0' });
    $('.itens-menu').removeClass('fechado')
        // Anima a propriedade right para trazer o menu da direita para a esquerda
        
}

function fecharMenu() {
    // Anima a propriedade right para mover o menu de volta para fora da tela
    $('.itens-menu').removeClass('aberto').animate({ right: '-446px' })
    $('.itens-menu').addClass('fechado')
}





// function trocarIcone(){
//     let icone = document.querySelector('.menu-d')

//     if(icone.classList.contains('fa-bars')){
//         icone.classList.remove('fa-bars')
//         icone.classList.add('fa-xmark')
//     }else{
//         icone.classList.remove('fa-xmark')
//         icone.classList.add('fa-bars')
//     }

// }