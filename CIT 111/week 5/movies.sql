-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`year`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`year` ;

CREATE TABLE IF NOT EXISTS `mydb`.`year` (
  `year_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `year_released` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`year_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`studio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`studio` ;

CREATE TABLE IF NOT EXISTS `mydb`.`studio` (
  `studio_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `studio_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`studio_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`rating`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`rating` ;

CREATE TABLE IF NOT EXISTS `mydb`.`rating` (
  `rating_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `rating` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`rating_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movie`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`movie` ;

CREATE TABLE IF NOT EXISTS `mydb`.`movie` (
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
    REFERENCES `mydb`.`year` (`year_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_studio1`
    FOREIGN KEY (`studio_id`)
    REFERENCES `mydb`.`studio` (`studio_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_rating1`
    FOREIGN KEY (`rating_id`)
    REFERENCES `mydb`.`rating` (`rating_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`media_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`media_type` ;

CREATE TABLE IF NOT EXISTS `mydb`.`media_type` (
  `media_type_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `media_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`media_type_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`genre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`genre` ;

CREATE TABLE IF NOT EXISTS `mydb`.`genre` (
  `genre_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `genre_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movie_genre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`movie_genre` ;

CREATE TABLE IF NOT EXISTS `mydb`.`movie_genre` (
  `movie_id` INT UNSIGNED NOT NULL,
  `genre_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `genre_id`),
  INDEX `fk_movie_genre_genre1_idx` (`genre_id` ASC) VISIBLE,
  INDEX `fk_movie_genre_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_genre_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `mydb`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_genre_genre1`
    FOREIGN KEY (`genre_id`)
    REFERENCES `mydb`.`genre` (`genre_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`actors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`actors` ;

CREATE TABLE IF NOT EXISTS `mydb`.`actors` (
  `actors_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `actor_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`actors_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movie_actors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`movie_actors` ;

CREATE TABLE IF NOT EXISTS `mydb`.`movie_actors` (
  `movie_id` INT UNSIGNED NOT NULL,
  `actors_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `actors_id`),
  INDEX `fk_movie_actors_actors1_idx` (`actors_id` ASC) VISIBLE,
  INDEX `fk_movie_actors_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_actors_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `mydb`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_actors_actors1`
    FOREIGN KEY (`actors_id`)
    REFERENCES `mydb`.`actors` (`actors_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`special_feature`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`special_feature` ;

CREATE TABLE IF NOT EXISTS `mydb`.`special_feature` (
  `special_feature_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `special_feature_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`special_feature_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movie_special_feature`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`movie_special_feature` ;

CREATE TABLE IF NOT EXISTS `mydb`.`movie_special_feature` (
  `movie_id` INT UNSIGNED NOT NULL,
  `special_feature_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `special_feature_id`),
  INDEX `fk_movie_special_feature_special_feature1_idx` (`special_feature_id` ASC) VISIBLE,
  INDEX `fk_movie_special_feature_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_special_feature_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `mydb`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_special_feature_special_feature1`
    FOREIGN KEY (`special_feature_id`)
    REFERENCES `mydb`.`special_feature` (`special_feature_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`movie_media_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`movie_media_type` ;

CREATE TABLE IF NOT EXISTS `mydb`.`movie_media_type` (
  `movie_id` INT UNSIGNED NOT NULL,
  `media_type_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`, `media_type_id`),
  INDEX `fk_movie_media_type_media_type1_idx` (`media_type_id` ASC) VISIBLE,
  INDEX `fk_movie_media_type_movie1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_media_type_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `mydb`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_media_type_media_type1`
    FOREIGN KEY (`media_type_id`)
    REFERENCES `mydb`.`media_type` (`media_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`price`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`price` ;

CREATE TABLE IF NOT EXISTS `mydb`.`price` (
  `price_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `price` DECIMAL(5,2) UNSIGNED NOT NULL,
  `movie_id` INT UNSIGNED NOT NULL,
  `media_type_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`price_id`, `movie_id`, `media_type_id`),
  INDEX `fk_price_movie_media_type1_idx` (`movie_id` ASC, `media_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_price_movie_media_type1`
    FOREIGN KEY (`movie_id` , `media_type_id`)
    REFERENCES `mydb`.`movie_media_type` (`movie_id` , `media_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
