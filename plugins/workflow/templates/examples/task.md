# Esempio didattico: errore di caricamento di una lista

Esempio inventato e neutro: non descrive un intervento eseguito o test già passati.

## Problema

Quando il servizio risponde con un errore, la pagina mostra «nessun elemento».
L'utente non distingue un servizio non disponibile da una lista vuota.

## Acceptance

- [ ] Una risposta valida senza elementi mostra lo stato vuoto.
- [ ] Una risposta valida con elementi mostra la lista.
- [ ] Un errore mostra un messaggio comprensibile e consente di riprovare.
- [ ] Gli altri utilizzatori della funzione condivisa mantengono il comportamento corretto.

## Scope

Da determinare leggendo il progetto: funzione di caricamento, chiamanti coinvolti,
presentazione dell'errore e relativo test. Nessuna riscrittura del client HTTP.

## Depends on

Nessuna; occorre individuare i file reali prima di iniziare.

## Come procedere

L'implementer controlla se un `catch` restituisce `[]` e nasconde l'errore.
Verifica tutti i chiamanti prima di cambiare il contratto. Riusa la gestione
degli errori già presente e aggiunge un controllo sul caso di fallimento.

Il reviewer legge il diff e verifica errore, lista vuota e riprova. Registra i
comandi effettivamente eseguiti. Finché queste prove mancano, non scrive APPROVED.
