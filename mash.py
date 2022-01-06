  SELECT emloyee_id,first_name FROM personal_information
  lEFT JOIN salary
  ON personal_information.emloyee_id=salary.emlpoyee_id
UNION
  SELECT emlpoyee_id, basic_salary FROM salary
  RIGHT JOIN personal_information
  ON personal_information.emloyee_id=salary.emlpoyee_id
	 