-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema film
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `film` ;

-- -----------------------------------------------------
-- Schema film
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `film` DEFAULT CHARACTER SET utf8 ;
USE `film` ;

-- -----------------------------------------------------
-- Table `film`.`year`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`year` ;

CREATE TABLE IF NOT EXISTS `film`.`year` (
  `year_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `year_released` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`year_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`studio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`studio` ;

CREATE TABLE IF NOT EXISTS `film`.`studio` (
  `studio_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `studio_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`studio_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`rating`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`rating` ;

CREATE TABLE IF NOT EXISTS `film`.`rating` (
  `rating_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `rating` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`rating_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`movie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`movie` ;

CREATE TABLE IF NOT EXISTS `film`.`movie` (
  `movie_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_tittle` VARCHAR(45) NOT NULL,
  `year_id` INT UNSIGNED NOT NULL,
  `studio_id` INT UNSIGNED NOT NULL,
  `rating_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`),
  INDEX `fk_movie_year1_idx` (`year_id` ASC) VISIBLE,
  INDEX `fk_movie_studio1_idx` (`studio_id` ASC) VISIBLE,
  INDEX `fk_movie_rating1_idx` (`rating_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_year1`
    FOREIGN KEY (`year_id`)
    REFERENCES `film`.`year` (`year_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_studio1`
    FOREIGN KEY (`studio_id`)
    REFERENCES `film`.`studio` (`studio_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_rating1`
    FOREIGN KEY (`rating_id`)
    REFERENCES `film`.`rating` (`rating_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`media_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`media_type` ;

CREATE TABLE IF NOT EXISTS `film`.`media_type` (
  `media_type_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `media_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`media_type_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`genre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`genre` ;

CREATE TABLE IF NOT EXISTS `film`.`genre` (
  `genre_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `genre_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`movie_genre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`movie_genre` ;

CREATE TABLE IF NOT EXISTS `film`.`movie_genre` (
  `movie_id` INT UNSIGNED NOT NULL,
  `genre_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `genre_id`),
  INDEX `fk_movie_genre_genre1_idx` (`genre_id` ASC) VISIBLE,
  INDEX `fk_movie_genre_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_genre_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_genre_genre1`
    FOREIGN KEY (`genre_id`)
    REFERENCES `film`.`genre` (`genre_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`actors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`actors` ;

CREATE TABLE IF NOT EXISTS `film`.`actors` (
  `actors_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `actor_first_name` VARCHAR(45) NOT NULL,
  `actor_last_name` VARCHAR(45) NULL,
  PRIMARY KEY (`actors_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`movie_actors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`movie_actors` ;

CREATE TABLE IF NOT EXISTS `film`.`movie_actors` (
  `movie_id` INT UNSIGNED NOT NULL,
  `actors_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `actors_id`),
  INDEX `fk_movie_actors_actors1_idx` (`actors_id` ASC) VISIBLE,
  INDEX `fk_movie_actors_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_actors_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_actors_actors1`
    FOREIGN KEY (`actors_id`)
    REFERENCES `film`.`actors` (`actors_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`special_feature`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`special_feature` ;

CREATE TABLE IF NOT EXISTS `film`.`special_feature` (
  `special_feature_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `special_feature_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`special_feature_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`movie_special_feature`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`movie_special_feature` ;

CREATE TABLE IF NOT EXISTS `film`.`movie_special_feature` (
  `movie_id` INT UNSIGNED NOT NULL,
  `special_feature_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `special_feature_id`),
  INDEX `fk_movie_special_feature_special_feature1_idx` (`special_feature_id` ASC) VISIBLE,
  INDEX `fk_movie_special_feature_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_special_feature_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_special_feature_special_feature1`
    FOREIGN KEY (`special_feature_id`)
    REFERENCES `film`.`special_feature` (`special_feature_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`price`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`price` ;

CREATE TABLE IF NOT EXISTS `film`.`price` (
  `price_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `price` DECIMAL(5,2) UNSIGNED NOT NULL,
  PRIMARY KEY (`price_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `film`.`movie_media_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `film`.`movie_media_type` ;

CREATE TABLE IF NOT EXISTS `film`.`movie_media_type` (
  `movie_id` INT UNSIGNED NOT NULL,
  `media_type_id` INT UNSIGNED NOT NULL,
  `price_id` INT UNSIGNED NULL,
  PRIMARY KEY (`movie_id`, `media_type_id`),
  INDEX `fk_movie_media_type_media_type1_idx` (`media_type_id` ASC) VISIBLE,
  INDEX `fk_movie_media_type_movie1_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_movie_media_type_price1_idx` (`price_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_media_type_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_media_type_media_type1`
    FOREIGN KEY (`media_type_id`)
    REFERENCES `film`.`media_type` (`media_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_media_type_price1`
    FOREIGN KEY (`price_id`)
    REFERENCES `film`.`price` (`price_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

USE film;

INSERT INTO genre (genre_name)
VALUES ('family'),
	('animated'),
    ('musical'),
    ('romance'),
    ('sci fi'),
    ('comedy'),
    ('drama'),
    ('music'),
    ('action'),
    ('adventure');

Select * FROM genre;

INSERT INTO actors (actor_first_name, actor_last_name)
VALUES ('Tom','Hanks'),
	('Tim','Allen'),
	('Annie','Potts'),
	('John','Ratzenburger'),
	('Gene','Kelly'),
	('Cyd','Charisse'),
	('Van','Johnson'),
	('Harrison','Ford'),
	('Carrie','Fisher'),
	('Mark','Hamill'),
	('Emilia','Jones'),
	('Marlee','Matlin'),
	('Troy','Kotsur'),
	('Timothee','Chalamet'),
	('Rebecca','Ferguson'),
	('Zendaya',NULL),
	('Oscar','Isaac'),
	('Jason','Momoa');
    
SELECT * FROM actors;

INSERT INTO special_feature (special_feature_name)
VALUES ('bloopers'),
	('actor interviews'),
	('cut scenes'),
	('trailers'),
	('deleted scenes'),
    ('special effects');

SELECT * FROM special_feature;

INSERT INTO rating (rating)
VALUES ('G'),
	('PG'),
	('PG-13');

SELECT * FROM rating;

INSERT INTO media_type (media_type)
VALUES ('DVD'),
	('blu-ray'),
    ('Streaming'),
    ('4K');

SELECT * FROM media_type;
    
INSERT INTO price (price)
VALUES (19.95),
(24.95),
(35.00);
SELECT * FROM price;

INSERT INTO year (year_released)
VALUES (1995),
(1999),
(1954),
(1977),
(2021);

SELECT * FROM year;

INSERT INTO studio (studio_name)
VALUES ('Pixar'),
	(+'MGM'),
	('20th Century Fox'),
	('Apple TV+'),
	('Warner Bros');
SELECT * FROM studio;

INSERT INTO movie (movie_tittle, year_id, studio_id, rating_id)
VALUES ('Toy Story', 1 , 1, 1),
('Toy Story 2', 2, 1, 1),
('Brigadoone', 3, 2, 1),
('The Empire Strikes Back', 4, 3, 2),
('Coda', 5, 4, 3),
('Dune', 5, 5, 3);
SELECT * FROM movie;

INSERT INTO movie_genre(movie_id, genre_id)
VALUES (1, 1),
(1,2),
(2,1),
(2,2),
(3,3),
(3,4),
(4, 5),
(5, 6),
(5,7),
(5, 8),
(6, 9),
(6,10),
(6,7);
SELECT * FROM movie_genre;

INSERT INTO movie_actors(movie_id, actors_id)
VALUES (1,1),
(1,2),
(1,3),
(1,4),
(2,1),
(2,2),
(2,3),
(2,4),
(3,5),
(3,6),
(3,7),
(4,8),
(4,9),
(4,10),
(5,11),
(5,12),
(5,13),
(6,14),
(6,15),
(6,16),
(6,17),
(6,18);

SELECT * FROM movie_actors;

INSERT INTO movie_special_feature(movie_id, special_feature_id)
VALUES(1,1),
(2,2),
(4,3),
(4,1),
(5,4),
(6,4),
(6,5),
(6,6);
SELECT * FROM movie_special_feature;

INSERT INTO movie_media_type(movie_id, media_type_id, price_id)
VALUES(1,1,1),
(2,1,2),
(3,1,1),
(4,2,3),
(5,3,NULL),
(6,4,2),
(6,2,1);
SELECT * FROM movie_media_type;



