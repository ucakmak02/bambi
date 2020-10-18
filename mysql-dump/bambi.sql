-- MySQL dump 10.13  Distrib 8.0.19, for osx10.15 (x86_64)
--
-- Host: localhost    Database: bambi
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `bambi`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `bambi` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `bambi`;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_class` varchar(100) DEFAULT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `product_price` varchar(30) DEFAULT NULL,
  `product_title` varchar(100) DEFAULT NULL,
  `product_expo` varchar(100) DEFAULT NULL,
  `register_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (11,'main_page','thirdSlide.jpg','','','','','2020-10-15 18:31:29'),(15,'main_page','firstSlide.jpg','','','','','2020-10-15 21:23:44'),(16,'main_page','secondSlide.jpg','','','','','2020-10-16 11:30:32'),(22,'yatak','99542736978278.jpg','Borjen Yatak','2300€','','','2020-10-16 12:55:28'),(23,'yatak','95758353616051.jpg','Magnasand Therapy Yatak','2000€','','','2020-10-16 13:04:04'),(24,'yatak','44868001953575.jpg','Royal Craft Yatak','1000€','','','2020-10-16 13:17:39'),(25,'yatak','90434102348425.jpg','Visco Comfort Yatak','3000€','','','2020-10-16 13:18:42'),(26,'yatak','34510214815928.jpg','Latex Therapy Yatak','1000€','','','2020-10-16 13:19:37'),(27,'komidin','71674350596475.jpg','Clima Naturel Prime Komodin','1200€','','','2020-10-16 13:21:28'),(28,'komidin','69332323506989.jpg','Clima Naturel Prime Komodin','2000€','','','2020-10-16 13:22:23'),(29,'komidin','23790216781578.jpg','Prime Komodin','900€','','','2020-10-16 13:28:57'),(30,'komidin','60322166180284.jpg',' Naturel Komodin','1200€','','','2020-10-16 13:30:05'),(31,'tekstil','25881043575177.jpg','Clima Naturel Prime','200€','','','2020-10-16 13:31:13'),(32,'tekstil','37702791761852.jpg','Clima Naturel Prime','200€','','','2020-10-16 13:32:04'),(33,'tekstil','33081060670879.jpg','Clima Naturel Prime','200€','','','2020-10-16 13:32:25'),(34,'tekstil','86683245989172.jpg','Clima Naturel Prime','200€','','','2020-10-16 13:32:39'),(35,'koltuk','66006396662087.jpg','Koltuk Takımı','2000€','','','2020-10-16 13:35:56'),(36,'koltuk','7744393665596.jpg','Koltuk Takımı','2000€','','','2020-10-16 13:36:13'),(37,'koltuk','42399366675489.jpg','Koltuk Takımı','2000€','','','2020-10-16 13:36:28'),(38,'koltuk','73252050584175.jpg','Koltuk Takımı','2000€','','','2020-10-16 13:36:42'),(39,'main_page','4116084494996.jpg','firstSlide','','BAMBI ','LITERIE & MEUBLES','2020-10-16 14:34:58'),(41,'koltuk','83758340889248.jpg','Evdeki koltuk','3000€','','','2020-10-16 14:51:18'),(47,'main_page','84242342019990.jpg','secondSlide','','','','2020-10-17 09:49:23'),(49,'main_page','16301009293974.jpg','thirdSlide','','','','2020-10-17 11:13:07');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-18 18:05:54
