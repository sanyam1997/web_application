from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10

import time
# import unittest

class NewVisitorTest( LiveServerTestCase) :

    def setUp( self ) :
        self.browser = webdriver.Firefox( )

    def tearDown( self ) :
        self.browser.quit( )

    def check_for_row_in_list_table( self , row_text ) :
        table = self.browser.find_element_by_id( "id_list_table" )
        rows = table.find_elements_by_tag_name( "tr" )
        self.assertIn( row_text , [ row.text for row in rows ] )

    def test_can_start_a_list_and_retrieve_it_later( self ) :
        # Sanyam has heard about this cool new online to-do app. He goes
        # to checkout its homepage.
        self.browser.get( self.live_server_url )
        # She notices the page title and header mention to-do lists
        self.assertIn( "To-Do" , self.browser.title )
        header_text = self.browser.find_element_by_tag_name( "h1" ).text
        self.assertIn( "To-Do" , header_text )

        # He is invited to a to-do item straight away.
        inputbox = self.browser.find_element_by_id( "id_new_item" )
        self.assertEqual(
            inputbox.get_attribute( "placeholder" ) ,
            "Enter a to-do item"
        )
        # He types "Buy peacock feathers" into a text box ( Sanyam' hobby is typing in
        # fly-fishing lures)
        inputbox.send_keys( "Buy peacock feathers" )

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in to-do list
        inputbox.send_keys( Keys.ENTER )
        self.wait_for_row_in_list_table( "1: Buy peacock feathers" )

        self.check_for_row_in_list_table( "1: Buy peacock feathers" )

        inputbox = self.browser.find_element_by_id( "id_new_item" )
        inputbox.send_keys( "Use peacock feathers to make a fly" )
        inputbox.send_keys( Keys.ENTER )
        # time.sleep( 1 )

        self.wait_for_row_in_list_table( "2: Use peacock feathers to make a fly" )
        self.wait_for_row_in_list_table( '1: Buy peacock feathers' )
        self.check_for_row_in_list_table( "1: Buy peacock feathers" )
        self.check_for_row_in_list_table( "2: Use peacock feathers to make a fly" )
        # self.assertIn( "2: Use peacock feathers to fly" , [ row.text for row in rows ] )
        # self.assertTrue(
        #     any( row.text == '1: Buy peacock feathers' for row in rows ) ,
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )
        # There is still a text box inviting her to add another item. He
        # enters "Use peacock feathers to make a fly" ( Sanyam is very
        # methodical )
        self.fail( "Finish the test." )

        # The page updates again, and now shows both items on her list

        # Sanyam wonders whether the site still remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # text to that effect.

        # He visits the URL - his to-do list is still there.

    def wait_for_row_in_list_table( self , row_text ) :
        start_time = time.time( )
        while True:
            try:
                table = self.browser.find_element_by_id( "id_list_table" )
                rows = table.find_elements_by_tag_name( "tr" )
                self.assertIn( row_text , [ row.text for row in rows ] )
                return
            except ( AssertionError , WebDriverException ) as e:
                if time.time( ) - start_time > MAX_WAIT :
                    raise e
                time.sleep(0.5)


# if __name__ == "__main__" :
#     unittest.main( warnings = 'ignore' )
