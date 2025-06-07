#  Gerador de Violão com Ritmo Swingado em Python

Este projeto gera um arquivo `.mid` com acompanhamento de violão baseado em uma progressão de acordes definida pelo usuário, usando um ritmo swingado comum em músicas pop.

O arquivo MIDI pode ser importado diretamente em qualquer DAW (FL Studio, Studio One, Reaper, etc.) com o plugin **Ample Guitar M Lite 3.7.0**, para simular acordes realistas de violão.

---

##  Requisitos

- Python 3.8 ou superior
- Biblioteca [mido](https://pypi.org/project/mido/)
- Plugin VST: [Ample Guitar M Lite 3.7.0](https://www.amplesound.net/en/download.asp) (gratuito)

---

##  Instalação

Abra seu terminal e instale o pacote necessário com:

```bash
pip install mido python-rtmidi

## Como o código funciona
O script:

Define uma progressão de 4 acordes: C, G, Am, F

Aplica um ritmo swingado dentro de cada compasso (com duração alternada das palhetadas)

Repete a sequência de acordes conforme especificado

Salva o resultado em violao.mid

## Parâmetros personalizáveis
bpm: velocidade da música (batidas por minuto)

acordes: lista de acordes, definidos por notas (ex: ['C3', 'E3', 'G3'])

reps: número de repetições da progressão

ritmo: sequência de posições de palhetadas dentro do compasso (em ticks)

## Exemplo de uso no Ample Guitar
Abra seu DAW

Crie uma track MIDI com o Ample Guitar M Lite

Importe violao.mid nessa track

Dê o play para ouvir os acordes tocados com dinâmica de violão realista

