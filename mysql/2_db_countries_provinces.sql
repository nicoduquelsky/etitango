-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: db_etitango
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `countries_province`
--

DROP TABLE IF EXISTS `countries_province`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries_province`
(
  `id` int NOT NULL AUTO_INCREMENT,
  `province_name` varchar
(64) DEFAULT NULL,
  `country_id` varchar
(2) DEFAULT NULL,
  PRIMARY KEY
(`id`),
  UNIQUE KEY `province_name`
(`province_name`),
  KEY `countries_province_country_id_2208426f_fk_countries`
(`country_id`),
  CONSTRAINT `countries_province_country_id_2208426f_fk_countries` FOREIGN KEY
(`country_id`) REFERENCES `countries_country`
(`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries_province`
--

LOCK TABLES `countries_province` WRITE;
/*!40000 ALTER TABLE `countries_province` DISABLE KEYS */;
/*!40000 ALTER TABLE `countries_province` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-05 18:53:49

INSERT INTO `countries_province` (`id`, `province_name`, `country_id`) VALUES
(1, 'Buenos Aires', 'AR'),
(2, 'Buenos Aires-GBA', 'AR'),
(3, 'Capital Federal', 'AR'),
(4, 'Catamarca', 'AR'),
(5, 'Chaco', 'AR'),
(6, 'Chubut', 'AR'),
(7, 'Córdoba', 'AR'),
(8, 'Corrientes', 'AR'),
(9, 'Entre Ríos', 'AR'),
(10, 'Formosa', 'AR'),
(11, 'Jujuy', 'AR'),
(12, 'La Pampa', 'AR'),
(13, 'La Rioja', 'AR'),
(14, 'Mendoza', 'AR'),
(15, 'Misiones', 'AR'),
(16, 'Neuquén', 'AR'),
(17, 'Río Negro', 'AR'),
(18, 'Salta', 'AR'),
(19, 'San Juan', 'AR'),
(20, 'San Luis', 'AR'),
(21, 'Santa Cruz', 'AR'),
(22, 'Santa Fe', 'AR'),
(23, 'Santiago del Estero', 'AR'),
(24, 'Tierra del Fuego', 'AR'),
(25, 'Tucumán', 'AR'),
(26, 'Arica y Parinacota', 'CL'),
(27, 'Tarapacá', 'CL'),
(28, 'Antofagasta', 'CL'),
(29, 'Atacama', 'CL'),
(30, 'Coquimbo', 'CL'),
(31, 'Valparaíso', 'CL'),
(32, 'Lib. Gral. Bernardo O Higgins', 'CL'),
(33, 'Maule', 'CL'),
(34, 'Ñuble', 'CL'),
(35, 'Biobío', 'CL'),
(36, 'La Araucanía', 'CL'),
(37, 'Los Ríos', 'CL'),
(38, 'Los Lagos', 'CL'),
(39, 'Aysén del Gral. C. Ibáñez del Campo', 'CL'),
(40, 'Magallanes y Antártica Chilena', 'CL'),
(41, 'Metropolitana de Santiago', 'CL');