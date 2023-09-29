function mudaTexto() {
if (document.getElementById("demo").innerHTML === "Texto padrão.") {
    document.getElementById("demo").innerHTML = "Alteração de texto.";
  } else {
    document.getElementById("demo").innerHTML = "Texto padrão.";
  }
}
function realizarOperacao(operacao) {
  const n1 = parseFloat(document.getElementById("numero1").value);
  const n2 = parseFloat(document.getElementById("numero2").value);
  let resultado = 0;

  if (operacao === 'adicao') {
      resultado = n1 + n2;
  } else if (operacao === 'subtracao') {
      resultado = n1 - n2;
  } else if (operacao === 'multiplicacao') {
      resultado = n1 * n2;
  } else if (operacao === 'divisao') {
      resultado = n1 / n2;
  }

  document.getElementById("resultado").innerHTML = "O resultado é: " + resultado;
}
