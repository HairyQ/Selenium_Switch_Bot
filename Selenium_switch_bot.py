import sys, time, signal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

email = 'YOUR_BESTBUY_EMAIL_HERE'
password = 'YOUR_PASSWORD_HERE'

def sign_in(isOrdered):
    driver = webdriver.Firefox()
    driver.get('https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255')

    assert 'Best Buy' in driver.title
    acct_button = driver.find_elements_by_class_name('BtnTxt')[0]
    actions = ActionChains(driver)
    actions.move_to_element(acct_button)
    actions.click(acct_button)
    actions.perform()
    driver.implicitly_wait(5)

    sign_in_button = driver.find_element_by_link_text('Sign In')
    actions = ActionChains(driver)
    actions.move_to_element(sign_in_button)
    actions.click(sign_in_button)
    actions.perform()
    driver.implicitly_wait(10)

    time.sleep(4)
    user_element = driver.find_element_by_id("fld-e")
    user_element.send_keys(email)
    pass_element = driver.find_element_by_id('fld-p1')
    pass_element.send_keys(password)

    new_sign_in_button = driver.find_element_by_class_name('cia-form__controls')
    actions = ActionChains(driver)
    actions.move_to_element(new_sign_in_button)
    actions.click(new_sign_in_button)
    actions.perform()
    driver.implicitly_wait(5)

    time.sleep(5)
    run_bot(isOrdered, driver)

def run_bot(isOrdered, driver):
    while 1:
        if isOrdered:
            break
        try:
            driver.refresh()
            button = driver.find_element_by_class_name('add-to-cart-button')

            driver.execute_script("window.scrollTo(0, 250)")
            time.sleep(5)

            if button.text == "Sold Out" or button.text == "Check Stores":
                print('Sold out')
                continue

            elif button.text == "Add to Cart":
                print('Was able to check one out - hopefully button is clickable...')
                time.sleep(3)
                action = ActionChains(driver)
                action.move_to_element(button)
                action.click(button)
                action.perform()
                time.sleep(3)

        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Survey popup')
            continue
            #driver.close()
            #sign_in(isOrdered)

        action1 = ActionChains(driver)
        try:
            cart_button = driver.find_element_by_class_name('cart-nav')
            action1.move_to_element(cart_button)
            action1.click(cart_button)
            action1.perform()
        except KeyboardInterrupt:
            print('Bye')
            exit()
        except NoSuchElementException:
            action2 = ActionChains(driver)
            print('exception reached')
            cart_button = driver.find_element_by_class_name('cart-icon-container')
            driver.execute_script("window.scrollTo(0, 0)")
            action2.move_to_element(cart_button)
            action2.click(cart_button)
            action2.perform()

        time.sleep(4)

        i = 0
        while i < 10:
            i += 1
            try:
                time.sleep(3)
                action_ensure_only_one = ActionChains(driver)
                amt_dropdown = driver.find_element_by_class_name('c-dropdown')
                action_ensure_only_one.move_to_element(amt_dropdown)
                action_ensure_only_one.click(amt_dropdown)
                action_ensure_only_one.send_keys('1')
                action_ensure_only_one.send_keys(u'\ue007')
                action_ensure_only_one.perform()
                break
            except KeyboardInterrupt:
                print('Bye')
                exit()
            except:
              continue


        try:
            free_shipping = None
            shipping_methods = driver.find_elements_by_class_name('availability__fulfillment')
            for shipping_method in shipping_methods:
                if 'FREE Shipping' in shipping_method.text:
                    free_shipping = shipping_method
                    break
                else:
                    continue

            if free_shipping:
                free_shipping = free_shipping.find_element_by_name('availability-selection')
                action3 = ActionChains(driver)
                action3.move_to_element(free_shipping)
                action3.click(free_shipping)
                action3.perform()
                time.sleep(3)

                checkout_button = driver.find_element_by_class_name('checkout-buttons__checkout')
                checkout_button = checkout_button.find_element_by_class_name('btn-primary')

                action4 = ActionChains(driver)
                action4.move_to_element(checkout_button)
                action4.click(checkout_button)
                action4.perform()
                time.sleep(5)

                final_button = driver.find_element_by_class_name('button__fast-track')

                time.sleep(6)

                final_button.send_keys(Keys.PAGE_DOWN)

                time.sleep(3)

                action5 = ActionChains(driver)
                action5.move_to_element(final_button)
                action5.click(final_button)
                action5.perform()

                print('Transaction Complete!')
                isOrdered += 1
                driver.close()
                break

            else:
                print('failed to order')
                driver.close()
                sign_in(isOrdered)

        except KeyboardInterrupt:
            print('Bye')
            exit()
        except:
            print('Survey popup reached')
            driver.close()
            sign_in(isOrdered)
        
isOrdered = 0
sign_in(isOrdered)
exit()
