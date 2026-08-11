# Experiment 05: Viva Voce Examination Questions & Answers

---

### Q1: What is SQL Injection (SQLi)?
**Answer:** SQL Injection is a web vulnerability where untrusted user input is directly concatenated into dynamic SQL database queries without sanitization or parameterization, enabling an attacker to manipulate query syntax and execute arbitrary SQL commands.

---

### Q2: How do Parameterized Queries (Prepared Statements) prevent SQL Injection?
**Answer:** Parameterized queries send the SQL template structure to the database engine first, compiling the query execution plan separately from parameters. When user input parameters are subsequently bound, the database engine treats them strictly as literal data values rather than executable SQL syntax commands, rendering injection impossible.

---

### Q3: What is the purpose of the `UNION` operator in SQLi exploitation?
**Answer:** The `UNION` operator allows an attacker to combine the results of the original query with a secondary arbitrary `SELECT` query, enabling the extraction of unauthorized data from other database tables (e.g., retrieving password hashes from a `users` table).

---

### Q4: Explain the difference between Error-Based SQLi and Blind SQLi.
**Answer:** Error-Based SQLi relies on detailed database error messages returned directly on screen to leak database schema details. Blind SQLi occurs when the application suppresses database errors; the attacker must infer data by observing boolean true/false application responses (Boolean-Blind) or measuring execution delays caused by sleep functions (Time-Blind).

---

### Q5: Why is input sanitization (escaping characters) insufficient as a primary defense against SQLi?
**Answer:** Escaping algorithms are prone to implementation flaws, character encoding bypasses (such as multi-byte UTF-8 tricks), and missing context edge-cases (such as numeric fields where quotes are not required). Prepared statements provide structural separation at the database driver level.

---

### Q6: How does an attacker determine the number of columns in a SELECT query during UNION SQLi?
**Answer:** By systematically injecting `ORDER BY N` payloads (e.g., `ORDER BY 1`, `ORDER BY 2`) until a database error occurs (e.g., `Unknown column 'N'`), indicating the target query selects `N-1` columns.

---

### Q7: What is the Principle of Least Privilege in database security?
**Answer:** Principle of Least Privilege dictates that the web application's database user account should only possess the minimum permissions required for operation (e.g., `SELECT`, `INSERT`, `UPDATE` on specific application tables) and should never connect as `db_owner`, `root`, or `sa`.

---

### Q8: What role do comments play in SQL Injection payloads (e.g., `-- -` or `/*`)?
**Answer:** SQL comment indicators instruct the database engine to truncate and ignore the remainder of the original developer's SQL query string following the injected payload.

---

### Q9: Can Stored Procedures prevent SQL Injection?
**Answer:** Yes, if the stored procedure uses parameterized inputs internally. However, if a stored procedure dynamically concatenates input strings internally (e.g., `EXECUTE IMMEDIATE sql_str`), it remains vulnerable to SQL injection.

---

### Q10: How can Object-Relational Mapping (ORM) frameworks help mitigate SQL Injection?
**Answer:** Modern ORMs (such as SQLAlchemy, Hibernate, or Django ORM) automatically construct parameterized SQL queries under the hood when using standard API methods, preventing raw string concatenation vulnerabilities.
