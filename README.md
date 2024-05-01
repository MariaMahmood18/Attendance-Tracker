# ATTENDANCE TRACKER
### Video Demo: https://youtu.be/NY5G13Y-R2Q
### Description:
**Attendance Tracker** is a command-line python based project. It can be used by running the project.py file. It simplifies the process of recording, managing, and viewing student attendance. It allows teachers and administrators to efficiently track student attendance, reducing manual effort and paperwork.

The main features of this project are:
- Attendance Recording:
Teachers can mark student attendance for each class session, specifying whether the student is present, absent, or on a leave.
- View Attendance:                                                                               Only authorized personnel can view their attendance records for specific dates and classes.
- Security:                                                                                             User authentication and access control ensure that only authorized users can record and view attendance data.

This project consists of five .py files namely project.py, classes.py, student.py, validate_user.py, and test_project.py.

The **project.py** includes functions for user login, marking attendance, viewing attendance records, and adding new students. It reads and writes data from CSV files for student details and attendance records. The main function orchestrates these tasks based on user input after successful login authentication.

As the name suggests, in **student.py** and **classes.py** a class of student and a class of classes is implemented that includes methods to get and display information about students and classes.

The **validate_user.py** defines a hash_password function that takes a password as input, hashes it using the SHA-256 algorithm, and returns the resulting hash in hexadecimal format. This demonstrates the concept of hashing for password security, where even if two users have the same password, the stored hashes will be the same, ensuring that the actual passwords are not stored in plain text and are difficult to reverse-engineer.

Further the **test_project.py** file contains unit tests for validating the functions from the validate_user and project modules. It utilizes the unittest.mock library to simulate user input and compare expected outcomes, ensuring that the functions behave correctly. These tests are crucial for verifying the accuracy and reliability of the code within the validate_user and project modules.

Moreover it also has three .csv files namely **student_detail.csv** to store student related data, **attendance_detail.csv** to store student's attendance and **password_hashes.csv** to store the authorized person's username and hashed-password.

A text file named **requirements.txt** contains a list of all the external libraries used in the project

### Project Requirements:

&#9745; Your project must be implemented in Python.

&#9745; Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.

&#9745; Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.

&#9745; Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).

&#9745; Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).

&#9745; Implementing your project should entail more time and effort than is required by each of the course’s problem sets.

&#9745; Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.






