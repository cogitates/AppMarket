-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: appmarket
-- ------------------------------------------------------
-- Server version	5.7.21-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `commenttable`
--

DROP TABLE IF EXISTS `commenttable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commenttable` (
  `commentid` int(11) NOT NULL,
  `appid` int(11) DEFAULT NULL,
  `mark` int(11) DEFAULT NULL,
  `comment` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`commentid`),
  KEY `appid_idx` (`appid`),
  CONSTRAINT `appid` FOREIGN KEY (`appid`) REFERENCES `insideapp` (`insideappid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commenttable`
--

LOCK TABLES `commenttable` WRITE;
/*!40000 ALTER TABLE `commenttable` DISABLE KEYS */;
INSERT INTO `commenttable` VALUES (1,1,3,'general'),(2,3,4,'love it'),(3,6,5,'very good'),(4,6,4,'excellent'),(5,3,4,'my money gone'),(7,4,5,'good'),(9,4,5,'excellent app'),(10,11,5,'very good'),(11,11,4,'i like it'),(12,11,3,'good');
/*!40000 ALTER TABLE `commenttable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `developer`
--

DROP TABLE IF EXISTS `developer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `developer` (
  `developerid` int(11) NOT NULL,
  `developername` varchar(45) DEFAULT NULL,
  `developerpwd` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`developerid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `developer`
--

LOCK TABLES `developer` WRITE;
/*!40000 ALTER TABLE `developer` DISABLE KEYS */;
INSERT INTO `developer` VALUES (1,'tencent-wechat','001'),(2,'tencent-QQ','002'),(3,'alibaba','003'),(4,'netease','004'),(5,'baidu','005'),(6,'Google','006'),(7,'JD','007'),(8,'sina','008');
/*!40000 ALTER TABLE `developer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedbackid` int(11) NOT NULL,
  `outsideappid` int(11) DEFAULT NULL,
  `feedback` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`feedbackid`),
  KEY `outsideappid_idx` (`outsideappid`),
  CONSTRAINT `outsideappid` FOREIGN KEY (`outsideappid`) REFERENCES `outsideapp` (`outsideappid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,1004,'some bug'),(3,9,'too much  authority'),(4,1006,' some questions');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insideapp`
--

DROP TABLE IF EXISTS `insideapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `insideapp` (
  `insideappid` int(11) NOT NULL,
  `appname` varchar(45) DEFAULT NULL,
  `appdescription` varchar(45) DEFAULT NULL,
  `developerid` int(11) DEFAULT NULL,
  PRIMARY KEY (`insideappid`),
  KEY `developer_idx` (`developerid`),
  KEY `idx_insideapp_appname` (`appname`),
  CONSTRAINT `developerid` FOREIGN KEY (`developerid`) REFERENCES `developer` (`developerid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insideapp`
--

LOCK TABLES `insideapp` WRITE;
/*!40000 ALTER TABLE `insideapp` DISABLE KEYS */;
INSERT INTO `insideapp` VALUES (1,'wechat','chat',1),(3,'alipay','spending money',3),(4,'netease music','music',4),(6,'chrome','brower',6),(7,'gboad','keyboard',6),(9,'QQ','chat ',2),(10,'jd','shopping',7),(11,'weibo','news stars',8),(13,'baidu netdisk','netdisk',5),(15,'youtube','video',6),(16,'google doc','doc',6),(17,'netease read','read',4);
/*!40000 ALTER TABLE `insideapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager` (
  `managerid` int(11) NOT NULL,
  `managername` varchar(45) DEFAULT NULL,
  `managerpwd` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`managerid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` VALUES (1,'weifeng','123');
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outsideapp`
--

DROP TABLE IF EXISTS `outsideapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outsideapp` (
  `outsideappid` int(11) NOT NULL,
  `appname` varchar(45) DEFAULT NULL,
  `appdescription` varchar(45) DEFAULT NULL,
  `developerid` int(11) DEFAULT NULL,
  PRIMARY KEY (`outsideappid`),
  KEY ` developerid_idx` (`developerid`),
  CONSTRAINT ` developerid` FOREIGN KEY (`developerid`) REFERENCES `developer` (`developerid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outsideapp`
--

LOCK TABLES `outsideapp` WRITE;
/*!40000 ALTER TABLE `outsideapp` DISABLE KEYS */;
INSERT INTO `outsideapp` VALUES (8,'taobao','shopping',3),(9,'netease course','learn',4),(14,'baidu map','map',5),(1004,'QQ brower','web ',1),(1005,'netease news','news',4),(1006,'youdao ','dictionary',4);
/*!40000 ALTER TABLE `outsideapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `userpwd` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user1','111'),(2,'user2','222'),(3,'user3','333'),(4,'user4','444');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `user_view`
--

DROP TABLE IF EXISTS `user_view`;
/*!50001 DROP VIEW IF EXISTS `user_view`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `user_view` AS SELECT 
 1 AS `insideappid`,
 1 AS `appname`,
 1 AS `appdescription`,
 1 AS `developername`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `user_view`
--

/*!50001 DROP VIEW IF EXISTS `user_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_view` AS select `insideapp`.`insideappid` AS `insideappid`,`insideapp`.`appname` AS `appname`,`insideapp`.`appdescription` AS `appdescription`,`developer`.`developername` AS `developername` from (`insideapp` join `developer`) where (`insideapp`.`developerid` = `developer`.`developerid`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-30 16:54:51
