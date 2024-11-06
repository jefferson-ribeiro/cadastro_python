// scripts.js

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Impede o envio imediato para mostrar a mensagem de confirmação

    // Coletar dados do formulário
    const nomeCompleto = document.querySelector("#nomeCompleto").value;
    const telefone = document.querySelector("#telefone").value;
    const cpf = document.querySelector("#cpf").value;
    const email = document.querySelector("#email").value;

    // Exibir uma mensagem de confirmação
    alert(
      `Nome Completo: ${nomeCompleto}\nTelefone: ${telefone}\nCPF: ${cpf}\nEmail: ${email}`
    );

    // Permitir o envio do formulário após um pequeno atraso
    setTimeout(function () {
      form.submit();
    }, 500); // Aguardar 500 ms antes de submeter o formulário
  });
});
document.querySelectorAll("a.nav-link").forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document
      .querySelector(this.getAttribute("href"))
      .scrollIntoView({ behavior: "smooth" });
  });
});
