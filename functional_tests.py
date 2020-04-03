from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest( unittest.TestCase ) :

    def setUp( self ) :
        self.browser = webdriver.Firefox( )

    def tearDown( self ) :
        self.browser.quit( )

    def test_can_start_a_list_and_retrieve_it_later( self ) :
        # Sanyam has heard about this cool new online to-do app. He goes
        # to checkout its homepage.
        self.browser.get( "http:/localhost:8000" )
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
        inputbox.send_keys( keys.ENTER )
        time.sleep( 1 )

        table = self.browser.find_element_by_id( "id_list_table" )
        rows = table.find_elements_by_tag_name( "tr" )
        self.assertTrue(
            any( row.text == '1: Buy peacock feathers' for row in rows )
        )
        # There is still a text box inviting her to add another item. He
        # enters "Use peacock feathers to make a fly" ( Sanyam is very
        # methodical )
        self.fail( "Finish the test." )

        # The page updates again, and now shows both items on her list

        # Sanyam wonders whether the site still remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # text to that effect.

        # He visits the URL - his to-do list is still there.

if __name__ == "__main__" :
    unittest.main( warnings = 'ignore' )

if __name__ == "__main__" :
    unittest.main( warnings = 'ignore' )
