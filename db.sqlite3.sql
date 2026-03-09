BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "result_user" (
	"id"	integer NOT NULL,
	"email"	varchar(225) NOT NULL,
	"password"	varchar(225) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "result_student" (
	"id"	integer NOT NULL,
	"name"	varchar(225) NOT NULL,
	"dob"	date NOT NULL,
	"age"	integer NOT NULL,
	"address"	text NOT NULL,
	"branch"	varchar(225) NOT NULL,
	"HallTicketNo"	varchar(225) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2024-04-06 13:05:11.730465'),
 (2,'auth','0001_initial','2024-04-06 13:05:11.802584'),
 (3,'admin','0001_initial','2024-04-06 13:05:11.842063'),
 (4,'admin','0002_logentry_remove_auto_add','2024-04-06 13:05:11.876654'),
 (5,'admin','0003_logentry_add_action_flag_choices','2024-04-06 13:05:11.898100'),
 (6,'contenttypes','0002_remove_content_type_name','2024-04-06 13:05:11.942925'),
 (7,'auth','0002_alter_permission_name_max_length','2024-04-06 13:05:11.979613'),
 (8,'auth','0003_alter_user_email_max_length','2024-04-06 13:05:12.011693'),
 (9,'auth','0004_alter_user_username_opts','2024-04-06 13:05:12.031779'),
 (10,'auth','0005_alter_user_last_login_null','2024-04-06 13:05:12.072822'),
 (11,'auth','0006_require_contenttypes_0002','2024-04-06 13:05:12.092243'),
 (12,'auth','0007_alter_validators_add_error_messages','2024-04-06 13:05:12.111939'),
 (13,'auth','0008_alter_user_username_max_length','2024-04-06 13:05:12.161852'),
 (14,'auth','0009_alter_user_last_name_max_length','2024-04-06 13:05:12.319961'),
 (15,'auth','0010_alter_group_name_max_length','2024-04-06 13:05:12.359404'),
 (16,'auth','0011_update_proxy_permissions','2024-04-06 13:05:12.392222'),
 (17,'auth','0012_alter_user_first_name_max_length','2024-04-06 13:05:12.444298'),
 (18,'sessions','0001_initial','2024-04-06 13:05:12.503828'),
 (19,'result','0001_initial','2024-05-12 05:16:08.676797'),
 (20,'result','0002_admin_delete_user','2024-05-13 05:02:58.224163'),
 (21,'result','0003_delete_admin','2024-05-13 12:27:58.735992'),
 (22,'result','0004_initial','2024-05-13 12:44:16.708187'),
 (23,'result','0005_student','2024-05-13 12:59:11.228567'),
 (24,'result','0006_alter_student_hallticketno_alter_student_age','2024-05-13 12:59:53.387381'),
 (25,'result','0007_alter_student_hallticketno','2024-05-14 05:20:31.876578');
INSERT INTO "auth_user_user_permissions" ("id","user_id","permission_id") VALUES (69,6,1),
 (70,6,2),
 (71,6,3),
 (72,6,4),
 (73,6,5),
 (74,6,6),
 (75,6,7),
 (76,6,8),
 (77,6,9),
 (78,6,10),
 (79,6,11),
 (80,6,12),
 (81,6,13),
 (82,6,14),
 (83,6,15),
 (84,6,16),
 (85,6,17),
 (86,6,18),
 (87,6,19),
 (88,6,20),
 (89,6,21),
 (90,6,22),
 (91,6,23),
 (92,6,24),
 (93,6,25),
 (94,6,26),
 (95,6,27),
 (96,6,28),
 (97,6,29),
 (98,6,30),
 (99,6,31),
 (100,6,32),
 (101,6,33),
 (102,6,34),
 (103,6,35),
 (104,6,36);
INSERT INTO "django_admin_log" ("id","object_id","object_repr","action_flag","change_message","content_type_id","user_id","action_time") VALUES (10,'5','akshay123',3,'',4,6,'2024-05-14 06:10:48.913707'),
 (11,'6','user',2,'[{"changed": {"fields": ["User permissions"]}}]',4,6,'2024-05-14 06:10:58.170394'),
 (12,'4','Student object (4)',3,'',9,6,'2024-05-14 12:58:32.138141'),
 (13,'3','Student object (3)',3,'',9,6,'2024-05-14 12:58:32.159721');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'result','user'),
 (8,'result','admin'),
 (9,'result','student');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_user','Can add user'),
 (26,7,'change_user','Can change user'),
 (27,7,'delete_user','Can delete user'),
 (28,7,'view_user','Can view user'),
 (29,8,'add_admin','Can add admin'),
 (30,8,'change_admin','Can change admin'),
 (31,8,'delete_admin','Can delete admin'),
 (32,8,'view_admin','Can view admin'),
 (33,9,'add_student','Can add student'),
 (34,9,'change_student','Can change student'),
 (35,9,'delete_student','Can delete student'),
 (36,9,'view_student','Can view student');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES (6,'pbkdf2_sha256$600000$cuV6XtbHvsgoRQYLsEqg6r$I4QkokCYCYuyiSSmngfjTkw5klqQuRzJecLSQYlIatQ=','2024-05-15 14:55:17.410840',1,'user','','',1,1,'2024-05-14 06:09:59','');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('j2dzipk6r235s8oil5ww0txd7xt0800d','.eJxVjEEOgjAQRe_StWmYlhmLS_eegUyng0UNTSisjHcXEha6_e-9_zY9r0vu16pzPyZzMWBOv1tkeeq0g_Tg6V6slGmZx2h3xR602ltJ-roe7t9B5pq3mgRJKVIHNJCLCA5kANJOQLxSkyC0Q3NWlNAKqgYRDFuEHTrPns3nC9nWN68:1s60gv:wAp-IITdlIVwxR-jcfiTsrXQgFnF9YONDN8FnbKkVxY','2024-05-26 04:20:05.617702'),
 ('8e4cati2s6iok2a7thoq4osvvdaknop9','.eJxVjMsOwiAQRf-FtSG8Cy7d-w1kYBipGkhKuzL-uzbpQrf3nHNfLMK21riNssQZ2Zk5dvrdEuRHaTvAO7Rb57m3dZkT3xV-0MGvHcvzcrh_BxVG_dYes1EhSUJLxWpI0miLSqHxlEEiaamKAW8tOTdR0BSUtgJ9mUSWWbD3B_gNOAc:1s7G2H:GPGoGpzbNkOAK3_MeZNV4RCFaXOyXYhDz1rrfO2IUGg','2024-05-29 14:55:17.432753');
INSERT INTO "result_student" ("id","name","dob","age","address","branch","HallTicketNo") VALUES (1,'akshay','2006-04-06',18,'GDK','CSM','23XW5A6609'),
 (2,'sadana','2005-06-06',19,'hyd','CSM','22XW1A6648');
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
