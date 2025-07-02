[EN]

# Python-apps

<b> Assignment 1 - object oriented application witch text mode. </b>
- simulation involving a wolf that tries to catch sheep scattered in a meadow, which uses text mode,
- saving the position of every animal at the end of each round to a json file,
- saving the number of alive sheep at the end of each round to an csv file,
- handling the command-line arguments using argparse module,
- loading an absolute value of the limit imposed on each coordinate of the initial positions of sheep, a distance of sheep movement, and a distance of wolf movement from a configuration INI file whose name is specified as part of the -c/--config command-line argument,
- logging events to a log file using logging package.
- two stop conditions - the wolf has caught all the sheep or the sheep have survived a certain number of rounds.

<b>Assignment 2 - simple flask app. </b>
A web application with an HTML interface and REST API, built using a web framework (e.g., Flask) and ORM (e.g., SQLAlchemy), supporting CRUD operations on a relational database with a single table (ID, continuous features as floats, one categorical feature as int), with full data validation and proper error handling (400/404).
Supported routes:
- / – home page displaying all records in a table with delete buttons,
- /add – form to add a new record (POST with validation),
- /delete/<record_id> – deletes a record by ID (POST, 404 if not found),
- GET /api/data – returns all records as JSON,
- POST /api/data – adds a new record from JSON input (400 on validation error),
- DELETE /api/data/<record_id> – deletes a record by ID (404 if not found).
Validation ensures correct data types and formats. On failure, appropriate HTTP responses with error messages are returned. Basic navigation and optional custom styling are supported.

<b> Assignment 3 - a site for comparing the popularity of entries on Wikipedia. </b>

[PL]

# Aplikacje w Pythonie

<b> Assignment 1 - obiektowo zorientowana aplikacja konsolowa - symulacja gry z udziałem wilka próbującego złapać owce rozrzucone na łące z poniższą charakterystyką:
- na koniec każdej rundy pozycje każdgego zwierzęcia są zapisywane do pliku json,
- na koniec każdej rundy liczba żywych owiec jest zapisywana do pliku csv,
- obsługa argumentów wiersza poleceń za pomocą modułu argparse,
- ładowanie wartości bezwzględnej limitu nałożonego na każdą współrzędną początkowych pozycji owiec, odległości ruchu owiec i odległości ruchu wilka z pliku INI konfiguracji, którego nazwa jest określona jako część argumentu wiersza poleceń -c/--config,
- rejestrowanie zdarzeń w pliku dziennika za pomocą pakietu logging.
- dwa warunki stopu - wilk złapał wszystkie owce lub owce przetrwały określoną liczbę rund.

<b> Assignment 2 - prosta aplikacja we flasku </b>
Aplikacja webowa z interfejsem HTML i REST API, oparta na frameworku Flask i SQLAlchemy, umożliwiająca operacje CRUD na relacyjnej bazie danych z jedną tabelą (ID, cechy ciągłe jako float, cecha kategoryczna jako int), z pełną walidacją danych i obsługą błędów (400/404).
Obsługiwane ścieżki:
- / – strona główna z tabelą wszystkich rekordów i możliwością ich usunięcia,
- /add – formularz dodawania rekordu (POST z walidacją),
- /delete/<record_id> – usuwa rekord po ID (POST, 404 jeśli nie istnieje),
- GET /api/data – zwraca wszystkie rekordy jako JSON,
- POST /api/data – dodaje rekord z JSON-a (walidacja, 400 przy błędzie),
- DELETE /api/data/<record_id> – usuwa rekord po ID (404 jeśli brak rekordu).
Walidacja sprawdza poprawność typów i zakresów danych wejściowych. Przy błędach generowane są odpowiednie komunikaty i kody HTTP. Nawigacja między stronami oraz stylizacja HTML są wspierane, ale opcjonalne.

<b> Assignment 3 - strona służąca do porównywania popularności haseł na Wikipedii.
