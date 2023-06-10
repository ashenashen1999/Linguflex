# Linguflex

Linguflex ist eine **innovative Plattform**, die eine **natürliche Interaktion** mit Textgeneratoren wie **OpenAI GPT** ermöglicht und die Erstellung schlanker, effizienter **Erweiterungsmodule** unterstützt. Vorgefertigte Module bieten eine Vielfalt an Funktionen – von Terminkalender und E-Mail-Verwaltung über Echtzeitzugriff auf Webinformationen, Wetterupdates oder Nachrichten bis hin zur Medienwiedergabe und Steuerung von Smart-Home-Geräten. Linguflex hebt sich hervor durch seine **Erweiterbarkeit**, **kompakten Modulcode** und die **Flexibilität**, individuellen Anwendungsanforderungen gerecht zu werden.

### Voraussetzungen
- Python 3.9.9
- OpenAI API key  
Für einen OpenAI API key gegebenenfalls Account bei OpenAI eröffnen ([platform.openai.com](https://platform.openai.com/)). Anschließend rechts oben auf den Profilnamen klicken, dann im Menü auf "View API Keys" und anschließend auf "Create new secret key".

### Installation

- [Python 3.9.9](https://www.python.org/downloads/release/python-399/) installieren
- Linguflex Repository kopieren ("klonen")  
Zip-File herunterladen und entpacken oder bei installiertem Github `git clone https://github.com/KoljaB/Linguflex.git` ausführen
- in das Verzeichnis wechseln `cd linguflex`, (optional) virtuelle Umgebung erstellen mit `python -m venv env` und `env/bin/activate`
- Abhängigkeiten installieren  
für die Vanilla-Installation: `pip install -r requirements.txt`
für die Basis-Installation: `pip install -r requirements_basic.txt`
für die Komplett-Installation: `pip install -r requirements_full.txt`
- OpenAI API Key eintragen
Den OpenAI API key in die config.txt in der Sektion [openai_generator] eintragen. 

Hinweis: Nutzung zusätzlicher Module über Vanilla hinaus erfordern zum Teil weitere Anpassungen in der Konfigurationsdatei wie zB das eintragen weiterer API-Keys. Näheres dazu in der Beschreibung der jeweiligen Module.

### Start von Linguflex
Konsolenfenster öffnen und folgendes eingeben:  
  
`python linguflex`

### Konfiguration
Eine Linguflex-Konfiguration ist eine Textdatei, welche die zu ladenden Modulen und deren Einstellungen beschreibt. Standardmäßig lädt Linguflex die Konfiguration, die in der Datei config.txt hinterlegt ist. Optional kann der Pfad zu einer anderen Konfigurationsdatei per Kommandozeilenparameter übergeben werden.  

Es werden drei Beispielkonfigurationen mitgeliefert:  
1. Vanilla (Sprachkommunikation mit dem GPT-Modell)
2. Basis (grundlegende Erweiterungsmodule)
3. Komplett (alle verfügbaren Module)

Es wird empfohlen, mit der einfachen Vanilla-Konfiguration zu beginnen und dann sukzessive präferierte Module zu ergänzen, da deren Inbetriebnahme oft mit zusätzlichen Schritten verbunden ist. Wie ein einzelnes Modul in der config.txt angelegt und konfiguriert wird kann den Dateien config_basic.txt oder config_full.txt entnommen werden.

### Module
In der Sektion [modules] der config-Datei werden die zu ladenden Module angegeben. Linguflex lädt und startet alle Module in der hier angegebenen Reihenfolge.

<br>

## Vanilla-Konfiguration
`microphone_recorder`
`whisper_speechtotext`
`openai_generator`
`system_texttospeech`  

Diese einfache Grundkonfiguration wird zur ersten Inbetriebnahme empfohlen und ermöglicht eine grundlegende Sprachkommunikation mit der Chat KI. Sie ist in config_vanilla.txt und initial in der config.txt hinterlegt. 

Zunächst den OpenAI API key in die config.txt in der Sektion [openai_generator] eintragen. 
```
[openai_generator]
openai_api_key=ENTER YOUR OPENAI API-KEY HERE
```
Alternativ kann der Key auch in die Umgebungsvariable LINGU_OPENAI_API_KEY geschrieben werden.

Konfigurationsparameter der Vanillakonfiguration:
Der Mikrofon-Rekorder nimmt auf, sobald der Eingangspegel über dem in der volume_start_recording festgelegten Schwellwert steigt und beendet die Aufnahme, wenn der Pegel unter den von volume_stop_recording festgelegten Wert fällt. Wenn GPT 4 statt GTP 3.5 Turbo verwendet werden soll, den Wert des Parameters gpt_model auf "gpt-4" ändern.

Die bestehende Whisper-Installation nutzt die CPU. Die Spracherkennung kann durch Umstellung auf GPU beschleunigt werden: dazu PyTorch mit CUDA-Support installieren (Anleitungen dazu sind im Internet zu finden), whisper_speechtotext stellt automatisch auf GPU-Nutzung um, sobald CUDA verfügbar ist.

<br>

## Basis-Konfiguration
Die Basis-Konfiguration liegt in config_basic.txt und erweitert Vanilla um ein User Interface, ausgereiftere Text-To-Speech Module, Terminkalender-Integration, EMail-Support, den Abruf von Echtzeit-Informationen mit Google, ein Modul zur Steuerung des Charakters / der Persönlichkeit der Chat-KI und ein Modul, welches der Sprachmodell-KI ermöglicht, selbständig Aktionen auszuführen, die durch andere Module bereitgestellt werden.

### UI-Modul
`user_interface`  
  
Standardmäßig zeigt Linguflex nur ein Konsolenfenster mit Loggingmeldungen an. Diese Modul bietet ein ansprechenderes User Interface zur Anzeige der Kommunikation mit der Chat KI. Breite und Höhe des Fensters können in der config.txt eingestellt werden (siehe Beispielkonfiguration in config_basic.txt).

### Text-To-Speech-Module
`edge_texttospeech`
`azure_texttospeech`
`elevenlabs_texttospeech`  
  
Liefern professionellere Sprachausgabe. Dazu wird das Modul Sprachausgabemodul "system_texttospeech" aus der Sektion [modules] der Konfigurationsdatei entfernt und durch eines der oben angegebenen Sprachausgabemodule ersetzt. 
edge_texttospeech nutzt zur Sprachausgabe das Edge-Browserfenster und bietet so kostenlose, hochqualitative Sprachausgabe bei reduzierter Stabilität und Komfort (aufgrund der Verwendung des Browserfensters). 
azure_texttospeech hochqualitativ, stabil und komfortabel, benötigt allerdings einen Microsoft Azure API Key. Ein Account kann unter [portal.azure.com](https://portal.azure.com/) erstellt werden, dann eine Ressource erstellen und in der Ressource links auf "Schlüssel und Endpunkt" klicken.
elevenlabs_texttospeech ist ebenfalls hochqualitativ, stabil und komfortabel und bietet eine emotionalere Sprachausgabe. Zur Nutzung wird ein Elevenlabs API Key benötigt. Ein Account kann unter [elevenlabs.io](https://beta.elevenlabs.io/) erstellt werden, dann rechts oben auf das Profilbild und auf "Profile" klicken.
API Keys werden in die config.txt eingetragen oder als Umgebungsvariable (LINGU_AZURE_SPEECH_KEY bzw LINGU_ELEVENLABS_SPEECH_KEY) definiert.

### Terminkalender-Modul
`google_calendar`  
  
Integration mit dem Google Calendar zum Abruf und Eintragen von Terminen. 
Benötigt die Datei credentials.json im Ausführungsverzeichnis von Linguflex. Dazu in [console.cloud.google.com](https://console.cloud.google.com/) ein Projekt anlegen, und unter "APIs und Dienste" links auf "Anmeldedaten". Dann auf "Anmeldedaten erstellen" und eine neue OAuth-ClientId erstellen. Diese wird anschließend unter OAuth 2.0-Client-IDs gelistet, dort ist ganz rechts ein Pfeil nach unten. Dort draufklicken und dann auf "JSON herunterladen". 
Fehlt die credentials.json wird die Logmeldung ""[calendar] ERROR:[Errno 2] No such file or directory: 'credentials.json'" ausgegeben. 
Bei der ersten Ausführung auf einem Gerät wird der Benutzer weiterhin aufgefordert, seine Google-Anmeldeinformationen einzugeben. Diese Informationen werden dann in einer Datei token.pickle gespeichert, um zukünftige Anmeldungen zu vermeiden. 

Kalenderdaten können auch von einfacheren Sprachmodellen wie GPT 3.5 abgerufen werden. Für das Eintragen von Terminen mit umgangssprachlichen Zeitreferenzen ("morgen", "in drei Tagen"), benötigt man jedoch ein performantes Modell wie GPT-4.

### EMail-Modul
`email_imap`  
  
Abruf von EMails. IMAP-Server, Benutzername und Passwort werden in die Sektion [email_imap] der Konfigurationsdatei geschrieben, siehe Beispiel in config_basis.txt.

### Abruf von Echtzeit-Informationen aus dem Internet
`google_information`  
  
Abruf von Echtzeitinformationen aus dem Internet. Benötigt einen SerpAPI-Key (erhältlich unter [serpapi.com](https://serpapi.com/)), der in die Konfigurationsdatei eingetragen oder in die Umgebungsvariable LINGU_SERP_API_KEY geschrieben wird.

### Persönlichkeits-Modul
`personality_switch`  
  
Schreibt der Chat-KI einen vorgefertigten Charakter zu, der dann während einer Session gewechselt werden kann. Der Start-Charakter kann in der Konfigurationsdatei festgelegt werden. 

### Modul zur selbständigen Aktionsauswahl
`auto_action`  

Wird die vom Benutzer gestellte Anfrage vom Sprachmodell nicht erfüllt, prüft dieses Modul die von anderen Modulen bereitgestellten Aktionen und setzt diese ein, wenn sie zielführend sind. Das GPT 3.5 Modell kommt je nach Komplexität der zur Verfügung gestellten Aktionen an seine Grenzen, GPT 4 performt deutlich besser. 

<br>

## Komplett-Konfiguration
Die Komplett-Konfiguration ist in config_full.txt hinterlegt und beinhaltet zusätzlich zur Basic-Konfiguration noch Audio- und Video-Ausspiel, aktuelle Wetterdaten, Smart-Home Lichtsteuerung, Abruf von Nachrichten, Suche nach Bildern im Internet, Erzeugung von Bildern mit Bildgeneratoren, den Abruf aktueller Investmentdepot-Daten und Spiele.

### Modul für Audio- und Videoausspiel
`media_playout`  
  
Nutzt Youtube und Firefox, um Audios und Videos auszuspielen. Benötigt einen zur installierten Firefox-Version passenden Geckodriver (ein einzelnes Executable zur Automatisierung von Firefox, erhältlich hier: https://github.com/mozilla/geckodriver/releases) im Ausführungsordner von Linguflex. Ich habe mit dem Geckodriver 0.33.0 Probleme gehabt, während 0.32.2 gut funktionierte - dies mag aber im Zusammenspiel mit der installierten Firefox-Version (114 bei mir) bei jedem anders sein.

### Wetter-Modul
`weather_summary`  
  
Benötigt einen OpenWeatherMap API Key (https://openweathermap.org/api), der in der Konfigurationsdatei oder in der Umgebungsvariable LINGU_OPENWEATHERMAP_API_KEY hinterlegt wird. In der Konfigurationsdatei sollte die default_city von Hamburg auf den eigenen Wohnort geändert werden.

### Nachrichten-Modul
`news_summary`  
  
Fasst die aktuellen Tagesnachrichten zusammen. Das Sprachmodell kann nach den Hauptnachrichten oder Nachrichten aus den Bereichen Wirtschaft, Technik, Forschung, Inland, Ausland oder Gesellschaft befragt werden. Als Nachrichtenquelle wird Tagesschau genutzt, die Informationen werden per BeautifulSoup gepollt.

### Bildersuche-Modul
`pic_search`  
  
Sucht im Internet nach einem Bild und zeigt dieses an. Benötigt einen Google API- und CX-Schlüssel, die in der Konfigurationsdatei (siehe config_full.txt) oder in den Umgebungsvariablen LINGU_GOOGLE_API_KEY und LINGU_GOOGLE_CX_KEY hinterlegt werden. Für den Google API Key auf https://console.cloud.google.com mit dem Google Konto anmelden (gegebenenfalls erstellen). Neues Projekt erstellen, in der Bibliothek nach "Custom Search API" suchen und für das Projekt aktivieren. Im "Credentials"-Bereich auf "+ Create Credentials", dann "API key" wählen. Für den Google Search Engine (CX)-Schlüssel auf https://cse.google.com/cse/all mit dem Google Konto anmelden. Neue Suchmaschine erstellen und die Informationen ausfüllen (z.B. welche Websites durchsucht werden sollen), dann auf "Erstellen".  Dann auf den Namen Ihrer Suchmaschine, um die Details anzuzeigen und man sieht die "Suchmaschinen-ID", das ist der benötigte CX-Schlüssel.

### Bildererzeugungs-Modul
`pic_generate`  
  
Erzeugt ein Bild mit dem DALL-E Bildgenerator unter Nutzung der OpenAI API und zeigt dieses an. Zu jeder Nutzung fallen Kosten an ([openai.com/pricing](https://openai.com/pricing)).

### SmartHome Lichtsteuerung
`lights_control`  
  
Steuert Farben und Helligkeit von Tuya Smartbulbs Lampen. Zu jeder Lampe wird ein frei vergebbarer Name, sowie Device-Id, die IP-Adresse der Lampe, den "Local Key" und Version in der Konfigurationsdatei hinterlegt. Beispieleinträge sind in der config_full.txt zu finden. Auf der [Webseite des tinytuya-Projekts](https://pypi.org/project/tinytuya/) gibt es unter der Rubrik "Setup Wizard - Getting Local Keys" eine ausführliche Anleitung, wie man an diese Daten kommt. 

### Spiele-Modul
`emoji_game`  
  
Zeigt eine Auswahl von Emojis, die ein "zufällig" ausgewähltes Werk (Film, Buch oder Serie) repräsentieren, welches daraufhin erraten werden muss.

### Depot-Modul
`depot_summary`  
  
Abruf und Zusammenfassung von Investmentdepot-Daten. Das Investment-Depot wird als comdirect-Musterdepot angelegt und der externe Link dazu ("Aktionen gesamtes Musterdepot" => "Freunden zeigen") in der Konfigurationsdatei abgelegt.

<br>

## Ausblick

Als nächstes folgt ein Webserver-Modul, das die Bedienung von LinguFlex mit dem Smartphone von überall aus ermöglicht. Ein funktionierender Webserver samt Client existiert bereits, zur Veröffentlichung ist der Code jedoch nicht ausgereift genug. Der jetzige Webserver ist eine eigenständige Flask-Anwendung, um dem Linguflex-Server nicht die Implementierung als CORS/Flask-Anwendung aufzuzwingen. Die daraus resultierende Interprozesskommunikation zwischen Linguflex- und Webserver basiert derzeit auf Textdateien und einer ganzen Reihe unschöner Spin/Busy-Waits. Dies aber auch generell Flask als Basis für den Webserver sind aus Sicherheitsgründen nicht ausreichend für ein Release, spätestens wenn man Ports nicht nur für das lokalen Netzwerk, sondern nach außen freigeben möchte, um Linguflex auch von unterwegs aus nutzen zu können.
