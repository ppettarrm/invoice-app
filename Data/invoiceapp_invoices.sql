-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: invoiceapp
-- ------------------------------------------------------
-- Server version	5.7.36-log

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
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoices` (
  `invoice_id` varchar(30) NOT NULL,
  `product_id` int(11) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `product_price` decimal(10,2) NOT NULL,
  `product_amount` int(11) NOT NULL,
  `product_measure` varchar(10) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `used` tinyint(4) DEFAULT '0',
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES ('20211225204322',1010,'Paradajz',120.89,1,'kg',56,0,1),('20211225204322',5839,'Milka cokolada 300g',427.97,1,'kom',57,0,1),('20211225204322',18790,'Plazma keks 150g',100.00,5,'kom',58,0,1),('20211225204539',18790,'Plazma keks 150g',100.00,1,'kom',59,0,1),('20211225204539',1010,'Paradajz',120.89,1,'kg',60,0,1),('20211225204659',1010,'Paradajz',120.89,1,'kg',61,0,1),('20211225204944',1010,'Paradajz',120.89,2,'kg',62,0,1),('20211225204944',4879,'Stark bananica',15.00,10,'kom',63,0,1),('20211225205654',1010,'Paradajz',120.89,2,'kg',64,0,1),('20211225205654',5839,'Milka cokolada 300g',427.97,1,'kom',65,0,1),('20211225205817',1010,'Paradajz',120.89,2,'kg',66,1,1),('20211225205817',18790,'Plazma keks 150g',100.00,2,'kom',67,1,1),('2021122521151',57369,'Bakterioloska analiza',3067.57,2,'kom',68,1,746826),('2021122521151',16829,'Antigenski test Covid-19',999.90,2,'kom',69,1,746826),('20221318042',1010,'Paradajz',120.89,1,'kg',70,0,1);
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-11 10:17:09
