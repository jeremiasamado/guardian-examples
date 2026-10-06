<div align="center">

**PT-PT** | [EN](./README.md)

<img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=36&duration=3200&pause=1200&color=8A00C4&background=00000000&center=true&vCenter=true&width=850&height=80&lines=GUARDIAN+RESEARCH+TOOLING;MAPEAR+A+SUPERF%C3%8DCIE;TRIAR+O+ARTEFACTO;SEGUIR+A+EVID%C3%8ANCIA;RECON+%2F+RESEARCH+%2F+REPORT" alt="Guardian research tooling">

<br>

<img src="https://readme-typing-svg.demolab.com?font=VT323&size=24&duration=2600&pause=1000&color=E4BCFF&background=00000000&center=true&vCenter=true&width=850&height=40&lines=%3E+enumerar+%2F+fingerprint+%2F+triage;%3E+ficheiros+%2F+strings+%2F+hashes;%3E+observar+%E2%86%92+extrair+%E2%86%92+documentar;Ferramentas+pequenas.+Evid%C3%AAncia+limpa." alt="Enumerar, fingerprint e triage">

</div>

# Guardian Examples

Pequenos utilitários Python para **reconnaissance autorizado** e investigação
local. A tooling fica deliberadamente focada: recolher o que está visível,
identificar a resposta, fazer triage de artefactos locais e deixar a
interpretação para o operador.

## Estrutura

```text
recon/
├─ web_surface_mapper.py   # mapa de uma página: links, forms e metadata
├─ endpoint_inventory.py    # inventário de robots, sitemap e endpoints same-origin
└─ headers_fingerprint.py   # headers, esquema TLS e pistas do servidor
research/
├─ file_triage.py           # identidade e triage básica de ficheiros locais
├─ strings_extract.py       # extracção de strings ASCII/UTF-16LE
├─ hash_inventory.py        # inventário SHA-256 de ficheiro ou directório
└─ bounded_bruteforce_demo.py # exercício local de guessing limitado
```

## Arranque rápido

```powershell
python .\recon\headers_fingerprint.py https://example.com
python .\recon\web_surface_mapper.py https://example.com
python .\recon\endpoint_inventory.py https://example.com

python .\research\file_triage.py .\sample.bin
python .\research\strings_extract.py .\sample.bin
python .\research\hash_inventory.py .\samples
python .\research\bounded_bruteforce_demo.py
```

O demo de brute force é diferente de propósito: corre apenas contra um fixture
sintético em memória, usa uma lista fixa de oito candidatos e não tem rede nem
aceita um alvo fornecido pelo utilizador. Mostra credential auditing limitado,
não acesso contra um serviço real.

As ferramentas de recon fazem no máximo um pedido por recurso descoberto e
mantêm-se na mesma origem. Não fazem brute force de paths, não exploram
inputs, não contornam controlos nem lançam scans concorrentes.

## Âmbito

Usa a recon apenas contra sistemas teus ou para os quais tenhas autorização
explícita. Usa a research apenas em ficheiros que tens autorização para
inspeccionar. Consulta o [`SCOPE.md`](./SCOPE.md).

<p>
  <img src="./assets/badboy17jpg.jpg" width="24" height="24" alt="">
  <strong>BadBoy17</strong>
</p>
