# Il flusso

```text
Problema → criteri concordati → lettura del codice → modifica minima
        → verifiche → review → correzioni se necessarie → consegna
```

1. **Definisci il risultato.** L'utente descrive il problema. L'agente rende
   verificabili i requisiti, senza inventare nuove richieste.
2. **Leggi il contesto.** Regole, task, codice interessato, chiamanti e baseline.
3. **Esplora solo dove serve.** Un dubbio concreto può richiedere una ricerca.
   Salva il risultato in `progress/explore/<argomento>.md`.
4. **Implementa.** Un task, uno scope chiaro, controlli proporzionati al rischio.
5. **Verifica.** Comandi del progetto, test sul comportamento e osservazione reale
   per UI o integrazioni. Riporta errori preesistenti e controlli saltati.
6. **Fai review.** Un'altra sessione o un altro agente legge il diff e riesegue
   i controlli pertinenti. Può essere Claude o Codex, in entrambe le direzioni.
7. **Consegna.** Risultato, prove, limiti e prossimo passo. Le correzioni riaprono
   la review sulle parti cambiate. Una modifica successiva può invalidare il verdetto.

I percorsi `progress/` sono relativi a `harness/`. Crea le cartelle al bisogno.
Per iniziare basta un task locale; GitHub Issues può diventare la fonte del
contratto quando serve coordinamento. Evita due backlog indipendenti.

Il passaggio tra strumenti avviene tramite task, codice e file di progress:
non presuppone memoria condivisa fra chat. Un cambio di modello non garantisce
da solo una review indipendente: servono lettura del diff e verifiche effettive.

Per lavori paralleli, separa worktree, porte e dati locali. Assegna insieme chi
scrive e chi legge lo stesso contratto. Aumenta il parallelismo solo quando il
flusso di una singola feature produce risultati verificabili.
