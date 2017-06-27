import MySQLdb, sqlite3
from os.path import isfile

from app import db as application_db
from app import app
from app.models import User

from config import db_settings

#----
#
#
#
#### CONSTANTS ####
# Default Users
SUPER_USER  = { "firstname": "Super",
                "lastname": "User",
                "username": "superuser" }
ADMIN       = { "firstname": "Admin",
                "lastname": "User",
                "username": "admin" }
DOCTOR      = { "firstname": "Investigation",
                "lastname": "Doctor",
                "username": "doctor" }
EMPLOYEE    = { "firstname": "Registeration",
                "lastname": "Employee",
                "username": "emp" }

# Theme Settings
STEP_INFO   = ">"
STEP_WARN   = "!"
STEP_ERR    = "X"
STEP_DONE   = "  DONE!."

#----
#
#
#
#### Functions ####
def setup_database(db_settings):
    DB_NAME = db_settings.value["NAME"]

    if db_settings.type == 'mysql':
        connection = MySQLdb.connect(host=db_settings.value["HOST"],
                                    user=db_settings.value["USER"],
                                    passwd=db_settings.value["PASSWD"])
        c = connection.cursor()

        try:
            print "{} Create database with name '{}'...".format(STEP_INFO, DB_NAME)

            c.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)
            )

            print STEP_DONE

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            if list(e)[0] == 1007:
                print "{} Database <{}> already exists.".format(STEP_WARN, DB_NAME)

            else:
                print "{} {}".format(STEP_ERR, e)
                exit(1)

        except Exception as e:
            print e
            exit(1)

        finally:
            connection.close()


    if db_settings.type == 'sqlite':
        db_file_path = 'app/' + db_settings.value["NAME"]

        print "{} Checking sqlite database '{}'..." \
                    .format(STEP_INFO, DB_NAME)

        if not isfile(db_file_path):
            try:
                print "{} Create sqlite database '{}'..." \
                            .format(STEP_INFO, DB_NAME)

                open(db_file_path, 'a').close()

                print STEP_DONE

            except Exception as e:
                print "{} {}".format(STEP_ERR, e)
                exit(1)
        else:
            print STEP_DONE


def create_default_tables(db, db_settings):
    DB_NAME = db_settings.value["NAME"]

    print "{} Create default tables for '{}'...".format(STEP_INFO, DB_NAME)

    try:
        db.create_all()
        db.session.commit()

        print STEP_DONE

    except Exception as e:
        db.session.rollback()
        print "{} {}".format(STEP_ERR, e)
        exit(1)


def create_default_user(db, firstname, lastname, username):
    print "{} Create default '{}' user...".format(STEP_INFO, username)

    try:
        user = User()
        user.firstname = firstname
        user.lastname  = lastname
        user.username  = username
        user.hash_password(username)

        db.session.add(user)
        db.session.commit()

        print "  Username: {}".format(username)
        print "  Password: {}".format(username)
        print STEP_DONE

    except Exception as e:
        db.session.rollback()
        print "{} {}".format(STEP_ERR, e.message)

#----
#
#
#
#### __main__ ####
setup_database(db_settings)
create_default_tables(application_db, db_settings)

create_default_user(application_db, **SUPER_USER)
create_default_user(application_db, **ADMIN)
create_default_user(application_db, **DOCTOR)
create_default_user(application_db, **EMPLOYEE)