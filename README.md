# kit

Skill, agenti e strumenti che [cervera.studio](https://cervera.studio) usa su progetti reali,
pubblicati come marketplace di plugin per Claude Code.

```
/plugin marketplace add cervera-studio/kit
/plugin install workflow@cervera-studio
/plugin install process-map@cervera-studio
```

| Plugin | Cosa fa |
|---|---|
| [workflow](plugins/workflow) | Agenti leader, implementer, reviewer e architect, più i template di progetto per lavorare con Claude e Codex su task delimitati e revisionati. |
| [process-map](plugins/process-map) | Mappa i processi di un'azienda reparto per reparto in un file YAML e li trasforma in una pagina HTML con diagramma e costi mensili. |

## workflow

Un metodo ricavato da workflow reali, ripulito dai dettagli dei clienti. Non c'è un
orchestratore automatico: il flusso si segue anche a mano.

1. Leggi [il flusso](plugins/workflow/templates/harness/FLOW.md) e [l'esempio](plugins/workflow/templates/examples/task.md).
2. Copia nel tuo progetto i file di [templates/](plugins/workflow/templates) e compila
   il contesto e i comandi in `AGENTS.md`. Se esiste già, unisci le regole utili
   senza sovrascriverlo.
3. Per Codex, chiedi esplicitamente di leggere `AGENTS.md` e il file del ruolo che ti
   serve, da [agents/](plugins/workflow/agents).
4. Prova una piccola modifica, verifica il risultato, poi passa alla review.

Non servono tutti i ruoli per cambiare una riga. Il flusso completo serve quando c'è
un requisito da chiarire, più file coinvolti o un rischio concreto.

**Avvio:**

> Leggi AGENTS.md e il task concordato. Individua il flusso interessato e tutti
> i chiamanti prima di modificare codice. Proponi la modifica minima e i controlli
> pertinenti, poi completa il lavoro autorizzato. Registra evidenze e prossimo
> passo in harness/progress/current/nome-task.md.

**Passaggio da Claude a Codex, o viceversa:**

> Riprendi il task dal file harness/progress/current/nome-task.md. Leggi i file
> indicati e controlla il diff reale. Non assumere che il report sia corretto.
> Esegui il prossimo passo e aggiorna il file con ciò che hai osservato.

**Secondo parere:**

> Usa l'agente harness-reviewer. Controlla criteri di accettazione, diff e verifiche.
> Non modificare il codice prodotto. Scrivi rilievi riproducibili e verdetto in
> harness/progress/review/nome-task.md.

Nessun `init.sh` viene incluso o dato per esistente: usa i comandi di verifica del tuo
progetto. Una verifica saltata va riportata come tale; un exit code zero da solo non
prova che tutto sia passato. Prima di automatizzare con gli hook, fai funzionare il
flusso manuale.

## process-map

Chiedi a Claude di mappare un processo: intervista reparto per reparto, scrive lo YAML
e genera la pagina. Oppure usa lo script direttamente (serve [uv](https://docs.astral.sh/uv/)):

```sh
uv run plugins/process-map/skills/process-map/render.py plugins/process-map/skills/process-map/example.yaml
```

Ogni passaggio ha owner, stato (`live`, `testing`, `idea`), minuti al mese e tool con
costo mensile. La pagina mostra il diagramma per reparto e i costi di lavoro e tool;
un tool usato da più passaggi viene contato una volta sola.
Formato: [example.yaml](plugins/process-map/skills/process-map/example.yaml).

## Cosa non c'è

Credenziali, configurazioni personali, sessioni, dati di clienti e accessi MCP non
fanno parte del kit. Ciascuno configura i propri strumenti.
