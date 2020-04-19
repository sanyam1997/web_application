from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest( FunctionalTest ) :

    def test_can_start_a_list_for_one_user( self ):

        # Sanyam has heard about this cool new online to-do app. He goes
        # to checkout its homepage.
        self.browser.get( self.live_server_url )
        # She notices the page title and header mention to-do lists
        self.assertIn( "To-Do" , self.browser.title )
        header_text = self.browser.find_element_by_tag_name( "h1" ).text
        self.assertIn( "To-Do" , header_text )

        # He is invited to a to-do item straight away.
        inputbox = self.get_item_input_box( )
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

        inputbox = self.get_item_input_box( )
        inputbox.send_keys( "Use peacock feathers to make a fly" )
        inputbox.send_keys( Keys.ENTER )
        # time.sleep( 1 )

        self.wait_for_row_in_list_table( "2: Use peacock feathers to make a fly" )
        self.wait_for_row_in_list_table( '1: Buy peacock feathers' )
        # There is still a text box inviting her to add another item. He
        # enters "Use peacock feathers to make a fly" ( Sanyam is very
        # methodical )

        # The page updates again, and now shows both items on his list
        self.check_for_row_in_list_table( "1: Buy peacock feathers" )
        self.check_for_row_in_list_table( "2: Use peacock feathers to make a fly" )

        # Sanyam wonders whether the site still remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # text to that effect.

        # He visits the URL - his to-do list is still there.
        # The page updates again, and now shows both items on his list

    def test_multiple_users_can_start_lists_at_different_urls( self ) :
        # Sanyam has a new to-do list
        self.browser.get( self.live_server_url )
        inputbox = self.get_item_input_box( )
        inputbox.send_keys( "Buy peacock feathers" )
        inputbox.send_keys( Keys.ENTER )
        self.wait_for_row_in_list_table( "1: Buy peacock feathers" )

        # He notices that his list has a unique URL
        sanyam_list_url = self.browser.current_url
        self.assertRegex( sanyam_list_url , '/lists/.+' )

        # Now a new user, Edith, comes along to the site.

        # We use a new browser session to make sure that no information
        # of Sanyam's is coming through from cookies etc
        self.browser.quit( )
        self.browser = webdriver.Firefox( )

        # Francis visits the home page. There is no sign of Sanyam's
        # list
        self.browser.get( self.live_server_url )
        page_text = self.browser.find_element_by_tag_name( "body" ).text
        self.assertNotIn( "Buy peacock feathers" , page_text )
        self.assertNotIn( "make a fly" , page_text )

        # Francis starts a new list by entering a new item. He is
        # less interesting than Sanyam.
        inputbox = self.get_item_input_box( )
        inputbox.send_keys( "Buy milk" )
        inputbox.send_keys( Keys.ENTER )
        self.wait_for_row_in_list_table( "1: Buy milk" )

        # Francis got his own URL
        francis_list_url = self.browser.current_url
        self.assertRegex( francis_list_url , '/lists/.+' )
        self.assertNotEqual( francis_list_url , sanyam_list_url )

        # Again, there is no trace of Sanyam's URL
        page_text = self.browser.find_element_by_tag_name( "body" ).text
        self.assertNotIn( "Buy peacock feathers" , page_text )
        self.assertIn( "Buy milk" , page_text )
        # Satisfied they go back to sleep
