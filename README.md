Python for Everybody Specialization

University of Michigan · Coursera

A structured repository documenting my completion of the Python for Everybody Specialization, developed by the University of Michigan and offered through Coursera.

This repository preserves the progression of the specialization from foundational Python programming through data structures, web data, databases, and the Capstone. It brings together selected programming exercises, graded work, source code, databases, datasets, generated outputs, visualization artifacts, and project work developed throughout the coursework.

The overall progression is:

Python Programming → Data Structures → Web Data → Databases → Capstone

---

About the Specialization

The Python for Everybody Specialization provides a progressive introduction to programming and practical data handling with Python.

The coursework moves from fundamental programming concepts into increasingly practical applications involving files, structured data, web retrieval, networks, APIs, SQL, relational databases, data modeling, algorithms, and visualization.

This repository is organized as a technical record of that progression. Rather than treating each course as an isolated collection of exercises, the repository preserves how the concepts build toward larger data-processing and analysis workflows.

---

Courses Included

1. Programming for Everybody (Getting Started with Python)

The foundation of the specialization, covering the essential concepts required to write, understand, execute, and debug Python programs.

Key areas include:

- Programming concepts and computational thinking
- Variables, expressions, and data types
- Conditional execution
- Functions
- Loops and iteration
- Program execution and debugging
- Basic problem solving with Python

The course establishes the programming foundation used throughout the remaining courses.

---

2. Python Data Structures

Builds upon Python fundamentals by introducing practical structures and techniques for processing collections of information.

Key areas include:

- Strings
- Files and file processing
- Lists
- Dictionaries
- Tuples
- Sorting and counting
- Searching and retrieving information
- Processing real-world text data

The repository retains the modules and coursework artifacts represented in the final project structure. Certain course modules consist of optional, non-graded learning activities that do not produce repository artifacts and therefore are not represented as physical folders.

---

3. Using Python to Access Web Data

Extends Python into web-based data retrieval and processing.

Key areas include:

- Regular expressions
- Networks and sockets
- HTTP request-response concepts
- Retrieving data from the web
- HTML parsing with BeautifulSoup
- XML
- JSON
- REST APIs
- Geo-location API usage

The course demonstrates how Python can move beyond local files and work with information available through networked sources and web services.

---

4. Using Databases with Python

Introduces persistent data storage and relational database concepts using Python and SQLite.

Key areas include:

- Object-oriented programming concepts
- SQL
- SQLite
- CRUD operations
- Relational data models
- Multi-table databases
- Many-to-many relationships
- Database-backed Python applications
- Database-driven visualization

The coursework progresses from basic SQL operations toward relational schemas and practical Python applications that interact with databases.

---

5. Capstone - Retrieving, Processing, and Visualizing Data with Python

Brings together concepts from across the specialization through larger practical workflows.

The Capstone work includes:

- Web spidering
- PageRank
- Email retrieval and modeling
- Data aggregation
- Data visualization
- External data-source analysis
- End-to-end data-processing workflows

The Capstone provides the strongest connection between the individual programming concepts learned throughout the specialization and complete data-oriented workflows.

---

Skills Covered

Python Programming

- Python fundamentals
- Variables and expressions
- Data types
- Conditional logic
- Functions
- Loops and iteration
- File processing
- Python data structures
- Object-oriented programming concepts

Web & Network Programming

- HTTP
- TCP/IP sockets
- URL retrieval
- Web scraping
- HTML parsing
- XML parsing
- JSON processing
- REST APIs
- Web services

Databases & SQL

- SQLite
- SQL queries
- CRUD operations
- Relational database design
- Primary and foreign-key relationships
- Many-to-many relationships
- Database-backed data processing

Data Processing & Analysis

- Text processing
- Regular expressions
- Data extraction
- File-based data processing
- Data cleaning and preprocessing
- Aggregation
- Exploratory analysis
- Structured data workflows

Algorithms & Data Workflows

- PageRank
- Web crawling
- Link analysis
- Data modeling
- Ranking
- Aggregation
- Multi-stage processing pipelines

Visualization

- D3.js
- JavaScript-based visualization workflows
- HTML-based visualizations
- Geographic visualization
- Timeline visualization
- Word clouds
- Exploratory data visualizations

---

Tools & Technologies

Programming & Development

- Python
- JavaScript
- VS Code

Python Libraries & Modules

- "sqlite3"
- "urllib"
- "BeautifulSoup"
- "re"
- "json"
- "xml.etree.ElementTree"
- "socket"
- "ssl"
- "zlib"
- "datetime"
- "pandas"
- "NumPy"
- "Matplotlib"
- "Seaborn"

Databases & Data Formats

- SQLite
- CSV
- TSV
- JSON
- XML
- HTML

Visualization

- D3.js
- D3 Cloud Layout
- JavaScript-generated visualization data
- HTML-based visualizations

Course-provided and third-party resources are distinguished from original implementation work where relevant.

Development environment: VS Code was the primary development environment used throughout the specialization. Jupyter notebooks were used specifically for the OpenFoodFacts Capstone project.

---

Highlighted Practical Work

PageRank & Web Spidering

The Capstone PageRank work combines web crawling, HTML parsing, SQLite storage, link analysis, ranking, JavaScript data generation, and visualization.

The overall workflow can be represented as:

Retrieve → Parse → Store → Rank → Export → Visualize

Key components include:

- Web page retrieval
- HTML parsing with BeautifulSoup
- URL resolution and link processing
- SQLite-backed page and link storage
- PageRank calculation
- Rank generation and export
- JavaScript-based visualization
- Custom visualization outputs

The implementation demonstrates how raw web pages can be transformed into structured graph data and subsequently processed using a ranking algorithm.

---

GMANE Email Retrieval & Modeling

The Capstone email-processing work demonstrates a multi-stage workflow for retrieving, parsing, storing, modeling, and aggregating email data.

The workflow can be represented as:

Retrieve → Parse → Store → Model → Aggregate

The implementation includes:

- Email retrieval
- Header and date parsing
- SQLite storage
- Sender and subject modeling
- Message relationships
- Data normalization
- Compressed content storage
- Frequency aggregation

This work demonstrates the transition from raw retrieved data to a structured relational representation suitable for further analysis.

---

Email Data Visualization

The Capstone visualization work builds upon the processed email data and transforms aggregated information into visual representations.

The workflow can be represented as:

Aggregate → Transform → Generate Visualization Data → Visualize

Artifacts include:

- Word clouds
- Monthly timelines
- Yearly timelines
- Organization-based aggregation
- D3.js-based visualizations
- JavaScript visualization data

Together, these artifacts demonstrate how processed data can be transformed into interpretable visual outputs.

---

OpenFoodFacts Capstone Project

The OpenFoodFacts analysis forms the external data-source analysis component of the Capstone and is also maintained as a separate standalone project repository.

The project follows a complete data-analysis workflow:

Data Source Selection → Data Cleaning & Preprocessing → Exploratory Data Analysis → Visualization & Insights → Conclusion

Dataset Scale

The original OpenFoodFacts dataset contained:

- 356,027 products
- 163 columns

After preprocessing:

- 356,027 products
- 64 columns

The preprocessing stage removed columns with more than 90% missing values while retaining all records. "potassium_100g" was explicitly retained, and the final processed dataset contained no duplicate records.

Analysis

The analysis examines nutritional information across countries, brands, food categories, and PNNS food groups.

The workflow includes:

- Dataset inspection
- Data cleaning and preprocessing
- Exploratory data analysis
- Nutrition-related feature analysis
- Country representation
- Brand representation
- Nutrition-grade distribution
- Food-category comparisons
- PNNS food-group comparisons
- Nutritional relationship analysis

The visualization stage produces four principal figures covering nutritional profiles, category-level comparisons, country-level nutrition scores, and key nutritional relationships.

The relationship analysis uses a sample of 5,000 complete observations with "random_state=42".

The standalone project maintains its own structured organization for data, notebooks, outputs, dependencies, and documentation, while the relevant Capstone artifacts are preserved within this specialization repository.

---

Datasets & Data Sources

The coursework works with multiple forms of structured and semi-structured data, including:

- Text files
- CSV files
- TSV files
- JSON data
- XML data
- HTML documents
- SQLite databases
- Web API responses
- Email datasets
- OpenFoodFacts product data

Examples represented in the repository include:

- "mbox-short.txt"
- "mbox.txt"
- "words.txt"
- "romeo.txt"
- "tracks.csv"
- "roster_data.json"
- "where.data"
- SQLite databases created and processed throughout the coursework
- OpenFoodFacts product data used for the Capstone analysis

Large datasets and generated artifacts may be retained locally or represented through derived outputs where appropriate; their presence or absence from a remote Git repository should not be interpreted as a statement about whether the underlying coursework was completed.

---

Repository Structure

Python for Everybody Specialization
│
├── LICENSE
│
├── Capstone - Retrieving, Processing, and Visualizing Data with Python
│   ├── Module 1 - Welcome to the Capstone
│   │   └── Python for Everybody - A Review
│   │       └── python_for_everybody_a_review.pdf
│   │
│   ├── Module 2 - Building a Search Engine
│   │   └── Peer Grade – Page Rank
│   │       ├── d3.v2.js
│   │       ├── force.css
│   │       ├── force.html
│   │       ├── force.js
│   │       ├── force_custom.html
│   │       ├── force_custom.js
│   │       ├── force_drchuck.html
│   │       ├── force_drchuck.js
│   │       ├── LICENSE
│   │       ├── pagerank_custom_database_output.png
│   │       ├── pagerank_custom_visualization.png
│   │       ├── pagerank_drchuck_database_output.png
│   │       ├── pagerank_drchuck_visualization.png
│   │       ├── spdump.py
│   │       ├── spider.js
│   │       ├── spider.py
│   │       ├── spider_custom.js
│   │       ├── spider_custom.sqlite
│   │       ├── spider_drchuck.js
│   │       ├── spider_drchuck.sqlite
│   │       ├── spjson.py
│   │       ├── sprank.py
│   │       ├── spreset.py
│   │       └── bs4
│   │           ├── dammit.py
│   │           ├── dammit.py.bak
│   │           ├── diagnose.py
│   │           ├── diagnose.py.bak
│   │           ├── element.py
│   │           ├── element.py.bak
│   │           ├── testing.py
│   │           ├── testing.py.bak
│   │           ├── __init__.py
│   │           ├── __init__.py.bak
│   │           └── builder
│   │               ├── _html5lib.py
│   │               ├── _html5lib.py.bak
│   │               ├── _htmlparser.py
│   │               ├── _htmlparser.py.bak
│   │               ├── _lxml.py
│   │               ├── _lxml.py.bak
│   │               ├── __init__.py
│   │               └── __init__.py.bak
│   │
│   ├── Module 3 - Exploring Data Sources (Project)
│   │   └── Identifying a Data Source
│   │       ├── 01_dataset_selection_and_inspection.ipynb
│   │       └── Discussion Prompt
│   │           └── identifying_a_data_source.txt
│   │
│   ├── Module 4 - Spidering and Modeling Email Data
│   │   └── Loading and Modeling Mail Data
│   │       ├── content_350.sqlite
│   │       ├── content_sqlite.png
│   │       ├── gbasic.py
│   │       ├── gbasic_24_output.png
│   │       ├── gmane.py
│   │       ├── gmodel.py
│   │       ├── gmodel_output.png
│   │       ├── index_350.sqlite
│   │       ├── index_sqlite.png
│   │       └── mapping.sqlite
│   │
│   ├── Module 5 - Accessing New Data Sources (Project)
│   │   └── Analyzing a Data Source
│   │       ├── 02_data_cleaning_and_preprocessing.ipynb
│   │       ├── 03_exploratory_data_analysis.ipynb
│   │       └── Discussion Prompt
│   │           └── analyzing_a_data_source.txt
│   │
│   ├── Module 6 - Visualizing Email Data
│   │   └── Visualizing Email Data
│   │       ├── d3.layout.cloud.js
│   │       ├── d3.v2.js
│   │       ├── gbasic_350_output.png
│   │       ├── gline.htm
│   │       ├── gline.py
│   │       ├── gline_350_monthly.htm
│   │       ├── gline_350_monthly.js
│   │       ├── gline_350_yearly.htm
│   │       ├── gline_350_yearly.js
│   │       ├── gword.htm
│   │       ├── gword.py
│   │       ├── gword_350.htm
│   │       ├── gword_350.js
│   │       ├── gyear.py
│   │       ├── gyear_350.py
│   │       ├── timeline_monthly.png
│   │       ├── timeline_yearly.png
│   │       └── word_cloud.png
│   │
│   └── Module 7 - Visualizing new Data Sources (Project)
│       └── Data Analysis and Visualization
│           ├── 04_data_visualization_and_insights.ipynb
│           ├── 05_project_conclusion.ipynb
│           ├── average_nutrition_score_across_major_countries.png
│           ├── key_nutritional_relationships.png
│           ├── nutritional_profiles_across_major_food_categories.png
│           ├── nutritional_profiles_across_pnns_food_groups.png
│           └── Discussion Prompt
│               └── data_analysis_and_visualization.txt
│
├── Certificates
│   ├── Capstone – Retrieving, Processing, and Visualizing Data with Python.pdf
│   ├── Programming for Everybody (Getting Started with Python).pdf
│   ├── Python Data Structures.pdf
│   ├── Python for Everybody Specialization.pdf
│   ├── Using Databases with Python.pdf
│   └── Using Python to Access Web Data.pdf
│
├── Programming for Everybody (Getting Started with Python)
│   ├── Module 1 - Chapter One – Why We Program
│   │   └── Programming Concepts Check-In
│   │       └── programming_concepts_check_in.pdf
│   ├── Module 2 - Installing Python
│   │   └── Installing Python
│   │       └── installing_python.pdf
│   ├── Module 3 - Chapter One – Why We Program (continued)
│   │   ├── Quiz – Chapter 1
│   │   │   └── quiz_chapter_1.pdf
│   │   └── Write Hello World
│   │       └── write_hello_world.pdf
│   ├── Module 4 - Chapter Two – Variables and Expressions
│   │   ├── Expressions Check-In
│   │   │   └── expressions_check_in.pdf
│   │   ├── Pay Calculator
│   │   │   └── pay_calculator.pdf
│   │   ├── Quiz – Chapter 2
│   │   │   └── quiz_chapter_2.pdf
│   │   └── Welcome Message
│   │       └── welcome_message.pdf
│   ├── Module 5 - Chapter Three – Conditional Code
│   │   ├── Overtime Pay Calculator
│   │   │   └── overtime_pay_calculator.pdf
│   │   ├── Quiz – Chapter 3
│   │   │   └── quiz_chapter_3.pdf
│   │   └── Write Conditional Statements
│   │       └── write_conditional_statements.pdf
│   ├── Module 6 - Chapter Four – Functions
│   │   ├── Build Functions
│   │   │   └── build_functions.pdf
│   │   └── Quiz – Chapter 4
│   │       └── quiz_chapter_4.pdf
│   └── Module 7 - Chapter Five – Loops and Iteration
│       ├── Find the Largest and Smallest Numbers
│       │   └── find_the_largest_and_smallest_numbers.pdf
│       ├── Loops and Iterations Check-In
│       │   └── loops_and_iterations_check_in.pdf
│       └── Quiz – Chapter 5
│           └── quiz_chapter_5.pdf
│
├── Python Data Structures
│   ├── Module 1 - Chapter Six – Strings
│   │   ├── Parse Text Strings
│   │   │   └── parse_text_strings.pdf
│   │   └── Quiz – Chapter 6
│   │       ├── quiz_chapter_6_answers.pdf
│   │       └── quiz_chapter_6_grade.pdf
│   ├── Module 3 - Chapter Seven – Files
│   │   ├── Quiz – Chapter 7
│   │   │   ├── quiz_chapter_7_answers.pdf
│   │   │   └── quiz_chapter_7_grade.pdf
│   │   ├── Read a File and Convert Its Text
│   │   │   ├── read_a_file_and_convert_its_text.pdf
│   │   │   └── words.txt
│   │   └── Read a File and Process its Data
│   │       ├── mbox-short.txt
│   │       └── read_a_file_and_process_its_data.pdf
│   ├── Module 4 - Chapter Eight – Lists
│   │   ├── Build a List of Senders
│   │   │   ├── build_a_list_of_senders.pdf
│   │   │   └── mbox-short.txt
│   │   ├── Create a Sorted Word List
│   │   │   ├── create_a_sorted_word_list.pdf
│   │   │   └── romeo.txt
│   │   └── Quiz – Chapter 8
│   │       ├── quiz_chapter_8_answers.pdf
│   │       └── quiz_chapter_8_grade.pdf
│   ├── Module 5 - Chapter Nine – Dictionaries
│   │   ├── Find the Most Frequent Sender
│   │   │   ├── find_the_most_frequent_sender.pdf
│   │   │   └── mbox-short.txt
│   │   └── Quiz – Chapter 9
│   │       ├── quiz_chapter_9_answers.pdf
│   │       └── quiz_chapter_9_grade.pdf
│   └── Module 6 - Chapter Ten – Tuples
│       ├── Quiz – Chapter 10
│       │   ├── quiz_chapter_10_answers.pdf
│       │   └── quiz_chapter_10_grade.pdf
│       └── Sort and Count Messages
│           └── sort_and_count_messages.pdf
│
├── Using Databases with Python
│   ├── Module 1 - Chapter Fourteen – Object Oriented Python
│   │   ├── Object Oriented Programming
│   │   │   ├── object_oriented_programming_answers.pdf
│   │   │   └── object_oriented_programming_grade.pdf
│   │   └── Using Encoded Data in Python 3
│   │       ├── using_encoded_data_in_python_3_answers.pdf
│   │       └── using_encoded_data_in_python_3_grade.pdf
│   ├── Module 2 - Chapter Fifteen – Basic Structured Query Language
│   │   ├── Counting Email in a Database
│   │   │   ├── counting_email_in_database.py
│   │   │   ├── mbox.txt
│   │   │   ├── organization_counts.sqlite
│   │   │   └── queries.sql
│   │   ├── Our First Database
│   │   │   ├── our_first_database.sqlite
│   │   │   └── queries.sql
│   │   └── Single-Table SQL
│   │       ├── single_table_sql_answers.pdf
│   │       └── single_table_sql_grade.pdf
│   ├── Module 3 - Chapter Fifteen – Data Models and Relational SQL
│   │   ├── Multi-Table Database - Tracks
│   │   │   ├── queries.sql
│   │   │   ├── trackdb.sqlite
│   │   │   ├── tracks.csv
│   │   │   ├── tracks.py
│   │   │   └── tracks_database.py
│   │   └── Multi-Table Relational SQL
│   │       ├── multi_table_relational_sql_answers.pdf
│   │       └── multi_table_relational_sql_grade.pdf
│   ├── Module 4 - Chapter Fifteen – Many-to-Many Relationships in SQL
│   │   ├── Many Students in Many Courses
│   │   │   ├── queries.sql
│   │   │   ├── roster.py
│   │   │   ├── rosterdb.sqlite
│   │   │   └── roster_data.json
│   │   └── Many-to-Many Relationships and Python
│   │       ├── many_to_many_relationships_and_python_answers.pdf
│   │       └── many_to_many_relationships_and_python_grade.pdf
│   └── Module 5 - Chapter Sixteen – Databases and Visualization
│       └── Databases and Visualization (peer-graded)
│           ├── geodump.py
│           ├── geodump_output.png
│           ├── geoload.py
│           ├── geoload_output.png
│           ├── opengeo.sqlite
│           ├── queries.sql
│           ├── where.data
│           ├── where.html
│           ├── where.js
│           └── where_map.png
│
└── Using Python to Access Web Data
    ├── Module 1 - Getting Started
    │   └── Peer Review – Installing and Running Python Screen Shots
    │       ├── peer_review_grade.pdf
    │       ├── program_execution_in_command_line.png
    │       └── program_in_text_editor.png
    ├── Module 2 - Chapter Eleven – Regular Expressions
    │   ├── Extracting Data With Regular Expressions
    │   │   ├── finding_numbers_in_a_haystack.py
    │   │   └── regex_sum_2334048.txt
    │   └── Regular Expressions
    │       ├── regular_expressions_answers.pdf
    │       └── regular_expressions_grade.pdf
    ├── Module 3 - Chapter Twelve – Networks and Sockets
    │   ├── Networks and Sockets
    │   │   ├── networks_and_sockets_answers.pdf
    │   │   └── networks_and_sockets_grade.pdf
    │   └── Understanding the Request – Response Cycle
    │       └── exploring_the_hypertext_transport_protocol.py
    ├── Module 4 - Chapter Twelve – Programs that Surf the Web
    │   ├── Following Links in HTML Using BeautifulSoup
    │   │   └── following_links_in_python.py
    │   ├── Reading Web Data From Python
    │   │   ├── reading_web_data_from_python_answers.pdf
    │   │   └── reading_web_data_from_python_grade.pdf
    │   └── Scraping HTML Data with BeautifulSoup
    │       └── scraping_numbers_from_html_using_beautifulsoup.py
    ├── Module 5 - Chapter Thirteen – Web Services and XML
    │   ├── eXtensible Markup Language
    │   │   ├── extensible_markup_language_answers.pdf
    │   │   └── extensible_markup_language_grade.pdf
    │   └── Extracting Data from XML
    │       └── extracting_data_from_xml.py
    └── Module 6 - Chapter Thirteen – JSON and the REST Architecture
        ├── Extracting Data from JSON
        │   └── extracting_data_from_json.py
        ├── REST, JSON, and APIs
        │   ├── rest_json_and_apis_answers.pdf
        │   └── rest_json_and_apis_grade.pdf
        └── Using a Geo Location API
            └── calling_a_json_api.py

---

Certificates

Course| Verification
Programming for Everybody (Getting Started with Python)| https://coursera.org/verify/32PVA1AH4GQO
Python Data Structures| https://coursera.org/verify/Z5NI6GFEKH5K
Using Python to Access Web Data| https://coursera.org/verify/QMCFPJL8O5TE
Using Databases with Python| https://coursera.org/verify/BTBESDPGAK5M
Capstone - Retrieving, Processing, and Visualizing Data with Python| https://coursera.org/verify/KKU2ZQE4QAKO
Python for Everybody Specialization| https://coursera.org/verify/specialization/0FJIV7OWCILU

---

Repository Philosophy

This repository is organized to show a progression from fundamental programming concepts toward practical data workflows.

Programming Fundamentals
        │
        ▼
Python Data Structures & File Processing
        │
        ▼
Web Retrieval, Parsing & APIs
        │
        ▼
SQL, SQLite & Relational Data
        │
        ▼
Capstone Data Workflows
        │
        ├── PageRank & Web Spidering
        │
        ├── Email Retrieval & Modeling
        │
        ├── Email Visualization
        │
        └── OpenFoodFacts Data Analysis

The emphasis is not only on completing individual exercises, but on preserving how programming concepts develop into increasingly complete data-processing workflows.

Across the specialization, the work moves from writing small Python programs to handling files, retrieving information from the web, interacting with APIs, storing structured information in databases, modeling relationships, implementing algorithms, and producing analytical visualizations.

The resulting repository therefore represents both a learning progression and a practical record of applying Python to increasingly structured data problems.

---

Notes

- This repository follows the five-course structure of the Python for Everybody Specialization.
- Coursework artifacts are organized according to their corresponding course, module, activity, and project context.
- Optional and non-graded course activities that do not produce retained repository artifacts are not represented as physical folders.
- The repository prioritizes meaningful coursework artifacts, source code, graded work, project work, datasets, databases, and generated outputs.
- Course-provided and third-party resources are distinguished from original implementation work where relevant.
- The OpenFoodFacts analysis is part of the Capstone work and is additionally maintained as a standalone project repository.
- Some source files may contain environment-specific paths or configuration details from the original development environment.
- Large datasets and generated artifacts may be retained locally or represented through derived outputs where appropriate.

---

Disclaimer

This repository is maintained for educational, academic, portfolio, and personal learning purposes.

The Python for Everybody Specialization, its course materials, course-provided resources, and third-party libraries, frameworks, datasets, or other resources remain the property of their respective owners.

The repository documents original programming implementations, project work, analysis, generated outputs, and repository organization maintained by the author as a record of the learning process.

No ownership claim is made over course materials, third-party libraries, frameworks, datasets, or other resources that are not original works of the author.