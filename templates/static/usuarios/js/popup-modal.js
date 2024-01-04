var modal = document.querySelector('.modal-pop');

document.addEventListener('DOMContentLoaded', function() {
    let formulario = document.getElementById('form-cadastro');

    formulario.addEventListener('submit', function(event) {
        event.preventDefault();

        

    
        modal.style.display = 'block';

        // Aqui você pode adicionar a lógica para enviar os dados do formulário para o servidor
        // Por exemplo, usando AJAX para enviar os dados

        // Supondo que você use AJAX para enviar os dados do formulário
        // Substitua o código abaixo pela sua lógica de envio de dados

        // fetch('/sua-rota-de-envio', {
        //     method: 'POST',
        //     body: new FormData(formulario)
        // })
        // .then(response => {
        //     // Tratar a resposta do servidor aqui
        // })
        // .catch(error => {
        //     // Tratar erros aqui
        // });
    });
});


var btn_ok = document.getElementById('ok-pop')

btn_ok.addEventListener('click',function(){
    modal.style.display = 'none'
})

/*
document.addEventListener('DOMContentLoaded', function() {
    let formulario = document.getElementById('form-cadastro');

    formulario.addEventListener('submit', function(event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Aqui você pode obter os dados do formulário para enviar ao servidor
        let formData = new FormData(formulario);

        // Exemplo de envio usando fetch API
        fetch('URL_DO_SEU_ENDPOINT', {
            method: 'POST', // Ou 'GET', 'PUT', 'DELETE', etc., dependendo da sua necessidade
            body: formData // Aqui você envia os dados do formulário
        })
        .then(response => {
            if (response.ok) {
                // Se a resposta do servidor estiver ok, exiba o modal
                exibirModal();
            } else {
                // Se houver algum problema com o envio do formulário, trate-o aqui
                console.error('Ocorreu um erro no envio do formulário');
            }
        })
        .catch(error => {
            // Trate os erros de rede ou outros erros de fetch aqui
            console.error('Erro:', error);
        });
    });

    function exibirModal() {
        // Aqui você coloca a lógica para exibir o modal
        let modal = document.querySelector('.modal-pop');
        modal.style.display = 'block';
    }
});
*/
