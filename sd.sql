CREATE TABLE "users" (
  "ID" integer PRIMARY KEY,
  "team_id" integer,
  "username" varchar
);

CREATE TABLE "userUserRoles" (
  "userID" integer,
  "roleID" integer,
  PRIMARY KEY ("userID", "roleID")
);

CREATE TABLE "tasks" (
  "ID" integer PRIMARY KEY,
  "parent_task_id" integer,
  "project_id" integer,
  "priority" integer,
  "asignee_id" integer,
  "start_date" date,
  "due_date" date
);

CREATE TABLE "Team" (
  "ID" integer PRIMARY KEY
);

CREATE TABLE "project" (
  "Id" integer PRIMARY KEY
);

CREATE TABLE "teamusers" (
  "team_id" integer,
  "user_id" integer,
  PRIMARY KEY ("team_id", "user_id")
);

CREATE TABLE "comments" (
  "ID" integer PRIMARY KEY,
  "author_id" integer,
  "task_id" integer
);

CREATE TABLE "timelogs" (
  "ID" integer PRIMARY KEY,
  "task_id" integer,
  "user_id" integer,
  "time_minutes" integer,
  "date" date
);

CREATE TABLE "userroles" (
  "ID" integer PRIMARY KEY
);

ALTER TABLE "userUserRoles" ADD FOREIGN KEY ("userID") REFERENCES "users" ("ID");

ALTER TABLE "userUserRoles" ADD FOREIGN KEY ("roleID") REFERENCES "userroles" ("ID");

ALTER TABLE "teamusers" ADD FOREIGN KEY ("team_id") REFERENCES "Team" ("ID");

ALTER TABLE "teamusers" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("ID");

ALTER TABLE "comments" ADD FOREIGN KEY ("ID") REFERENCES "users" ("ID");

ALTER TABLE "comments" ADD FOREIGN KEY ("task_id") REFERENCES "tasks" ("ID");

ALTER TABLE "timelogs" ADD FOREIGN KEY ("task_id") REFERENCES "tasks" ("ID");

ALTER TABLE "users" ADD FOREIGN KEY ("ID") REFERENCES "tasks" ("asignee_id");

ALTER TABLE "project" ADD FOREIGN KEY ("Id") REFERENCES "tasks" ("project_id");
