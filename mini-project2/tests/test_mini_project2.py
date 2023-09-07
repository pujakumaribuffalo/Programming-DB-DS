import unittest
import pandas as pd
import mini_project2
import sqlite3
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestMiniProject2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        normalized_database_filename = 'normalized.db'
        cls.conn = mini_project2.create_connection(
            normalized_database_filename, delete_db=True)

    def setUp(self):
        self.mini_project2 = mini_project2

    @weight(5)
    @visibility('visible')
    @number("step1")
    def test_step1(self):
        data_filename = 'data.csv'
        normalized_database_filename = 'normalized.db'
        self.mini_project2.step1_create_region_table(
            data_filename, normalized_database_filename)
        data = pd.read_csv("step1.csv")
        df = pd.read_sql_query("""SELECT * FROM Region""", self.conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("step2")
    def test_step2(self):
        normalized_database_filename = 'normalized.db'
        region_to_regionid_dict = self.mini_project2.step2_create_region_to_regionid_dictionary(
            normalized_database_filename)
        expected_solution = {
            'British Isles': 1,
            'Central America': 2,
            'Eastern Europe': 3,
            'North America': 4,
            'Northern Europe': 5,
            'Scandinavia': 6,
            'South America': 7,
            'Southern Europe': 8,
            'Western Europe': 9
        }
        assert expected_solution == region_to_regionid_dict

    @weight(5)
    @visibility('visible')
    @number("step3")
    def test_step3(self):
        data_filename = 'data.csv'
        normalized_database_filename = 'normalized.db'
        self.mini_project2.step3_create_country_table(
            data_filename, normalized_database_filename)
        data = pd.read_csv("step3.csv")
        conn = self.mini_project2.create_connection(
            normalized_database_filename)
        df = pd.read_sql_query("""SELECT * FROM Country""", conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("step4")
    def test_step4(self):
        normalized_database_filename = 'normalized.db'
        country_to_countryid_dict = self.mini_project2.step4_create_country_to_countryid_dictionary(
            normalized_database_filename)
        expected_solution = {
            'Argentina': 1,
            'Austria': 2,
            'Belgium': 3,
            'Brazil': 4,
            'Canada': 5,
            'Denmark': 6,
            'Finland': 7,
            'France': 8,
            'Germany': 9,
            'Ireland': 10,
            'Italy': 11,
            'Mexico': 12,
            'Norway': 13,
            'Poland': 14,
            'Portugal': 15,
            'Spain': 16,
            'Sweden': 17,
            'Switzerland': 18,
            'UK': 19,
            'USA': 20,
            'Venezuela': 21
        }
        assert expected_solution == country_to_countryid_dict

    @weight(5)
    @visibility('visible')
    @number("step5")
    def test_step5(self):
        normalized_database_filename = 'normalized.db'
        data_filename = 'data.csv'
        self.mini_project2.step5_create_customer_table(
            data_filename, normalized_database_filename)
        data = pd.read_csv("step5.csv")
        conn = self.mini_project2.create_connection(normalized_database_filename)
        df = pd.read_sql_query("""SELECT * FROM Customer""", conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("step6")
    def test_step6(self):
        normalized_database_filename = 'normalized.db'
        customer_to_customerid_dict = self.mini_project2.step6_create_customer_to_customerid_dictionary(normalized_database_filename)
        expected_solution = {
            'Alejandra Camino': 1,
            'Alexander Feuer': 2,
            'Ana Trujillo': 3,
            'Anabela Domingues': 4,
            'Andre Fonseca': 5,
            'Ann Devon': 6,
            'Annette Roulet': 7,
            'Antonio Moreno': 8,
            'Aria Cruz': 9,
            'Art Braunschweiger': 10,
            'Bernardo Batista': 11,
            'Carine Schmitt': 12,
            'Carlos Gonzalez': 13,
            'Carlos Hernandez': 14,
            'Catherine Dewey': 15,
            'Christina Berglund': 16,
            'Daniel Tonini': 17,
            'Diego Roel': 18,
            'Dominique Perrier': 19,
            'Eduardo Saavedra': 20,
            'Elizabeth Brown': 21,
            'Elizabeth Lincoln': 22,
            'Felipe Izquierdo': 23,
            'Fran Wilson': 24,
            'Francisco Chang': 25,
            'Frederique Citeaux': 26,
            'Georg Pipps': 27,
            'Giovanni Rovelli': 28,
            'Guillermo Fernandez': 29,
            'Hanna Moos': 30,
            'Hari Kumar': 31,
            'Helen Bennett': 32,
            'Helvetius Nagy': 33,
            'Henriette Pfalzheim': 34,
            'Horst Kloss': 35,
            'Howard Snyder': 36,
            'Isabel de Castro': 37,
            'Jaime Yorres': 38,
            'Janete Limeira': 39,
            'Janine Labrune': 40,
            'Jean Fresniere': 41,
            'John Steel': 42,
            'Jonas Bergulfsen': 43,
            'Jose Pavarotti': 44,
            'Jose Pedro Freyre': 45,
            'Jytte Petersen': 46,
            'Karin Josephs': 47,
            'Karl Jablonski': 48,
            'Laurence Lebihan': 49,
            'Lino Rodriguez': 50,
            'Liu Wong': 51,
            'Liz Nixon': 52,
            'Lucia Carvalho': 53,
            'Manuel Pereira': 54,
            'Maria Anders': 55,
            'Maria Larsson': 56,
            'Marie Bertrand': 57,
            'Mario Pontes': 58,
            'Martin Sommer': 59,
            'Martine Rance': 60,
            'Mary Saveley': 61,
            'Matti Karttunen': 62,
            'Maurizio Moroni': 63,
            'Michael Holz': 64,
            'Miguel Angel Paolino': 65,
            'Palle Ibsen': 66,
            'Paolo Accorti': 67,
            'Pascale Cartrain': 68,
            'Patricia McKenna': 69,
            'Patricio Simpson': 70,
            'Paul Henriot': 71,
            'Paula Parente': 72,
            'Paula Wilson': 73,
            'Pedro Afonso': 74,
            'Peter Franken': 75,
            'Philip Cramer': 76,
            'Pirkko Koskitalo': 77,
            'Renate Messner': 78,
            'Rene Phillips': 79,
            'Rita Muller': 80,
            'Roland Mendel': 81,
            'Sergio Gutierrez': 82,
            'Simon Crowther': 83,
            'Sven Ottlieb': 84,
            'Thomas Hardy': 85,
            'Victoria Ashworth': 86,
            'Yang Wang': 87,
            'Yoshi Latimer': 88,
            'Yoshi Tannamuri': 89,
            'Yvonne Moncada': 90,
            'Zbyszek Piestrzeniewicz': 91
        }

        assert expected_solution == customer_to_customerid_dict

    @weight(5)
    @visibility('visible')
    @number("step7")
    def test_step7(self):
        normalized_database_filename = 'normalized.db'
        data_filename = 'data.csv'
        self.mini_project2.step7_create_productcategory_table(data_filename, normalized_database_filename)
        data = pd.read_csv("step7.csv")
        conn = self.mini_project2.create_connection(normalized_database_filename)
        df = pd.read_sql_query("""SELECT * FROM ProductCategory""", conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("step8")
    def test_step8(self):
        normalized_database_filename = 'normalized.db'
        productcategory_to_productcategoryid_dict = self.mini_project2.step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename)
        expected_solution = {
            'Beverages': 1,
            'Condiments': 2,
            'Confections': 3,
            'Dairy Products': 4,
            'Grains/Cereals': 5,
            'Meat/Poultry': 6,
            'Produce': 7,
            'Seafood': 8
        }
        assert expected_solution == productcategory_to_productcategoryid_dict

    @weight(5)
    @visibility('visible')
    @number("step9")
    def test_step9(self):
        normalized_database_filename = 'normalized.db'
        data_filename = 'data.csv'
        self.mini_project2.step9_create_product_table(data_filename, normalized_database_filename)
        data = pd.read_csv("step9.csv")
        conn = self.mini_project2.create_connection(normalized_database_filename)
        df = pd.read_sql_query("""SELECT * FROM Product""", conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("step_10")
    def test_step_10(self):
        normalized_database_filename = 'normalized.db'
        product_to_productid_dict = self.mini_project2.step10_create_product_to_productid_dictionary(normalized_database_filename)
        expected_solution = {
            'Alice Mutton': 1,
            'Aniseed Syrup': 2,
            'Boston Crab Meat': 3,
            'Camembert Pierrot': 4,
            'Carnarvon Tigers': 5,
            'Chai': 6,
            'Chang': 7,
            'Chartreuse verte': 8,
            "Chef Anton's Cajun Seasoning": 9,
            "Chef Anton's Gumbo Mix": 10,
            'Chocolade': 11,
            'Cote de Blaye': 12,
            'Escargots de Bourgogne': 13,
            'Filo Mix': 14,
            'Flotemysost': 15,
            'Geitost': 16,
            'Genen Shouyu': 17,
            'Gnocchi di nonna Alice': 18,
            'Gorgonzola Telino': 19,
            "Grandma's Boysenberry Spread": 20,
            'Gravad lax': 21,
            'Guarana Fantastica': 22,
            'Gudbrandsdalsost': 23,
            'Gula Malacca': 24,
            'Gumbar Gummibarchen': 25,
            "Gustaf's Knackebrod": 26,
            'Ikura': 27,
            'Inlagd Sill': 28,
            'Ipoh Coffee': 29,
            "Jack's New England Clam Chowder": 30,
            'Konbu': 31,
            'Lakkalikoori': 32,
            'Laughing Lumberjack Lager': 33,
            'Longlife Tofu': 34,
            'Louisiana Fiery Hot Pepper Sauce': 35,
            'Louisiana Hot Spiced Okra': 36,
            'Manjimup Dried Apples': 37,
            'Mascarpone Fabioli': 38,
            'Maxilaku': 39,
            'Mishi Kobe Niku': 40,
            'Mozzarella di Giovanni': 41,
            'Nord-Ost Matjeshering': 42,
            'Northwoods Cranberry Sauce': 43,
            'NuNuCa Nu-Nougat-Creme': 44,
            'Original Frankfurter grune Soe': 45,
            'Outback Lager': 46,
            'Pate chinois': 47,
            'Pavlova': 48,
            'Perth Pasties': 49,
            'Queso Cabrales': 50,
            'Queso Manchego La Pastora': 51,
            'Raclette Courdavault': 52,
            'Ravioli Angelo': 53,
            'Rhonbrau Klosterbier': 54,
            'Rod Kaviar': 55,
            'Rogede sild': 56,
            'Rossle Sauerkraut': 57,
            'Sasquatch Ale': 58,
            'Schoggi Schokolade': 59,
            'Scottish Longbreads': 60,
            'Singaporean Hokkien Fried Mee': 61,
            "Sir Rodney's Marmalade": 62,
            "Sir Rodney's Scones": 63,
            "Sirop d'erable": 64,
            'Spegesild': 65,
            'Steeleye Stout': 66,
            'Tarte au sucre': 67,
            'Teatime Chocolate Biscuits': 68,
            'Thuringer Rostbratwurst': 69,
            'Tofu': 70,
            'Tourtiere': 71,
            'Tunnbrod': 72,
            "Uncle Bob's Organic Dried Pears": 73,
            'Valkoinen suklaa': 74,
            'Vegie-spread': 75,
            'Wimmers gute Semmelknodel': 76,
            'Zaanse koeken': 77
        }
        assert expected_solution == product_to_productid_dict

    @weight(20)
    @visibility('visible')
    @number("step_11_1")
    def test_step_11_1(self):
        normalized_database_filename = 'normalized.db'
        data_filename = 'data.csv'
        self.mini_project2.step11_create_orderdetail_table(data_filename, normalized_database_filename)
        data = pd.read_csv("step11.csv")
        conn = self.mini_project2.create_connection(normalized_database_filename)
        df = pd.read_sql_query("""SELECT * FROM OrderDetail LIMIT 1000""", conn)
        assert df.equals(data) == True


    @weight(20)
    @visibility('visible')
    @number("step_11_2")
    def test_step_11_2(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        ser = pd.read_sql_query("""SELECT count(*) FROM OrderDetail""", conn)
        assert int(ser.iloc[0])== 621806


    @weight(5)
    @visibility('visible')
    @number("z_ex1_1")
    def test_z_ex1_1(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex1(conn, 'Alejandra Camino')
        data = pd.read_csv("ex1_1.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(5)
    @visibility('visible')
    @number("z_ex1_2")
    def test_z_ex1_2(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex1(conn, 'Eduardo Saavedra')
        data = pd.read_csv("ex1_2.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(5)
    @visibility('visible')
    @number("z_ex1_2")
    def test_z_ex1_2(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex1(conn, 'Eduardo Saavedra')
        data = pd.read_csv("ex1_2.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("z_ex2_1")
    def test_z_ex2_1(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex2(conn, 'Alejandra Camino')
        data = pd.read_csv("ex2_1.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(5)
    @visibility('visible')
    @number("z_ex2_2")
    def test_z_ex2_2(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex2(conn, 'Eduardo Saavedra')
        data = pd.read_csv("ex2_2.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(5)
    @visibility('visible')
    @number("z_ex3")
    def test_z_ex3(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex3(conn)
        data = pd.read_csv("ex3.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True

    @weight(5)
    @visibility('visible')
    @number("z_ex4")
    def test_z_ex4(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex4(conn)
        data = pd.read_csv("ex4.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True



    @weight(5)
    @visibility('visible')
    @number("z_ex5")
    def test_z_ex5(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex5(conn)
        data = pd.read_csv("ex5.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(10)
    @visibility('visible')
    @number("z_ex6")
    def test_z_ex6(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex6(conn)
        data = pd.read_csv("ex6.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(10)
    @visibility('visible')
    @number("z_ex7")
    def test_z_ex7(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex7(conn)
        data = pd.read_csv("ex7.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True



    @weight(10)
    @visibility('visible')
    @number("z_ex8")
    def test_z_ex8(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex8(conn)
        data = pd.read_csv("ex8.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True


    @weight(10)
    @visibility('visible')
    @number("z_ex9")
    def test_z_ex9(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex9(conn)
        data = pd.read_csv("ex9.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True

    @weight(10)
    @visibility('visible')
    @number("z_ex_10")
    def test_z_ex_10(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex10(conn)
        data = pd.read_csv("ex10.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True

    @weight(10)
    @visibility('visible')
    @number("z_ex_11")
    def test_z_ex_11(self):
        normalized_database_filename = 'normalized.db'
        conn = self.mini_project2.create_connection(normalized_database_filename)
        sql_statement = self.mini_project2.ex11(conn)
        data = pd.read_csv("ex11.csv")
        df = pd.read_sql_query(sql_statement, conn)
        assert df.equals(data) == True



