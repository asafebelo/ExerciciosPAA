<h1 align="center">Exercícios Projeto e Análise de Algoritmos</h1>
<h2 align="center">Projeto e Análise de Algoritmos</h2>

## 🧑‍💻 Autor
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/97066868?v=4" width=115><br><sub>Asafe Belo Borges</sub>](https://github.com/asafebelo) |
| :---: |

## 📝 Exercícios 
### Exercício I
`Implemente um algoritmo de divisão e conquista para calcular o máximo de um array de números inteiros. O algoritmo deve dividir o array em duas metades, encontrar o máximo de cada metade recursivamente e, em seguida, comparar os dois valores para determinar o máximo global. Discuta a complexidade do seu algoritmo em termos de notação Big O e compare-a com a abordagem iterativa que percorre o array uma única vez.`

Complexidade: O algoritmo de **divisão e conquista** divide o array em duas metades usando recursão, resultando em uma árvore de altura com complexidade O(log(n)). Em cada nível da árvore, o algoritmo percorre os elementos uma vez para comparar os máximos das duas metades, o que leva a uma complexidade de O(n). Logo, a complexidade total é **O(n)**. Na **abordagem iterativa**, o algoritmo percorre o array uma vez, comparando cada elemento até achar o maior. Com isso, também temos um algoritmo de complexidade **O(n)**.

### Exercício II
`Escreva um algoritmo que utiliza divisão e conquista para calcular a soma de todos os elementos de um array. O algoritmo deve dividir o array em partes menores, somar recursivamente os elementos de cada parte e combinar os resultados. Após implementar o algoritmo, discuta a eficiência da abordagem de divisão e conquista em comparação com a soma iterativa.`

Complexidade: O algoritmo de **divisão e conquista** divide o array em duas metades usando recursão, resultando em uma árvore de altura com complexidade O(log(n)), devido a quantidade da pilha de recursão. m cada nível da árvore, o algoritmo percorre os elementos uma vez para comparar os máximos das duas metades, o que leva a uma complexidade de O(n). Por sua vez, o algoritmo iterativo percorre o array somente uma vez, somando cada elemento até o final, o que deixa-o com uma complexidade de O(n). Por fim, entendemos que o algoritmo iterativo é geralmente mais eficiente e simples. Ela realiza o cálculo com menos operações, evitando o overhead das chamadas recursivas e usando menos memória. O Algoritmo de divisão e conquista por sua vez é melhor em casos aonde os problemas precisam ser divididos em subproblemas mais complexos.
 
### Exercício III
`Escreva um algoritmo que utiliza divisão e conquista para calcular a potência de um número (por exemplo, x^n) de forma eficiente. O algoritmo deve aproveitar a propriedade da exponenciação, onde x^n pode ser reduzido para x^(n/2) × x^(n/2) para potências pares e x * x^(n−1) para potências ímpares.`

### Exercício IV
`Implemente um algoritmo de backtracking que gere todas as combinações possíveis de um conjunto de caracteres. O algoritmo deve explorar cada possibilidade, começando com o conjunto vazio e adicionando caracteres um por um, garantindo que todas as combinações sejam consideradas. Por exemplo, para o conjunto {A, B, C}, a saída deve incluir combinações individuais (A, B, C), combinações de dois elementos (AB, AC, BC) e a combinação completa (ABC).`

### Exercício V
`Escreva um algoritmo de backtracking para resolver o problema da soma de subconjuntos. Dado um conjunto de números e um valor alvo, o algoritmo deve explorar todas as combinações possíveis de elementos do conjunto para determinar se existe um subconjunto cuja soma é igual ao valor alvo.`

