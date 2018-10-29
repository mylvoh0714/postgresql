<h3>psql cheet sheet.. 개인저장용</h3>

1. 로컬접속 : psql -U [dbname]

2. 명령어
 - \dt : 관계테이블 list 보기

3. CSV 넣기
 - \copy course FROM [file-path] WITH CSV HEADER DELIMITER ',' ENCODING 'utf-8'
