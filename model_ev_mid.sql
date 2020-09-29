CREATE TABLE `model_ev_resu` (
	`state_dt` VARCHAR(50) NOT NULL DEFAULT '',
    `stock_code` varchar(45) NOT NULL DEFAULT '',
    `acc` decimal(20,4) default NULL,
    `recall` decimal(20,4) default null ,
    `f1` decimal(20,4) default null,
    `acc_neg` decimal(20,4) default null,
    `bz` VARCHAR(45) DEFAULT NULL,
    `predict` VARCHAR(45) DEFAULT NULL,
    PRIMARY KEY(`state_dt`,`stock_code`)
    )ENGINE = InnoDB DEFAULT CHARSET = `gbk`;