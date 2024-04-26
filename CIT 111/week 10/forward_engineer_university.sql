-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema university_data
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema university_data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `university_data` DEFAULT CHARACTER SET utf8 ;
USE `university_data` ;

-- -----------------------------------------------------
-- Table `university_data`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`department` ;

CREATE TABLE IF NOT EXISTS `university_data`.`department` (
  `department_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `department_name` VARCHAR(45) NOT NULL,
  `department_college` VARCHAR(45) NOT NULL,
  `department_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`department_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`class`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`class` ;

CREATE TABLE IF NOT EXISTS `university_data`.`class` (
  `class_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `class_course_number` INT UNSIGNED NOT NULL,
  `department_id` INT UNSIGNED NOT NULL,
  `class_credits` INT UNSIGNED NOT NULL,
  `class_course_title` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`class_id`),
  INDEX `fk_class_department1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `fk_class_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `university_data`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`teacher`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`teacher` ;

CREATE TABLE IF NOT EXISTS `university_data`.`teacher` (
  `teacher_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `teacher_first_name` VARCHAR(45) NOT NULL,
  `teacher_last_name` VARCHAR(45) NOT NULL,
  `teacher_capacity` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`teacher_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`semester`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`semester` ;

CREATE TABLE IF NOT EXISTS `university_data`.`semester` (
  `semester_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `semester_year` INT NOT NULL,
  `semester_term` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`semester_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`Section`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`Section` ;

CREATE TABLE IF NOT EXISTS `university_data`.`Section` (
  `Section_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `class_id` INT UNSIGNED NOT NULL,
  `teacher_id` INT UNSIGNED NOT NULL,
  `semester_id` INT UNSIGNED NOT NULL,
  `Section_number` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Section_id`),
  INDEX `fk_Section_class1_idx` (`class_id` ASC) VISIBLE,
  INDEX `fk_Section_teacher1_idx` (`teacher_id` ASC) VISIBLE,
  INDEX `fk_Section_semester1_idx` (`semester_id` ASC) VISIBLE,
  CONSTRAINT `fk_Section_class1`
    FOREIGN KEY (`class_id`)
    REFERENCES `university_data`.`class` (`class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Section_teacher1`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `university_data`.`teacher` (`teacher_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Section_semester1`
    FOREIGN KEY (`semester_id`)
    REFERENCES `university_data`.`semester` (`semester_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`student` ;

CREATE TABLE IF NOT EXISTS `university_data`.`student` (
  `student_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `student_first_name` VARCHAR(45) NOT NULL,
  `student_last_name` VARCHAR(45) NOT NULL,
  `student_gender` VARCHAR(45) NOT NULL,
  `student_city` VARCHAR(45) NOT NULL,
  `student_state` VARCHAR(45) NOT NULL,
  `student_birthdate` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `university_data`.`enrollment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `university_data`.`enrollment` ;

CREATE TABLE IF NOT EXISTS `university_data`.`enrollment` (
  `student_id` INT UNSIGNED NOT NULL,
  `Section_id` INT UNSIGNED NOT NULL,
  `enrollment_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`student_id`, `Section_id`),
  INDEX `fk_student_Section_Section1_idx` (`Section_id` ASC) VISIBLE,
  INDEX `fk_student_Section_student_idx` (`student_id` ASC) VISIBLE,
  CONSTRAINT `fk_student_Section_student`
    FOREIGN KEY (`student_id`)
    REFERENCES `university_data`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_Section_Section1`
    FOREIGN KEY (`Section_id`)
    REFERENCES `university_data`.`Section` (`Section_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO department (department_college, department_name, department_code)
VALUES ('College of Physical Science and Engineering', 'Computer Information Technology', 'CIT');

INSERT INTO class (class_course_number, class_course_title, class_credits, department_id)
VALUES('111', 'Intro to Databases', 3, 1);


INSERT INTO department (department_college, department_name, department_code)
VALUES ('College of Physical Science and Engineering', 'Web Design and Development', 'WDD');

INSERT INTO class (class_course_number, class_course_title, class_credits, department_id)
VALUES ('130', 'Web Fundamentals', 2, 2);


INSERT INTO department (department_college, department_name, department_code)
VALUES ('College of Business and Communication', 'Economics', 'ECON');

INSERT INTO class (class_course_number, class_course_title, class_credits,department_id)
VALUES ('358', 'International Economics', 4, 3);

INSERT INTO department (department_college, department_name, department_code)
VALUES ('College of Language and Letters', 'Humanities and Philosophy', 'HUM');

INSERT INTO class (class_course_number, class_course_title, class_credits, department_id)
VALUES ('202', 'Search Meaning Modern World', 2,4);

-- SELECT *
-- FROM class;
-- SELECT *
-- FROM department;

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Marshall', 'Spence', 'M', 'Garland', 'TX', '2000-06-23');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Maria', 'Clark', 'F', 'Akron', 'OH', '2002-01-25');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Tracy', 'Woodward', 'F', 'Newark', 'NJ', '2002-10-04');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Erick', 'Woodward', 'M', 'Newark', 'NJ', '1998-08-05');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Lillie', 'Summers', 'F', 'Reno', 'NV', '1999-11-05');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Nellie', 'Marquez', 'F', 'Atlanta', 'GA', '2001-06-25');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Allen', 'Stokes', 'M', 'Bozeman', 'MT', '2004-09-16');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Josh', 'Rollins', 'M', 'Decatur', 'TN', '1998-11-28');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Janine', 'Bowers', 'F', 'Rexburg', 'ID', '2004-06-23');

INSERT INTO student (student_first_name, student_last_name, student_gender, student_city, student_state, student_birthdate)
VALUES ('Kerri', 'Shah', 'F', 'Mesa', 'AZ', '2003-04-05');

INSERT INTO semester (semester_year, semester_term)
VALUES (2024, 'Fall'); 

INSERT INTO semester (semester_year, semester_term)
VALUES (2025, 'Winter');

INSERT INTO teacher (teacher_first_name, teacher_last_name, teacher_capacity)
VALUES ('Charles', 'Stratford', 40);

INSERT INTO teacher (teacher_first_name, teacher_last_name, teacher_capacity)
VALUES ('Blaine', 'Robertson', 35);

INSERT INTO teacher (teacher_first_name, teacher_last_name, teacher_capacity)
VALUES ('James', 'Christensen', 30);

INSERT INTO teacher (teacher_first_name, teacher_last_name, teacher_capacity)
VALUES ('Alan', 'Walburger', 40);

-- SELECT *
-- FROM teacher;
-- SELECT *
-- FROM semester;
-- SELECT *
-- FROM class;

INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (1,2,1,1);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (2,3,1,1);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (2,3,1,2);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (3,4,1,1);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (4,1,1,1);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (1,2,2,2);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (1,2,2,3);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (2,3,2,1);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (2,3,2,2);
INSERT INTO section (class_id, teacher_id, semester_id, Section_number)
VALUES (4,1,2,1);



-- SELECT *
-- FROM section s
-- JOIN class c ON c.class_id = s.class_id;
-- SELECT *
-- FROM student;

INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(1,1,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(1,3,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(2,4,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(3,4,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(4,5,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(5,4,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(5,5,'TA');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(6,7,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(7,6,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(7,8,'TA');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(7,10,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(8,9,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(9,9,'Student');
INSERT INTO enrollment (student_id, Section_id, enrollment_type)
VALUES(10,6,'Student');

-- SELECT *
-- FROM enrollment;

-- USE university_data;

-- SELECT  s.student_first_name, c.class_course_title
-- FROM class c
-- JOIN section se ON c.class_id = se.class_id
-- JOIN enrollment e ON se.Section_id = e.Section_id
-- JOIN student s ON e.student_id = s.student_id
-- ORDER BY s.student_first_name;
