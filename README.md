# djangocurd
django curd database table MYSQL

      DROP TABLE IF EXISTS `djangoapp`.`employee`;
      CREATE TABLE  `djangoapp`.`employee` (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `name` varchar(20) NOT NULL,
        `email` varchar(45) NOT NULL,
        `contact` varchar(15) NOT NULL,
        PRIMARY KEY (`id`)
      ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
