-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Week1data
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Week1data` ;

-- -----------------------------------------------------
-- Schema Week1data
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Week1data` DEFAULT CHARACTER SET utf8 ;
USE `Week1data` ;

-- -----------------------------------------------------
-- Table `Week1data`.`Photo_gallery`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Week1data`.`Photo_gallery` ;

CREATE TABLE IF NOT EXISTS `Week1data`.`Photo_gallery` (
  `Photo_gallery_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Photo_gallery_home_selfies` INT UNSIGNED NOT NULL,
  `Photo_gallery_home_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_home_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_home_interior/landscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_home_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_home_screenshot` INT UNSIGNED NOT NULL,
  `Photo_gallery_work_selfie` INT UNSIGNED NOT NULL,
  `Photo_gallery_work_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_work_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_work_interior/still-life` INT UNSIGNED NOT NULL,
  `Photo_gallery_work_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_work_screenshot` INT UNSIGNED NOT NULL,
  `Photo_gallery_social-setting_selfie` INT UNSIGNED NOT NULL,
  `Photo_gallery_social-setting_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_social-setting_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_social-setting_interior/still-life` INT UNSIGNED NOT NULL,
  `Photo_gallery_social-setting_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_social-setting_screenshot` INT UNSIGNED NOT NULL,
  `Photo_gallery_outdoors_selfie` INT UNSIGNED NOT NULL,
  `Photo_gallery_outdoors_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_outdoors_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_outdoors_interior/still-life` INT UNSIGNED NOT NULL,
  `Photo_gallery_outdoors_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_outdoors_screenshot` INT UNSIGNED NOT NULL,
  `Photo_gallery_school_selfie` INT UNSIGNED NOT NULL,
  `Photo_gallery_school_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_school_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_school_interior/still-life` INT UNSIGNED NOT NULL,
  `Photo_gallery_school_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_school_screenshot` INT UNSIGNED NOT NULL,
  `Photo_gallery_car_selfie` INT UNSIGNED NOT NULL,
  `Photo_gallery_car_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_car_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_car_interior/stilllife` INT UNSIGNED NOT NULL,
  `Photo_gallery_car_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_car_screenshot` INT UNSIGNED NOT NULL,
  `Photo_gallery_other_selfie` INT UNSIGNED NOT NULL,
  `Photo_gallery_other_group/others` INT UNSIGNED NOT NULL,
  `Photo_gallery_other_landscape/cityscape` INT UNSIGNED NOT NULL,
  `Photo_gallery_other_interior/still-life` INT UNSIGNED NOT NULL,
  `Photo_gallery_other_documentation` INT UNSIGNED NOT NULL,
  `Photo_gallery_other_screenshot` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Photo_gallery_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Week1data`.`distraction1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Week1data`.`distraction1` ;

CREATE TABLE IF NOT EXISTS `Week1data`.`distraction1` (
  `distraction1_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `distraction1_date` DATE NOT NULL,
  `distraction1_internet` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction1_social_media` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction1_digital_interactions` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction1_something_happening` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction1_someone_in_real_life` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction1_other` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`distraction1_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Week1data`.`distraction2`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Week1data`.`distraction2` ;

CREATE TABLE IF NOT EXISTS `Week1data`.`distraction2` (
  `distraction2_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `distraction2_date` DATE NOT NULL,
  `distraction2_internet` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction2_social_media` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction2_digital_interactions` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction2_something_happening` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction2_someone_in_real_life` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction2_other` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`distraction2_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Week1data`.`distraction3`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Week1data`.`distraction3` ;

CREATE TABLE IF NOT EXISTS `Week1data`.`distraction3` (
  `distraction3_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `distraction3_date` DATE NOT NULL,
  `distraction3_internet` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction3_social_media` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction3_digital_interactions` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction3_something_happening` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction3_someone_in_real_life` INT UNSIGNED NOT NULL DEFAULT 0,
  `distraction3_other` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`distraction3_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Week1data`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Week1data`.`person` ;

CREATE TABLE IF NOT EXISTS `Week1data`.`person` (
  `person_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `person_fname` VARCHAR(25) NOT NULL,
  `person_lname` VARCHAR(35) NOT NULL,
  `Photo_gallery_id` INT UNSIGNED NOT NULL,
  `distraction1_id` INT UNSIGNED NOT NULL,
  `distraction2_id` INT UNSIGNED NOT NULL,
  `distraction3_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`person_id`),
  INDEX `fk_person_Photo_gallery_idx` (`Photo_gallery_id` ASC) VISIBLE,
  INDEX `fk_person_distraction11_idx` (`distraction1_id` ASC) VISIBLE,
  INDEX `fk_person_distraction21_idx` (`distraction2_id` ASC) VISIBLE,
  INDEX `fk_person_distraction31_idx` (`distraction3_id` ASC) VISIBLE,
  CONSTRAINT `fk_person_Photo_gallery`
    FOREIGN KEY (`Photo_gallery_id`)
    REFERENCES `Week1data`.`Photo_gallery` (`Photo_gallery_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_distraction11`
    FOREIGN KEY (`distraction1_id`)
    REFERENCES `Week1data`.`distraction1` (`distraction1_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_distraction21`
    FOREIGN KEY (`distraction2_id`)
    REFERENCES `Week1data`.`distraction2` (`distraction2_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_distraction31`
    FOREIGN KEY (`distraction3_id`)
    REFERENCES `Week1data`.`distraction3` (`distraction3_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
