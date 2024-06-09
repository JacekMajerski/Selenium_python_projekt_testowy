from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
#Lokalizatory- Czy buttony dawać wielkimi literami? Czy przyjąć jakąś kolejność? jeśli tak to jaką?

    GO_BUTTON = (By.ID, 'submit')
    username_textbox = (By.ID, 'username')
    register_username_textbox = (By.ID, 'reg_email')
    password_textbox = (By.ID, 'password')
    register_password_textbox = (By.ID, 'reg_password')
    login_button = (By.CSS_SELECTOR, "[name='login']")
    register_button = (By.CSS_SELECTOR, "[name='register']")
    not_correct_password = (By.CSS_SELECTOR, ".woocommerce-error")
    create_account_button = (By.CSS_SELECTOR, ".btn-primary")
    username_ethereal = (By.CSS_SELECTOR, "div:nth-of-type(2) tr:nth-of-type(2) code")
    name_in_my_account =(By.CSS_SELECTOR, "strong:nth-of-type(1)")
    lost_your_password = (By.CSS_SELECTOR, ".woocommerce-LostPassword > a")
    lost_user_login = (By.ID, "user_login")
    reset_password_button = (By.CSS_SELECTOR, "[value='Reset password']")
    logout_my_account = (By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout > a")
    not_reset_email = (By.CSS_SELECTOR, ".woocommerce-message")
    breadcrumbs_my_account = (By.CSS_SELECTOR, "[rel='home']")

class MainPageLocators(object):

    go_to_shop = (By.XPATH, "//ul[@id='topbar-menu']/li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-21']//span[@class='nav__title']")
    go_to_cart_main_menu = (By.XPATH, "//ul[@id='topbar-menu']/li[@class='menu-item menu-item-type-post_type menu-item-object-page menu-item-20']//span[@class='nav__title']")
    go_to_cart_icon = (By.CSS_SELECTOR, "[data-toggle='czr-dropdown'] > .icn-shoppingcart")
    go_to_search = (By.CSS_SELECTOR, ".regular-nav.utils .search-toggle_btn")
    search_describe = (By.XPATH, "//div[@class='search__wrapper']//div[@class='form-group czr-focus']")
    search_field = (By.XPATH, "//div[@class='search__wrapper']//input[@name='s']")
    search_results = (By.CSS_SELECTOR, ".czr-title")
    button_shop_banner = (By.XPATH, "//div[@class='sektion-wrapper']//a[.='Shop']")
    second_post_icon = (By.CSS_SELECTOR, ".post-41 > .grid__item")
    hello_world_icon = (By.CSS_SELECTOR, ".post-39 .bg-link")

class ShopPageLocators(object):
    button_add_to_cart_bdd = (By.XPATH, "//li[@class='post-29 product type-product status-publish has-post-thumbnail product_cat-courses first instock shipping-taxable purchasable product-type-simple']/a[.='Add to cart']")
    button_after_adding_to_cart = (By.CSS_SELECTOR, ".added")
    number_in_icon_basket = (By.CSS_SELECTOR, "[data-toggle='czr-dropdown'] > .count")
    product_name_in_shop = (By.CSS_SELECTOR, ".woocommerce-loop-product__title")
    product_price_in_shop = (By.CSS_SELECTOR, ".post-29 .woocommerce-Price-amount")
    product_name_in_mini_basket = (By.CSS_SELECTOR, ".woocommerce-mini-cart-item > a:nth-of-type(2)")
    product_price_in_mini_basket = (By.CSS_SELECTOR, ".woocommerce-mini-cart__total > .woocommerce-Price-amount")
    icon_on_mini_basket = (By.CSS_SELECTOR, ".mCS_img_loaded")
    button_view_cart = (By.XPATH, "//a[.='View cart']")
    button_checkout = (By.XPATH, "//a[.='Checkout']")

class CartPageLocators(object):
    cart_describe = (By.CSS_SELECTOR, ".cart-empty")
    button_return_to_shop = (By.XPATH, "//a[contains(.,'Return to shop')]")
    enter_code = (By.XPATH, "//a[.='Click here to enter your code']")
    fill_code = (By.XPATH, "//input[@id='coupon_code']")
    button_apply_coupon = (By.XPATH, "//button[@name='apply_coupon']")
    notify_bad_coupon = (By.CSS_SELECTOR, ".woocommerce-error")
    first_name = (By.CSS_SELECTOR, "#billing_first_name")
    last_name = (By.CSS_SELECTOR, "#billing_last_name")
    company_name = (By.CSS_SELECTOR, "#billing_company")
    street_address = (By.ID, "billing_address_1")
    street_address_optional = (By.ID, "billing_address_2")
    postcode = (By.CSS_SELECTOR, "#billing_postcode")
    city = (By.ID, "billing_city")
    phone = (By.ID, "billing_phone")
    email_address = (By.ID, "billing_email")
    button_place_order = (By.ID, "place_order")
    first_name_error = (By.XPATH, "//li[contains(.,'Billing First name is a required field.')]")
class OrdersPageLocators(object):
    order_notice = (By.CSS_SELECTOR, ".woocommerce-notice")
    product_link = (By.XPATH, "//a[.='BDD Cucumber']")
    order_number = (By.CSS_SELECTOR, '.order > strong')
    order_date = (By.CSS_SELECTOR, '.date > strong')
    order_price = (By.CSS_SELECTOR, '.total .woocommerce-Price-amount')
    order_payment_method = (By.CSS_SELECTOR, '.method > strong')



class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass

