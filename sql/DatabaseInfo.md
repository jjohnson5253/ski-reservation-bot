Database consists of one table, `datestoreserve`.

Table creation statement:

```
CREATE TABLE `datestoreserve` (
 `month` int(11) NOT NULL,
 `day` int(11) NOT NULL,
 `year` int(11) NOT NULL,
 `mountains` varchar(255) NOT NULL,
 `emails` varchar(255) NOT NULL
)
```

The columns `month`, `day`, and `year` combine to form a specific date that the script should reserve. Values in the columns `mountains` and `emails` filter the script so that it will only reserve a specific date for mountains present in the `mountains` column and emails present in the `email` column. The `mountains` and `emails` columns should be formatted as a comma delimited string. For example, a valid value for `mountains` is "Brighton, Arapahoe Basin".
