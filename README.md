[EN]

# Python-apps

### Assignment 1 - object oriented application witch text mode. 
- simulation involving a wolf that tries to catch sheep scattered in a meadow, which uses text mode,
- saving the position of every animal at the end of each round to a json file,
- saving the number of alive sheep at the end of each round to an csv file,
- handling the command-line arguments using argparse module,
- loading an absolute value of the limit imposed on each coordinate of the initial positions of sheep, a distance of sheep movement, and a distance of wolf movement from a configuration INI file whose name is specified as part of the -c/--config command-line argument,
- logging events to a log file using logging package.
- two stop conditions - the wolf has caught all the sheep or the sheep have survived a certain number of rounds.

### Assignment 2 - simple flask app.
<br>A web application with an HTML interface and REST API, built using a web framework (e.g., Flask) and ORM (e.g., SQLAlchemy), supporting CRUD operations on a relational database with a single table (ID, continuous features as floats, one categorical feature as int), with full data validation and proper error handling (400/404).
Supported routes:
- / – home page displaying all records in a table with delete buttons,
- /add – form to add a new record (POST with validation),
- /delete/<record_id> – deletes a record by ID (POST, 404 if not found),
- GET /api/data – returns all records as JSON,
- POST /api/data – adds a new record from JSON input (400 on validation error),
- DELETE /api/data/<record_id> – deletes a record by ID (404 if not found).
Validation ensures correct data types and formats. On failure, appropriate HTTP responses with error messages are returned. Basic navigation and optional custom styling are supported.

### Assignment 3 - a site for comparing the popularity of entries on Wikipedia. 
- the site was built using the following technologies: Python/Flask (Backend), HTML/Bootstrap/JavaScript (Frontend) and Wikipedia API.
- the site allows you to compare the popularity of articles on Wikipedia,
- the form suggests the names of existing articles on Wikipedia to the user based on the letters they have entered so far (based on the Wikipedia API),
- the form allows you to select the Wikipedia language versions from which the user would like to compare articles (also based on the API of existing language versions),
- the form allows the user to select a date range, with simple validation that these are not dates from the future, and that the end date is later than the start date,
- the names of articles are automatically translated into the languages ​​of the language versions that have been selected,
- the chart was created using the Boteh library and has 3 interactions - date slicer, filtering with extinction after clicking the entry name on the legend and zooming,
- data on the number of article views on individual days is also available in the table below the chart and can be downloaded in _csv_ format.

[PL]

# Aplikacje w Pythonie

### Assignment 1 - obiektowo zorientowana aplikacja konsolowa:
- symulacja gry z udziałem wilka próbującego złapać owce rozrzucone na łące
- na koniec każdej rundy pozycje każdgego zwierzęcia są zapisywane do pliku json,
- na koniec każdej rundy liczba żywych owiec jest zapisywana do pliku csv,
- obsługa argumentów wiersza poleceń za pomocą modułu argparse,
- ładowanie wartości bezwzględnej limitu nałożonego na każdą współrzędną początkowych pozycji owiec, odległości ruchu owiec i odległości ruchu wilka z pliku INI konfiguracji, którego nazwa jest określona jako część argumentu wiersza poleceń -c/--config,
- rejestrowanie zdarzeń w pliku dziennika za pomocą pakietu logging.
- dwa warunki stopu - wilk złapał wszystkie owce lub owce przetrwały określoną liczbę rund.

### Assignment 2 - prosta aplikacja we flasku 
<br>Aplikacja webowa z interfejsem HTML i REST API, oparta na frameworku Flask i SQLAlchemy, umożliwiająca operacje CRUD na relacyjnej bazie danych z jedną tabelą (ID, cechy ciągłe jako float, cecha kategoryczna jako int), z pełną walidacją danych i obsługą błędów (400/404).
Obsługiwane ścieżki:
- / – strona główna z tabelą wszystkich rekordów i możliwością ich usunięcia,
- /add – formularz dodawania rekordu (POST z walidacją),
- /delete/<record_id> – usuwa rekord po ID (POST, 404 jeśli nie istnieje),
- GET /api/data – zwraca wszystkie rekordy jako JSON,
- POST /api/data – dodaje rekord z JSON-a (walidacja, 400 przy błędzie),
- DELETE /api/data/<record_id> – usuwa rekord po ID (404 jeśli brak rekordu).
Walidacja sprawdza poprawność typów i zakresów danych wejściowych. Przy błędach generowane są odpowiednie komunikaty i kody HTTP. Nawigacja między stronami oraz stylizacja HTML są wspierane, ale opcjonalne.

### Assignment 3 - strona służąca do porównywania popularności haseł na Wikipedii.
- strona zbudowana w technologiach: Python/Flask (Backend), HTML/Bootsrap/JavaScript (Frontend) i Wikipedia Api.
- strona umożliwia porównywanie popularności artykułów na Wikipedii,
- formularz podpowiada użytkownikowi nazwy istniejących na Wikipedii artykułów na podstawie wprowadzonych przez niego dotychczas liter (na podstawie API Wikipedii),
- formularz umożliwia wybranie wersji językowych Wikipedii, z których artykuły użytkownik chciałby porównać (również na podstawie API istniejących wersji językowych),
- formularz umożliwia wybranie przez użytkownika zakresu dat, z prostą walidacją aby nie były to daty z przyszłości, a także aby data końcowa była później niż początkowa,
- nazwy artykułów są automatycznie tłumaczone na języki tych wersji językowych, które zostały wybrane,
- wykres został stworzony przy pomocy biblioteki Boteh i posiada 3 interakcje - slicer dat, filtrowanie z wygaszeniem po kliknięciu nazwy hasła na legendzie oraz przybliżenie,
- dane dotyczące liczby odsłon artykułów w poszczególne dni są również dostępne w tabeli pod wykresem i możliwe do pobrania w formacie _csv_.
  
WikiApp jest postawiona na darmowym hostingu (w związku z czym po pierwszym uruchomieniu po dłuższym czasie może chwilę się ładować) i dostępna pod adresem: https://visualizationtask4.onrender.com/
