# Mini-WhatsApp-Chatanalysis

Kurzanalyse von WhatsApp-Chats

Das Skript liest exportierte WhatsApp-Chats und extrahiert die Daten. Möglicherweise müssen einige Bibliotheken installiert werden, bevor das Skript ausgeführt werden kann.

##### Unterstützte Analysen
------------------------------
- Name des Senders und Empfängers
- Zeitspanne des Chatverlaufes
- Chattage
- Aktivster Monat
- Aktivster Tag
- Nachrichten insgesamt
- Wörter insgesamt
- Buchstaben insgesamt
- Geteilte Medien
- Emojis gesendet
- Links geteilt

##### Vorschau
------------------------------
```
WhatsApp-Chatverlauf zwischen Anna und Anilo:

Chatverlauf zwischen 16.03.23 und 03.04.23
Chattage: 18
Aktivster Monat: März
Aktivster Tag: Freitag
Nachrichten insgesamt: 870
Wörter insgesamt: 9283
Buchstaben insgesamt: 45486
Geteilte Medien: 80
Emojis gesendet: 661
Links geteilt: 7
```

### Mindestanforderungen
----------------------
- Python 3.6+

### Hinweis
----------------------
- Dieser Skript verwendet RegEx, um die Daten extrahieren zu können.
- Es unterstützt nur folgendes Chatmuster:
```
    "01.01.01, 00:00 - Kontaktname: Dies ist eine Nachricht."
  ```
