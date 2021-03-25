SELECT country, last_name, MAX(balance) FROM users_user GROUP BY country, last_name;

-- country X last_name 조합 경우를 전부 계산 => aggregate()

