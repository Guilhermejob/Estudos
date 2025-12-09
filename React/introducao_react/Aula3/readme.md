# CSS MODULE

## Como Criar
para criar um module de css é simples basta no seu componente ou pagina quando for criar o arquivo css
ao inves de salvar como .css, iremos salvar como style.module.css (adicionamos um .module.css para informar que aquele arquivo é um css module)

## Como Usar
para usar no arquivo .jsx onde iremos importar ele, importaremos da seguinte forma `import styles from ./style.module.css` e quando formos aplicar a classe do css usaremos como se fosse um objeto className = {styles.card}

## Por que usar?
Por que no react por mais que importemos o css padrao apenas no componente, esse estilo vazará globalmente pela aplicação, podendo causar efeitos colaterais não desejados, usando css modules garantimos que aquela estilização fique apenas com aquele componente, e não vaze para o resto da aplicação