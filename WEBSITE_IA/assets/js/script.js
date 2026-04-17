//Aguarda o carregamento da página HTML antes de excutar o código javascript
document.addEventListener("DOMContentLoaded", function(){
    //console.log("Debug");
    const form = document.getElementById("form-contato");
    const alerta = document.getElementById("mensagem-alerta");
 
    if (!form) return;
 
    // "Escuta" o envio do formlário
 
    form.addEventListener("submit", function (event) {
 
        event.preventDefault();
 
    // Captura de dados digitados pelo usuário
    
    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const assunto = document.getElementById("assunto").value.trim();
    const mensagem = document.getElementById("mensagem").value.trim();
 
    // Validações (Regras do negócio)
 
    // Validação do nome
     if (nome.length < 3) {
        exibirAlerta("Por favor, insira um nome válido!", "alerta-erro");
        return; // Interrompe o envio
    }
    
    // Validação do email
    if (!email.includes("@") || !email.includes(".")) {
        exibirAlerta("Digite um e-mail válido.", "alerta-erro");
        return;
    }
    
    // Validação do assunto
    if (!assunto) {
        exibirAlerta("Selecione um assunto.", "alerta-erro");
        return;
    }
 
    // Validação da mensagem 
    if (mensagem.length < 10) {
        exibirAlerta("A mensagem deve ter pelo menos 10 caracteres!", "alerta-erro");
        return;
    }
 
    console.log("Dados enviados:",{
        nome,
        email,
        assunto,
        mensagem
    });
 
    // Mostra mensagem de sucesso
    exibirAlerta("Mensagem enviada com sucesso", "alerta-sucesso");
 
    //Limpar formulário
    form.reset();
 
    // Esconde o alerta depois de 5 segundos
    setTimeout(() => {
        alerta.style.display = "none"
        alerta.className = "mensagem-alerta"    
    }, 5000);

});
 
// Função reutilizável para exibir mensagens
    function exibirAlerta(texto, classe) {

        // Define o texto da mensagem
        alerta.textContent = texto;

        // Tornar a mensagem vísivel
        alerta.style.display = "block";

        // Aplica classe de estilo (erro ou sucesso)
        alerta.className = `mensagem-alerta ${classe}`;
    };
 
});