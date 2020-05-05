CREATE TABLE `users` (
  `user_name` varchar(0) NOT NULL,
  `user_password` varchar(0) NOT NULL,
  `device_id` varchar(20) NOT NULL,
  PRIMARY KEY (`device_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
