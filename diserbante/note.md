
## Come funziona l'api di tulip
    - a /api/query ti viene dato un dump ti tutti gli id delle flow (stream di traffico)
        - Si possono impostare dei filtri ad esempio solo sui flag-in come in dumper (li ho presi dal codice sorgente / BurpSuite)
        - Tulip usa Mongo, ci interessano gli oid

    - a /flow/{$oid} c'è il traffico associato all'oid tal dei tali
        -gli oid sono sequenziali
        -basta stampare il risultato e mandarlo a destr farm

    - Tulip di base non ha autenticazione, va aggiunta con una proxy
        - Magari c'è chi non la implementa bene e permette comunque l'accesso all'api(??)

    - Si può anche filtrare per servizi



## Destructive Farm
    - Può essere riconosciuto dalla risposta 'Could not verify your access level for that URL. You have to login with proper credentials' se l'autenticazione è abilitata
    - Di default l'autenticazione sull'api è spenta (bad idea, ma solo per postare flag, non per prenderle)
    - Questo vuol dire che possiamo mandare a chi tiene destr farm con l'api aperta sulla vulnbox tutte le flag che vogliamo (c'è la possibilità anche di fare denial of service, ma non facciamo così schifo)
    - Si può flaggare per conto di altri (credo sia molto avanzata come strategia ma potrebbe valere? Non credo sia legale)
        - Side note analizzando le formule si vede che una strategia feasible è flaggare per conto dei team deboli contro chi sta sopra di team

            -La formula dei punti è "simmetrica" ed è un simil-ELO

            ```
            scale = 15 * sqrt(5) 
            norm = ln(ln(5)) / 12 
            offense_points[flag] = scale / (1+exp((sqrt(score[attacker][service]) - sqrt(score[victim][service]))*norm))
            defense_points[flag] = min(victim_score, offense_points)
            ```

for flag in lost_flags[team][service]: 
  score[team][service] -= defense_points[flag]

    - L'api di destr farm è molto semplice 
        - /api/get_config dà la config, meno i parametri privati (peccato)
        - /api/post_flags permette di postare flag con una post, in json
            ex : {"flag": "K893ALON7772TGWI2IMOYPOPXXA3521=", "sploit": "dumper.py", "team": "Team #35"}
            

## Caronte TODO (Dio ci salvi è documentato malissimo)
