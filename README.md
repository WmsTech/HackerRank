# Desafios do HackerRank em Python

Minhas soluções de 13 desafios do [HackerRank](https://www.hackerrank.com/). Os arquivos reúnem exercícios de strings, matrizes, contagem, ordenação e operações com bits. Em alguns deles deixei alternativas de resolução comentadas.

## Soluções

| Desafio | Arquivo | Ideia trabalhada |
| --- | --- | --- |
| Time Conversion | [`conversion.py`](conversion.py) | Conversão entre horários de 12 e 24 horas |
| Counting Sort 1 | [`counting_sort.py`](counting_sort.py) | Vetor de frequências |
| Diagonal Difference | [`diagonal_difference.py`](diagonal_difference.py) | Percurso das diagonais de uma matriz |
| Flipping Bits | [`flipping_bits.py`](flipping_bits.py) | Inversão de uma representação de 32 bits |
| Lonely Integer | [`lonely_interger.py`](lonely_interger.py) | Busca do elemento sem repetição |
| Sparse Arrays | [`matching_strings.py`](matching_strings.py) | Contagem de ocorrências em consultas |
| Mini-Max Sum | [`max_min.py`](max_min.py) | Ordenação e somas parciais |
| Pangrams | [`pangrams.py`](pangrams.py) | Verificação das letras do alfabeto |
| Permuting Two Arrays | [`permuting_two_arrays.py`](permuting_two_arrays.py) | Reorganização de pares para atingir um limite |
| Plus Minus | [`plus_minus.py`](plus_minus.py) | Proporções de positivos, negativos e zeros |
| Sales by Match | [`sales_by_match.py`](sales_by_match.py) | Contagem de pares |
| Subarray Division | [`subarray_division_1.py`](subarray_division_1.py) | Segmentos contíguos de tamanho fixo |
| XOR Strings | [`xor.py`](xor.py) | Correção de código e XOR entre strings binárias |

## Experimentar uma função

As soluções usam a biblioteca padrão do Python 3. Depois de clonar e entrar na pasta:

```powershell
git clone https://github.com/WmsTech/HackerRank.git
cd HackerRank
python -c "from conversion import timeConversion; print(timeConversion('07:05:45PM'))"
```

Resultado: `19:05:45`.

Para uma matriz:

```python
from diagonal_difference import diagonalDifference

matriz = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(matriz))  # 15
```

## Entrada e saída da plataforma

Vários scripts mantêm o código de leitura fornecido pelo HackerRank e escrevem no arquivo indicado pela variável de ambiente `OUTPUT_PATH`. Para executá-los inteiros no PowerShell, defina essa variável antes:

```powershell
$env:OUTPUT_PATH = Join-Path $env:TEMP 'hackerrank-resultado.txt'
python conversion.py
Get-Content -LiteralPath $env:OUTPUT_PATH
```

Informe `07:05:45PM` quando o programa pedir a entrada. `plus_minus.py`, `max_min.py` e `xor.py` imprimem diretamente no terminal. O último também lê a entrada ao ser importado; para ele, prefira a execução como script.

## Continuidade

O próximo passo é registrar testes com casos de borda e discutir o custo das soluções. Algumas implementações fazem contagens repetidas ou percursos aninhados; comparar essas versões com dicionários de frequência e operações bit a bit ajuda a mostrar a evolução do raciocínio.

Resoluções de Washington Marinho dos Santos. Os desafios e trechos de leitura de entrada vêm do HackerRank. [Licença MIT do repositório](LICENSE).
