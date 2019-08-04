--List the following details of each employee: employee number,
	--last name, first name, gender, and salary.

SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees e
INNER JOIN salaries s ON (e.emp_no=s.emp_no);


--List employees who were hired in 1986.

SELECT * 
FROM employees
WHERE hire_date LIKE '1986-%';


--List the manager of each department with the following information:
	--department number, department name, the manager's employee number,
	--last name, first name, and start and end employment dates.

	--Based on the wording of the instructions, I wasn't sure if employment start and end dates
	--referred to their employment with the company or as a manager. I've chosed to intepret it
	--as their time as manager of the department. -KM

SELECT e.emp_no, e.last_name, e.first_name, dm.dept_no, d.dept_name, 
		dm.from_date, dm.to_date
FROM employees e
INNER JOIN dept_manager dm
	ON e.emp_no = dm.emp_no
INNER JOIN departments d
	ON d.dept_no = dm.dept_no;


--List the department of each employee with the following information:
	--employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
INNER JOIN dept_emp de
	ON e.emp_no = de.emp_no
INNER JOIN departments d
	ON d.dept_no = de.dept_no;

--List all employees whose first name is "Hercules" and last names begin with "B."

SELECT * 
FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

--List all employees in the Sales department, including their employee number,
	--last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
INNER JOIN dept_emp de
	ON e.emp_no = de.emp_no
INNER JOIN departments d
	ON d.dept_no = de.dept_no
WHERE d.dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their
	--employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
INNER JOIN dept_emp de
	ON e.emp_no = de.emp_no
INNER JOIN departments d
	ON d.dept_no = de.dept_no
WHERE d.dept_name IN ('Sales', 'Development');


--In descending order, list the frequency count of employee last names, 
	--i.e., how many employees share each last name.

SELECT last_name, COUNT(last_name) AS "Last Name Count"
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;

