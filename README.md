# prgPraxe
Popis projektů na mém githubu.
Projekty jsou řazeny chronologicky.



# spotify program
- Jedná se pouze o malý script, který používám jelikož nemám spotify premium
- Script má za úkol detekovat zda se pustí reklama na spotify, a pokud ano, spotify se vypne a zapne a následně spustí další song ve frontě

# GUI toDoList
- První zkušenost se soubory a python GUI
- Todolist není nijak graficky zajímavý, soustředil jsem se spíše na funkčnost porgramu než na jeho vzhled
- Sám ho používám

# Star Wars Web
- Webová stránka kam si zapisuju Star Wars filmy, hry, komiksy atd. které bych si rád prošel
- Stránka je pouze pro osobní využití, proto jsem se hlavně soustředil na funkčnost mého scriptu
- Ve zkratce má stránka být schopná uložit v jakém stádiu se daný Star Wars projekt nachází (např. červená vlaječka u knihy značí že se teprve chystám si danou knihu přečíst)
- Tvorbě webových stránek se ovšem moc nevěnuji, spíše mě zajímá tvorba aplikací

# guiBankSystem
- Jeden z větších projektů
- Snažil jsem se zde i o nějakou grafickou úpravu
- Chtěl jsem se celkově naučit něco málo o vývoji "mobilních" aplikací, proto jsem si zvolil bankovnictví
- Uživatel si může vytvořit účet, pracovat se svými financemi, nastavit tmavý a světlý režim, posílat peníze atd.
- Procvičil jsem si zde práci s OOP (i když oop v pythonu není nejlepší volba), práci s menší databází a celkově vývoj něčeho trochu většího
- Jelikož se jedná o jeden z prvních projektů tak je vše v jednom souboru (tudíž totální nepřehlednost).

# simpleTextSplitter
- Jedná se o python scritp, který rozdělí předný text do textových souborů podle počtu znaků zadaných uživatelem.
- Script jsem napsal protože nemám předplaceného chatGPT, a omylem jsem do jednoho důležitého chatu (který byl hodně dlouhý) dal přílohu. Bot tedy po nějakém čase přestane psát protože mi došel limit a já si chtěl naši konverzaci přepsat do jiného chatu. Konverzace ale byla moc dlouhá pro zprávu a tak jsem ji nějak potřeboval rozdělit.

# SongSelector
- Další python script. Tentokrát slouží k mému hraní na kytaru.
- Někdy se stává že nevím jakou písničku si zahrát nebo se naučit.
- Script tedy slouží k tomu, že si do něj nahraju svoje oblíbené písničky a pak si zvolím kolik jich chci náhodně vybrat.
- Mohu si písničky i mazat a zobrazit.
- Písničky se ukládají jednoduše do csv souborů.
- Je to dost jednoduchý script, ale často ho používám.

# chatApp
- Jedná se o základní chatovací aplikaci. Uživatel může vytvořit chatroom a pozvat ostatní uživatele. Vlastník dané chatroom může ostatní vyhodit a ostatní mohou pozvat další       uživatele.
- Jedná se o první Python projekt který jsem si rozdělil do složek a souborů, aby vše nebyl v jednom souboru. Projekt je tak přehlednější. 
- Tímto projektem jsem se naučil práci s Flasekem, Socketio a sqlalchemy
- Projekt ovšem nemá nějak zajímavý front end, nastyloval jsem pouze důležité věci, soustředil jsem se na funkčnost appky.

# phpPraxeNetteProject
- Jedná se o webovou aplikaci blogu
- Na aplikaci jsem pracoval v Plzeňské firmě RTsoft, kde jsem byl na praxích
- Blog jsem programoval v PHP frameworku Nette
- Na aplikaci jsem dělal vše sám a díky tomu jsem se na tomto testovacím projektu hodně naučil (menší front-end, práce s db, přemýšlení do budoucna při psaní kódu, úprava kódu)
- Zatím můj největší projekt

# Star Wars Web V4
- Vylepšená verze mého původního Star Wars webu
- Projekt je naprogramován ve frameworku Nette v jazyce PHP
- Jednotlivá díla se zde přidávají přímo na stránce a ukládají se do databáze
- Projekt ještě není kompletní (chybí přívětivější front end), ale možnosti na přidání, smazání a upravení díla jsou naimplementována.
- Při programování jsem si také poradil s tim, jak řadit časově díla, pokud budu chtít vložit nové dílo mezi dvě existující.

# FinanceWeb
- První čistě FE projekt
- Dospěl jsem k názoru že je třeba se naučit FE a tak jsem si vybral cizí design který jsem se rozhodl zreprodukovat
- Soustředil jsem se čistě na design bez responzivity, abych se naučil přenést design do kódu

# GeorgeDeskotop
- Další FE projekt
- Využil jsem zkušenosti z FinanceWeb a přidal jsem kompletní responzivitu
- Projekt mě hodně naučil a v tvorbě UI jsem se extrémně posunul.

# Discord-Playtime
- Jedná se o další mini script, který vznikl protože jsem byl s něčím opět nespokojen.
- Dlouho mě štvalo že na platformě Ubisoft Connect není u některých her vidět odehraný čas. U některých her je zase čas vidět, ale s velkou odchylkou oproti Steamu.
- Jelikož Discord počítá odehrané hodiny u her (pokud je zapnutá funkce zobrazení aktivity), tak jsem si od Discordu vyžádal log s mojí aktivitou.
- Tyto obrovské log soubory s více jak milionem řádků následně zpracoval můj program, který ke každé hře z logu vytáhl kolik jsem na každé hře nahrál.
- Nutno podotknout, že program nejdřív musel z jiných záznamů spojit jméno hry a její ID a až potom z úplně jiných záznamů podle ID hry najít nejvyšší total playtime. Záznamy totiž byly seřazeny naprosto náhodně.
