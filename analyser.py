import re
import pandas as pd
import emoji
from datetime import datetime

try:
    def readChat():
        f = open('Python/WhatsApp-Analyzer/WhatsApp-Chat-Anna.txt', 'r', encoding='utf-8')
        chat = f.read()
        return chat

    """Wenn Chatnutzer neue Zeilen oder Paraghraphen verwendet, wird der Chatverlauf auch dementsprechend formatiert. 
    Hier kommt RegEx in Verwendung, um so den Chatverlauf einheitlicher zu formatieren, sodass jede Zeile einer Nachricht entspricht."""
    def cleanChat():
        f_sub = open(f'Python/WhatsApp-Analyzer/WhatsApp-Chat-sub.txt', 'w', encoding='utf-8')
        cleanedChat = re.sub('\n(?!\d{1,2}.\d{1,2}.\d{1,2}, \d{1,2}:\d{1,2} - [a-zA-Z]+)', ' ', readChat())
        f_sub.write(str(cleanedChat))
        f_sub.close()
        return cleanedChat

    days_dict = {
        'Monday': 'Montag',
        'Tuesday': 'Dienstag',
        'Wednesday': 'Mittwoch',
        'Thursday': 'Donnerstag',
        'Friday': 'Freitag',
        'Saturday': 'Samstag',
        'Sunday': 'Sonntag'
    }

    months_dict = {
        'January': 'Januar',
        'February': 'Februar',
        'March': 'März',
        'April': 'April',
        'May': 'Mai',
        'June': 'Juni',
        'July': 'Juli',
        'August': 'August',
        'September': 'September',
        'October': 'Oktober',
        'November': 'November',
        'December': 'Dezember'
    }

    def seperateDateTimeAuthor():
        dates = re.findall('\d{1,2}.\d{1,2}.\d{1,2}(?=, \d{1,2}:\d{1,2} - [a-zA-Z]+)', cleanChat())
        days = [days_dict[datetime.strptime(day, '%d.%m.%y').strftime('%A')] for day in dates if datetime.strptime(day, '%d.%m.%y').strftime('%A') in days_dict]
        months = [months_dict[datetime.strptime(month, '%d.%m.%y').strftime('%B')] for month in dates if datetime.strptime(month, '%d.%m.%y').strftime('%B') in months_dict]
        times = re.findall('(?<=\d{2}.\d{2}.\d{2}, )\d{1,2}:\d{1,2}(?= - [a-zA-Z]+)', readChat())
        names = re.findall('(?<=(?<=\d{2}.\d{2}.\d{2}, \d{2}:\d{2} - ))(?=)[a-zA-Z]+(?=:)', readChat())
        messages = [match.group(1) for match in re.finditer(r'\d{2}.\d{2}.\d{2}, \d{1,2}:\d{1,2} - [a-zA-Z]+: (.*)', cleanChat())]
        return zip(dates, days, months, times, names, messages)

    df = pd.DataFrame(seperateDateTimeAuthor(), columns=['Datum', 'Tag', 'Monat', 'Uhrzeit', 'Name', 'Nachricht'])
    pd.set_option('display.max_colwidth', None)

    print(f"Nutzer:".ljust(30) + f"{df['Name'].drop_duplicates().tolist()[0]} und {df['Name'].drop_duplicates().tolist()[1]}")
    print(f"Zeitraum des Chatverlaufs:".ljust(30) + f"{df['Datum'][0]} und {df['Datum'][df.shape[0]-1]}")
    print(f"Chattage:".ljust(30) + f"{(datetime.strptime(df['Datum'][df.shape[0]-1], '%d.%m.%y') - datetime.strptime(df['Datum'][0], '%d.%m.%y')).days}")
    print(f"Aktivster Monat:".ljust(30) + f"{df['Monat'].mode().to_string(index=False)}")
    print(f"Aktivster Tag:".ljust(30) + f"{df['Tag'].mode().to_string(index=False)}")
    print(f"Nachrichten insgesamt:".ljust(30) +  f"{df.shape[0]}")
    print(f"Wörter insgesamt:".ljust(30) + f"{len(re.findall('[a-zA-ZÄÖÜäöüß]+', str(df['Nachricht'].to_string())))}")
    print(f"Buchstaben insgesamt:".ljust(30) + f"{len(re.findall('[a-zA-ZÄÖÜäöüß]', str(df['Nachricht'].to_string())))}")
    print(f"Geteilte Medien:".ljust(30) + f"{df[df['Nachricht']=='<Medien ausgeschlossen>'].shape[0]}")
    print(f"Emojis gesendet:".ljust(30) + f"{emoji.emoji_count(cleanChat())}")
    print(f"Links geteilt:".ljust(30) + f"{len(re.findall('https?', cleanChat()))}\n")
    print(f"Gesendete Emojis von {df['Name'].drop_duplicates().tolist()[0]}".ljust(30) + str(emoji.emoji_count((df[df['Name']==df['Name'].drop_duplicates().tolist()[0]].to_string()))))
    print(f"Gesendete Emojis von {df['Name'].drop_duplicates().tolist()[1]}".ljust(30) + str(emoji.emoji_count((df[df['Name']==df['Name'].drop_duplicates().tolist()[1]].to_string()))))
except:
    print('Es ist ein Fehler aufgetreten!\n\nSkript kann nicht ausgeführt werden. Die Textdatei ist entweder beschädigt oder enthält nicht über ausreichende Daten. Um den Fehler bestmöglich zu beheben, muss der Chatverlauf direkt von WhatsApp exportiert und unbearbeitet vom Skript gelesen werden. Der Chatverlauf muss ebenfalls mindestens zwei Nachrichten und zwei Autoren mit jeweils Sender und Empfänger beinhalten. Es wird empfohlen, dass vor dem Export des Chatverlaufes die Kontaktperson mit einem Namen eingespeichert wird.')

